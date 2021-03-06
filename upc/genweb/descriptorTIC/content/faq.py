# -*- coding: utf-8 -*-

"""Definition of the servei content type
"""

from zope.interface import implements, directlyProvides
from AccessControl import ClassSecurityInfo
from DateTime import DateTime

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent

from zope.component import getMultiAdapter, getUtility

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
            label_msgid="faqTIC_serveis_relacionats",
            description_msgid="faqTIC_descrip_serveis_relacionats",
            i18n_domain = "upc.genweb.descriptorTIC"
        ),
    ),

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
        mt = portal_catalog.searchResults(portal_type = 'ServeiTIC',
                                          path={"query": '/'.join(self.getParentNode().getParentNode().getPhysicalPath()),"depth":2},
                                          sort_on='Date')
        new_list=[]
        for f in mt:
            new_list.append(f.Title)
        new_list.sort()
        return new_list

    def serviciosEnlace(self):
        serveis = self.getListaservei()
        new = []
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'ServeiTIC',
                                          path={"query": '/'.join(self.getParentNode().getParentNode().getPhysicalPath()),"depth":2},
                                          )

        for i in serveis:
            for j in mt:
                if i==j.Title:
                    new.append(j)
        return new
        
    def serviciosPath(self):
        serveis = self.serviciosEnlace()
        return [s.getPath() for s in serveis]
        

atapi.registerType(Faq, PROJECTNAME)



