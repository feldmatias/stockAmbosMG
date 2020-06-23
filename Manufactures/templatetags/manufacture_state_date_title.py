from django import template

from Manufactures.models import Manufacture

register = template.Library()


@register.filter
def manufacture_state_date_title(state):
    state_dates = {
        Manufacture.STATUS_CUT: 'Fecha de corte',
        Manufacture.STATUS_SEWING: 'Fecha de envío a costura'
    }

    return state_dates.get(state, 'Fecha')
