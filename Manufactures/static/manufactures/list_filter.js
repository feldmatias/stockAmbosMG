function filter_manufactures_by_product(product_id) {
    if (product_id == 0) {
        $('.manufacture-list-item').show();
    } else {
        $('.manufacture-list-item').hide();
        $('.manufacture-list-item-' + product_id).show();
    }
}