from Manufactures.models import Manufacture


class ManufactureListDecorator:
    def __init__(self, state):
        self.state = state
        self._initialize_manufactures()

    def all_states(self):
        return Manufacture.STATES

    def state(self):
        return self.state

    def manufactures(self):
        return self.manufactures

    def _initialize_manufactures(self):
        self.manufactures = Manufacture.repository.find_by_state(self.state) if self.state else []
