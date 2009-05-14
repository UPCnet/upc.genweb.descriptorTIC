# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType

def isNotdescriptorProfile(context):
    return context.readDataFile("marker.txt") is None


def postInstall(context):
    """Last import step. """
    # the right place for your custom code
    if isNotdescriptorProfile(context): return
    site = context.getSite()
    
    # Crear ploneboard
    forums_en = crearObjecte(site,'forums-en','Ploneboard','Forum space','',)
    forums_es = crearObjecte(site,'forums-es','Ploneboard','Espacio de foros','',)
    forums_ca = crearObjecte(site,'forums-ca','Ploneboard','Espai de fòrums','',)
    setLanguageAndLink([(forums_ca,'ca'),(forums_es,'es'),(forums_en,'en')])
    
    
def setLanguageAndLink(items):
    canonical,canonical_lang = items[0]
    for item,language in items:
        item.setLanguage(language)
#        if item!=canonical and canonical_lang not in item.getTranslations().keys():
#            item.addTranslationReference(canonical)

def getObjectStatus(context):
    pw = getToolByName(context, "portal_workflow") 
    object_workflow = pw.getWorkflowsFor(context)[0].id
    object_status = pw.getStatusOf(object_workflow,context)
    return object_status

def doWorkflowAction(context):
    pw = getToolByName(context, "portal_workflow") 
    object_workflow = pw.getWorkflowsFor(context)[0].id
    object_status = pw.getStatusOf(object_workflow,context)
    if object_status:
        try:
            pw.doActionFor(context,{'genweb_simple':'publish','genweb_review':'publicaalaintranet'}[object_workflow])
        except:
            pass
    
def crearObjecte(context,id,type_name,title,description,exclude=True,constrains=None):
    pt = getToolByName(context,'portal_types')
    if not getattr(context,id,False) and type_name in pt.listTypeTitles().keys():
        #creem l'objecte i el publiquem
        _createObjectByType(type_name, context, id)
    #populem l'objecte
    created = context[id]            
    doWorkflowAction(created)    
    created.setTitle(title)
    created.setDescription(description)
    created._at_creation_flag=False
    try:
        created.setExcludeFromNav(exclude)
    except:
        pass
    if constrains:
        created.setConstrainTypesMode(1)
        created.setLocallyAllowedTypes(tuple(constrains[0]+constrains[1]))
        created.setImmediatelyAddableTypes(tuple(constrains[0]))
                            
    created.reindexObject()
    return created

