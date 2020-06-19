from urllib.parse import urlencode

import requests


class MercadoLibreService:

    def get_authorization_url(self, meli_user, redirect_url):
        params = {'client_id': meli_user.client_id, 'response_type': 'code', 'redirect_uri': redirect_url}
        url = 'https://auth.mercadolibre.com.ar/authorization' + '?' + urlencode(params)
        return url

    def authorize_user(self, meli_user, code, redirect_url):
        params = {'grant_type': 'authorization_code', 'client_id': meli_user.client_id,
                  'client_secret': meli_user.client_secret,
                  'code': code, 'redirect_uri': redirect_url}

        authorized = self.set_user_authorization(meli_user, params)
        if not authorized:
            return False

        self.get_user_id(meli_user)
        return True

    def refresh_access_token(self, meli_user):
        params = {'grant_type': 'refresh_token', 'client_id': meli_user.client_id,
                  'client_secret': meli_user.client_secret,
                  'refresh_token': meli_user.refresh_token}

        return self.set_user_authorization(meli_user, params)

    def set_user_authorization(self, meli_user, params):
        url = 'https://api.mercadolibre.com/oauth/token'

        response = requests.post(url, params=params)
        if response.status_code != 200:
            return False

        data = response.json()
        access_token = data['access_token']
        refresh_token = data['refresh_token']
        token_expires_in = data['expires_in']

        meli_user.set_access_token(access_token, refresh_token, token_expires_in)
        return True

    def check_access_token(self, meli_user):
        if meli_user.token_expired():
            self.refresh_access_token(meli_user)

    def get_user_id(self, meli_user):
        self.check_access_token(meli_user)
        url = 'https://api.mercadolibre.com/users/me'
        params = {'access_token': meli_user.access_token}

        response = requests.get(url, params=params)
        if response.status_code != 200:
            return False

        user_id = response.json()['id']
        meli_user.set_user_id(user_id)
        return True

    def get_items(self, meli_user):
        self.check_access_token(meli_user)
        url = f"https://api.mercadolibre.com/users/{meli_user.user_id}/items/search"
        params = {'access_token': meli_user.access_token}

        response = requests.get(url, params=params)
        if response.status_code != 200:
            return []

        items = response.json()['results']
        result = {}
        for item in items:
            result[item] = self.get_item_title(meli_user, item)
        return result

    def get_item_title(self, meli_user, item):
        self.check_access_token(meli_user)
        url = "https://api.mercadolibre.com/items"
        params = {'access_token': meli_user.access_token, 'ids': item}

        response = requests.get(url, params=params)
        return response.json()[0]['body']['title']

    def get_item_variations(self, meli_item):
        self.check_access_token(meli_item.meli_user)
        url = "https://api.mercadolibre.com/items"
        params = {'access_token': meli_item.meli_user.access_token, 'ids': meli_item.item_id}

        response = requests.get(url, params=params)
        if response.status_code != 200:
            return []

        items = response.json()[0]['body']['variations']
        variations = []
        for variation in items:
            data = {
                'id': variation['id'],
                'size': list(filter(lambda x: x['id'] == 'SIZE', variation['attribute_combinations']))[0]['value_name'],
                'color': list(filter(lambda x: x['id'] == 'COLOR', variation['attribute_combinations']))[0][
                    'value_name'],
            }
            variations.append(data)

        return variations

    def update_stock(self, stock):
        from MercadoLibre.models import MeliItemMapping
        mappings = MeliItemMapping.objects.get_all_for(stock.color, stock.size).select_related('meli_item',
                                                                                               'meli_item__product',
                                                                                               'meli_item__meli_user')
        for mapping in mappings:
            item = mapping.meli_item
            variation_id = mapping.item_id

            url = f"https://api.mercadolibre.com/items/{item.item_id}/variations/{variation_id}?access_token={item.meli_user.access_token}"
            for i in range(50):
                response = requests.put(url, json={"available_quantity": stock.stock})
                if response.status_code == 200:
                    break
