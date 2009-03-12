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
        label = _(u"Fitxa de Servei"),
        label_msgid = "servei_tic_nom",
        description = _(u"Indica el nom del servei"),
        description_msgid="servei_tic_description",
        i18n_domain = "upc.genweb.descriptorTIC")
    ),

    atapi.TextField('directedto',
        required=True,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            label = _(u"A qui s'adreça"),
            label_msgid = _(u"label_directedto_description"), 
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"), 
        schemata="default",
    ),

    atapi.StringField(
        name='colectiu',
        required = True,
        widget=atapi.MultiSelectionWidget(
            label = _(u'servei_tic_collectiu', default=u'Col·lectiu'),
            format = 'checkbox',
            i18n_domain='upctv.media',
        ),
        languageindependent=True,
        vocabulary='getColectius',
        schemata="default",
    ),

    atapi.TextField('descripcion_corta',
        required=True,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            label = _(u"Descripció curta"),
            label_msgid = _(u"label_description_curta"),
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"),
        schemata="default",
    ),

    atapi.TextField('descripcion_larga',
        required=True,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            label = _(u"Descripció llarga"),
            label_msgid = _(u"label_description_llarga"),
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"),
        schemata="default",
    ),

    atapi.TextField('suport',
        required=True,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            label = _(u"Suport"),
            label_msgid = _(u"label_suport"),
            rows  = 10,
            i18n_domain = "upc.genweb.descriptorTIC"),
        schemata="default",
    ),

    atapi.TextField('indicadors',
        required=True,
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            label = _(u"Indicadors"),
            label_msgid = _(u"label_indicadors"),
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
            label = _(u'label_normativa', default=u'Normativa'),
            description = '',
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
            label = _(u'label_manuals_documentacio', default=u'Manuals i documentacio'),
            description = '',
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

