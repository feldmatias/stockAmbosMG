from django import template

from Manufactures.models import Manufacture

register = template.Library()


@register.filter
def state_action_next(state):
    state_actions = {
        Manufacture.STATUS_PREPARATION: 'Cortado',
        Manufacture.STATUS_CUT: 'En costura',
        Manufacture.STATUS_SEWING: 'Terminado'
    }

    return state_actions.get(state, 'Siguiente estado')
