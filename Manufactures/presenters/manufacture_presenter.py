class ManufacturePresenter:
    def __init__(self, product=None, manufacture=None):
        self.product = manufacture.product if manufacture else product
        self.manufacture = manufacture

    def product(self):
        return self.product

    def manufacture(self):
        return self.manufacture

    def selected_status(self):
        return self.manufacture.status if self.manufacture else ''

    def selected_size(self):
        return self.manufacture.size if self.manufacture else 0
