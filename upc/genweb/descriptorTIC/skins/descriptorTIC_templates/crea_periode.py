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
from DateTime import DateTime

#1. copiar periode exemple
titol = context.REQUEST.get('titol')
descripcio = context.REQUEST.get('descripcio')
inici = context.REQUEST.get('inici')
fi = context.REQUEST.get('fi')
termini = context.REQUEST.get('termini')
portal_types = getToolByName(context, 'portal_types')

carpeta_unitats = getattr(portal_types, 'unitats', False)
carpeta_base = getattr(carpeta_unitats, 'osi', False)                           #carpeta on guardem periode exemple
periode_copy = carpeta_base.manage_copyObjects(['periode-dexemple'])            #id objecte base
if not carpeta_unitats or not carpeta_base:
   context.plone_utils.addPortalMessage(("El període d'exemple ha estat modificat, eliminat o mogut. Siusplau, assegura't que el període d'exemple existeix i està a la carpeta 'configuracio-periodes' de l'arrel del portal i el seu id és 'periode-dexemple'"), 'error')
   self.context.REQUEST.RESPONSE.redirect(self.context.absolute_url())

#2. guardar nou periode
periode_paste = context.manage_pasteObjects(periode_copy)    
nou_id = periode_paste[0]['new_id']
nou_periode = getattr(context, nou_id)


#3. modifiquem dades
nou_periode.edit(title = str(titol),
    description = descripcio,
    datainicial = inici,
    datafinal = fi,
    datalimit = termini,
    )

#4. eliminem els subobjectes no marcats
url = join(nou_periode.getPhysicalPath(), '/')
preguntas = context.portal_catalog.searchResults(path=url, portal_type='SurveyTextQuestionGenweb')
camps_a_eliminar = []
for camp in preguntas: #noms dels camps del formulari (camp = 'camp12')
    object_camp = camp.getObject()
    context.portal_workflow.doActionFor(object_camp,'publish',comment='publised programmatically')
    id_camp = camp.getId
    if context.REQUEST.get(id_camp) is None:
    	camps_a_eliminar.append(id_camp)
    	
try:
    nou_periode.manage_delObjects(camps_a_eliminar)
except:
    context.plone_utils.addPortalMessage(("Alguns dels camps del període d'exemple han estat eliminats o modificat. Siusplau, assegura't que el període d'exemple conté els camps 'camp1', 'camp2' ... 'camp15'"), 'error')
    self.context.REQUEST.RESPONSE.redirect(self.context.absolute_url())

#5. modifiquem id (sino posa copy9_of_periode-dexemple)

nou_id_generat = nou_periode.pretty_title_or_id().replace(' ', '_')
try:
    nou_periode.setId(nou_id_generat)
except:
    data_actual = DateTime(context.Date()).strftime('%d.%m.%Y')
    nou_periode.setId(nou_id_generat + data_actual)

#6. modifiquem url de sortida amb el nou id
nou_periode.edit(
    exitUrl = nou_periode.absolute_url()
    )



context.plone_utils.addPortalMessage(("El nou periode ha estat creat correctament"))
context.REQUEST.RESPONSE.redirect(nou_periode.absolute_url())
