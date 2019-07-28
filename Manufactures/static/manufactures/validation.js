function validate_manufacture_form() {
    let valid = false;

    $('.product-color-input').each(function () {
        if ($(this).val() > 0) {
            valid = true;
        }
    });

    if (!valid) {
        alert('El corte debe tener por lo menos un color');
    }
    return valid;
}