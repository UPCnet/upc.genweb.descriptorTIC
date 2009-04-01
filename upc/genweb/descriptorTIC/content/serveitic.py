# -*- coding: utf-8 -*-

"""Definition of the servei content type
"""

from zope.interface import implements, directlyProvides
from AccessControl import ClassSecurityInfo
from DateTime import DateTime

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent

from Products.Archetypes import atapi
from Products.Archetypes.public import DisplayList
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.configuration import zconf
from Products.validation import V_REQUIRED

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _
from upc.genweb.descriptorTIC.interfaces import IServeiTIC
from upc.genweb.descriptorTIC.config import PROJECTNAME

from Products.ATContentTypes.content.document import ATDocumentSchema, ATDocument
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

servei_tic_Schema = ATDocumentSchema.copy() + atapi.Schema((

    atapi.StringField(
    name = 'title',
    required = True,
    searchable = 1,
    widget = atapi.StringWidget(
        #label = _(u"Fitxa de Servei"),
        label_msgid="serveiTIC_nom",
        #description = _(u"Indica el nom del servei"),
        description_msgid="serveiTIC_descripcio_nom",
        i18n_domain = "upc.genweb.descriptorTIC")
    ),

    atapi.TextField('directedto',
        required = False,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            #label = _(u"A qui s'adreça"),
            label_msgid="serveiTIC_adreca", 
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"), 
        schemata="default",
    ),

    atapi.StringField(
        name='colectiu',
        required = False,
        widget=atapi.MultiSelectionWidget(
            #label = _(u'servei_tic_collectiu', default=u'Col·lectiu'),
 	    label_msgid="serveiTIC_collectiu",
            format = 'checkbox',
            i18n_domain = "upc.genweb.descriptorTIC",
        ),
        languageindependent=True,
        vocabulary='getColectius',
        schemata="default",
    ),

    atapi.TextField('descripcion_corta',
        required = False,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            #label = _(u"Descripció curta"),
            label_msgid="serveiTIC_descrip_curta",
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"),
        schemata="default",
    ),

    atapi.TextField('descripcion_larga',
        required = False,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            #label = _(u"Descripció llarga"),
            label_msgid="serveiTIC_descrip_llarga",
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"),
        schemata="default",
    ),

    atapi.TextField('suport',
        required = False,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            #label = _(u"Suport"),
            label_msgid="serveiTIC_suport",
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"),
        schemata="default",
    ),

    atapi.TextField('indicadors',
        required = False,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            #label = _(u"Indicadors"),
            label_msgid="serveiTIC_indicadors",
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"),
        schemata="default",
    ),


    atapi.ReferenceField('normativa',
        relationship = 'normativarelatesTo',
        multiValued = True,
        isMetadata = True,
        languageIndependent = False,
        write_permission = ModifyPortalContent,
        widget = ReferenceBrowserWidget(
            allow_search = True,
            allow_browse = True,
            show_indexes = False,
            force_close_on_insert = True,
            #label = _(u'label_normativa', default=u'Normativa'),
            label_msgid="serveiTIC_normativa",
	    description = '',
	    i18n_domain = "upc.genweb.descriptorTIC"
            ),
     ),

    atapi.ReferenceField('manuales_documentacio',
        relationship = 'man_doc_relatesTo',
        multiValued = True,
        isMetadata = True,
        languageIndependent = False,
        write_permission = ModifyPortalContent,
        widget = ReferenceBrowserWidget(
            allow_search = True,
            allow_browse = True,
            show_indexes = False,
            force_close_on_insert = True,
            #label = _(u'label_manuals_documentacio', default=u'Manuals i documentacio'),
	    label_msgid="serveiTIC_manuals",
            description = '',
            i18n_domain = "upc.genweb.descriptorTIC"
        ),
     ),

))

schemata.finalizeATCTSchema(servei_tic_Schema, moveDiscussion=False)

servei_tic_Schema['text'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}

class ServeiTIC(ATDocument):
    """Servei Descriptor TIC"""

    portal_type = "ServeiTIC"
    schema = servei_tic_Schema

    implements(IServeiTIC)

    def getColectius(self):
        return ['EST','PAS','PDI']

atapi.registerType(ServeiTIC, PROJECTNAME)
