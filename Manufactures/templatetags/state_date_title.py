from django import template

from Manufactures.models import Manufacture

register = template.Library()


@register.filter
def state_date_title(state):
    state_dates = {
        Manufacture.STATUS_PREPARATION: 'Fecha de creación',
        Manufacture.STATUS_CUT: 'Fecha de corte',
        Manufacture.STATUS_SEWING: 'Fecha de envío a costura'
    }

    return state_dates.get(state, 'Fecha')
