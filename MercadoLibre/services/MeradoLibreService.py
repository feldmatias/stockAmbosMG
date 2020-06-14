from urllib.parse import urlencode

import requests


class MercadoLibreService:

    def get_authorization_url(self, meli_user, redirect_url):
        params = {'client_id': meli_user.app_id, 'response_type': 'code', 'redirect_uri': redirect_url}
        url = 'https://auth.mercadolibre.com.ar/authorization' + '?' + urlencode(params)
        return url

    def authorize_user(self, meli_user, code, redirect_url):
        params = {'grant_type': 'authorization_code', 'client_id': meli_user.app_id, 'client_secret': meli_user.client_id,
                  'code': code, 'redirect_uri': redirect_url}

        return self.set_user_authorization(meli_user, params)

    def refresh_access_token(self, meli_user):
        params = {'grant_type': 'refresh_token', 'client_id': meli_user.app_id, 'client_secret': meli_user.client_id,
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
