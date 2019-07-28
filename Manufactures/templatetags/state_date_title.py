from django import template

from Manufactures.models import Manufacture

register = template.Library()


@register.filter
def state_date_title(state):
    state_dates = {
        Manufacture.STATE_PREPARATION: 'Fecha de creación',
        Manufacture.STATE_CUT: 'Fecha de corte',
        Manufacture.STATE_SEWING: 'Fecha de envío a costura'
    }

    return state_dates.get(state, 'Fecha')
