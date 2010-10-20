"""Definition of the AT Familia content type.
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

from upc.genweb.descriptorTIC.interfaces import IFamiliaTIC
from upc.genweb.descriptorTIC.config import PROJECTNAME
from Products.CMFCore.permissions import ModifyPortalContent

schema = Schema((
    ImageField(
        name='icono',
        widget=ImageField._properties['widget'](
            label='Imatge',
            label_msgid="familiatic_icono",
            description_msgid="familiatic_descrip_icono",
            i18n_domain = "upc.genweb.descriptorTIC"
        ),
        storage=AttributeStorage(),
    ),
),
)

FamiliaContainer_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

class FamiliaTIC(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(IFamiliaTIC)

    meta_type = 'FamiliaTIC'
    _at_rename_after_creation = True

    schema = FamiliaContainer_schema

registerType(FamiliaTIC, PROJECTNAME)

