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

# Take over the file schema from the ATContenttypes File content type
from Products.ATContentTypes.content.document import ATDocumentSchema, ATDocument

servei_tic_Schema = ATDocumentSchema.copy() + atapi.Schema((

))


schemata.finalizeATCTSchema(servei_tic_Schema, moveDiscussion=False)

class ServeiTIC(ATDocument):
    """Servei Descriptor TIC"""

    portal_type = "ServeiTIC"
    schema = servei_tic_Schema

    implements(IServeiTIC)

atapi.registerType(ServeiTIC, PROJECTNAME)

