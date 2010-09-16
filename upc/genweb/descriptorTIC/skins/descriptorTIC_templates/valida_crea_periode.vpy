titol = context.REQUEST.get('titol', '')
descripcio = context.REQUEST.get('descripcio', '')

if not titol:
    state.setError('titol', 'Introdueix el títol.')

if not descripcio:
    state.setError('descripcio', 'Introdueix la descripció.')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Corrige los errores marcados.')
else:
    return state.set(status='success', portal_status_message='El període ha estat creat correctament.')
