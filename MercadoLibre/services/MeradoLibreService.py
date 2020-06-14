from urllib.parse import urlencode


class MercadoLibreService:

    def get_authorization_url(self, meli_user, redirect_url):
        params = {'client_id': meli_user.app_id, 'response_type': 'code', 'redirect_uri': redirect_url}
        url = 'https://auth.mercadolibre.com.ar/authorization' + '?' + urlencode(params)
        return url
