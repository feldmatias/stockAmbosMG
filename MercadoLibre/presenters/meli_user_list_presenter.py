from MercadoLibre.models import MeliUser


class MeliUsersListPresenter:
    def __init__(self):
        self.users = MeliUser.objects.authorized().all()

    def users(self):
        return self.users
