from django.core.exceptions import ValidationError


class StockValidator:

    @staticmethod
    def validate(color, size):
        if color.product != size.product:
            raise ValidationError('Color and Size are from different products')
