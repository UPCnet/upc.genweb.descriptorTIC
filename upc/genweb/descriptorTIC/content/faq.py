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
from upc.genweb.descriptorTIC.interfaces import IFaq
from upc.genweb.descriptorTIC.config import PROJECTNAME

from Products.validation.config import validation
from AccessControl import ClassSecurityInfo

from Products.ATContentTypes.content.document import ATDocumentSchema, ATDocument
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

faq_tic_Schema = ATDocumentSchema.copy() + atapi.Schema((

    atapi.LinesField('listaservei',
                required=False,
                vocabulary='listaServicios',
                enforceVocabulary=True,
                widget=atapi.InAndOutWidget(
                    label="Lista de Servicios",
                    label_msgid="label_custom_view_fields",
                    description="Select which fields to display when ",
                    description_msgid="help_custom_view_fields",
                    i18n_domain = "plone"),
         ),

# Aquí es llisten el serveis de la Unitat. Seleccioneu de quins serveis és aquesta FAQ. Es mostraran quan estigui marcat 'Mostra com a taula'."

))

schemata.finalizeATCTSchema(faq_tic_Schema, moveDiscussion=False)

class Faq(ATDocument):
    """Servei Descriptor TIC"""

    portal_type = "Faq"
    schema = faq_tic_Schema

    implements(IFaq)

    security = ClassSecurityInfo()

    security.declareProtected(View, 'listaServicios')
    def listaServicios(self):
        """Return a list of metadata fields from portal_catalog.
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'ServeiTIC',path={"query":'/' + self.getPhysicalPath()[1] + '/' + self.getParentNode()._getURL(), "depth":2},sort_on='Date',review_state='published')
        new_list=[]
        for f in mt:
            new_list.append(f.Title)
        new_list.sort()
        return new_list

atapi.registerType(Faq, PROJECTNAME)



