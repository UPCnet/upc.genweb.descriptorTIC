## Controlled Python Script "nouperiodeview"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=titol, descripcio
##title=Validates nouperiode
##

# REQUIRED validations

if not titol:
    state.setError('titol', 'Introdueix el títol.','invalid_titol')

if not descripcio:
    state.setError('descripcio', 'Introdueix la descripció.,'invalid_descripcio')


if state.getErrors():
    return state.set(status='failure',
                     portal_status_message='Corrige los errores marcados.')
else:
    return state
