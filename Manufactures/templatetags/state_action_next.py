from django import template

from Manufactures.models import Manufacture

register = template.Library()


@register.filter
def state_action_next(state):
    state_actions = {
        Manufacture.STATE_PREPARATION: 'Cortado',
        Manufacture.STATE_CUT: 'En costura',
        Manufacture.STATE_SEWING: 'Terminado'
    }

    return state_actions.get(state, 'Siguiente estado')
