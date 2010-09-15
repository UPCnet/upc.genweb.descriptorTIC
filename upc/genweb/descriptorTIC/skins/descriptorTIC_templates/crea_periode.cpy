## Script (Python) "crea_periode"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=title=None
##title=Crea un nou periode
##

from Products.CMFCore.utils import getToolByName
from string import join


#1. copiar periode exemple
titol = context.REQUEST.get('titol')
descripcio = context.REQUEST.get('descripcio')
inici = context.REQUEST.get('inici')
fi = context.REQUEST.get('fi')
termini = context.REQUEST.get('termini')
body = 'Data inicial: ' + inici + '<br/>Data final: ' + fi + '<br/>Data final termini: ' + termini
portal_types = getToolByName(context, 'portal_types')
try:
   carpeta_base = getattr(portal_types, 'configuracio-periodes')                #carpeta on tenim base
   periode_copy = carpeta_base.manage_copyObjects(['periode-dexemple'])         #id objecte base
except:
   context.plone_utils.addPortalMessage(("El període d'exemple ha estat modificat, eliminat o mogut. Siusplau, assegura't que el període d'exemple existeix i està a la carpeta 'configuracio-periodes' de l'arrel del portal i el seu id és 'periode-dexemple'"), 'error')
   return

#2. guardar nou periode
periode_paste = context.manage_pasteObjects(periode_copy)    
nou_id = periode_paste[0]['new_id']
nou_periode = getattr(context, nou_id)

#3. modifiquem dades
nou_periode.edit(title = str(titol),
    description = descripcio,
    body = body,
    exitUrl = nou_periode.absolute_url()
    )

#4. eliminem els subobjectes no marcats
url = join(nou_periode.getPhysicalPath(), '/')
preguntas = context.portal_catalog.searchResults(path=url, portal_type='SurveyTextQuestion')
camps_a_eliminar = []
for camp in preguntas: #noms dels camps del formulari (camp = 'camp12')
    id_camp = camp.getId
    if context.REQUEST.get(id_camp) is None:
    	camps_a_eliminar.append(id_camp)
try:
    nou_periode.manage_delObjects(camps_a_eliminar)
except:
    context.plone_utils.addPortalMessage(("Alguns dels camps del període d'exemple han estat eliminats o modificat. Siusplau, assegura't que el període d'exemple conté els camps 'camp1', 'camp2' ... 'camp15'"), 'error')
    return

context.plone_utils.addPortalMessage(("El nou periode ha estat creat correctament"))
context.REQUEST.RESPONSE.redirect(nou_periode.absolute_url())
