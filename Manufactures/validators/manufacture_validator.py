from django.core.exceptions import ValidationError


class ManufactureValidator:

    @staticmethod
    def validate(product, size, colors):
        if not ManufactureValidator._validate_size(product, size):
            raise ValidationError('Size is from different product')

        if not ManufactureValidator._validate_colors(product, colors):
            raise ValidationError('Colors are from different product or are less than 0 or is empty')

    @classmethod
    def _validate_size(cls, product, size):
        return product == size.product

    @classmethod
    def _validate_colors(cls, product, colors):
        if not colors:
            return False

        for color, value in colors.items():
            if color.product != product or value <= 0:
                return False

        return True
