"""Definition of the AT Unitat content type.
"""
__author__ = """José Luis Vivanco C <jose.luis.vivanco@upcnet.es>"""
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.component import adapts

from Products.CMFCore.utils import getToolByName, _checkPermission
from Products.Archetypes.interfaces import IObjectPostValidation

from Products.Archetypes.atapi import *
from AccessControl import ClassSecurityInfo

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATContentTypes.content.folder import ATFolder

from upc.genweb.descriptorTIC.interfaces import IUnitatTIC
from upc.genweb.descriptorTIC.config import PROJECTNAME
from Products.CMFCore.permissions import ModifyPortalContent

schema = Schema((

),
)

UnitatContainer_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

class UnitatTIC(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(IUnitatTIC)

    meta_type = 'UnitatTIC'
    _at_rename_after_creation = True

    schema = UnitatContainer_schema

registerType(UnitatTIC, PROJECTNAME)

