from urllib.parse import urlencode

import requests


class MercadoLibreService:

    def get_authorization_url(self, meli_user, redirect_url):
        params = {'client_id': meli_user.client_id, 'response_type': 'code', 'redirect_uri': redirect_url}
        url = 'https://auth.mercadolibre.com.ar/authorization' + '?' + urlencode(params)
        return url

    def authorize_user(self, meli_user, code, redirect_url):
        params = {'grant_type': 'authorization_code', 'client_id': meli_user.client_id, 'client_secret': meli_user.client_secret,
                  'code': code, 'redirect_uri': redirect_url}

        authorized = self.set_user_authorization(meli_user, params)
        if not authorized:
            return False

        self.get_user_id(meli_user)

    def refresh_access_token(self, meli_user):
        params = {'grant_type': 'refresh_token', 'client_id': meli_user.client_id, 'client_secret': meli_user.client_secret,
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
