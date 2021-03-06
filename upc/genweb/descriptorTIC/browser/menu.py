from Acquisition import aq_inner

from zope.interface import implements
from zope.component import getMultiAdapter
from zope.app.component.hooks import getSite
from zope.app.publisher.browser.menu import BrowserMenu
from zope.app.publisher.browser.menu import BrowserSubMenuItem

from plone.memoize.instance import memoize
from plone.app.content.browser.folderfactories import _allowedTypes

from Products.CMFPlone import utils
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFCore.utils import getToolByName

from upc.genweb.descriptorTIC.interfaces import IConfigperiodeSubMenuItem
from upc.genweb.descriptorTIC.interfaces import IConfigperiodeMenu



class ConfigperiodeSubMenuItem(BrowserSubMenuItem):
    implements(IConfigperiodeSubMenuItem)

    title = _(u'label_configperiode_menu', default=u'Demanar indicadors')
    description = _(u'title_configperiode_menu', default=u'Configperiode for the current content item')
    submenuId = 'plone_contentmenu_configperiode'

    order = 10
    extra = {'id': 'plone-contentmenu-configperiode'}

    def __init__(self, context, request):
        BrowserSubMenuItem.__init__(self, context, request)
        self.context_state = getMultiAdapter((context, request), name='plone_context_state')

    def getToolByName(self, tool):
        return getToolByName(getSite(), tool)

    @property
    def action(self):
        folder = self.context
        if not self.context_state.is_structural_folder():
            folder = utils.parent(self.context)
        return folder.absolute_url() + '/folder_contents'


    @memoize
    def available(self):
        context = self.context
        usuari = context.portal_membership.getAuthenticatedMember()                                #mirem si lusuari te permis per afegir periodes
        rols = usuari.getRoles()
        if 'Manager' in rols or 'WebMaster' in rols:
        
            context_state = getMultiAdapter((context, self.request), name=u'plone_context_state')  #mirem si estem a carpeta 'osi'
            estem_a_osi = context.getPortalTypeName() == 'Folder' and context.getId() == 'osi'
            portal_types = getToolByName(context, 'portal_types')
            carpeta_unitats = getattr(portal_types, 'unitats', False)
            carpeta_base = getattr(carpeta_unitats, 'osi', False)
            if carpeta_unitats and carpeta_base:
                vista_per_defecte = carpeta_base.getDefaultPage()
                estem_a_vista_per_defecte_osi = vista_per_defecte == context.getId()
                if estem_a_osi or estem_a_vista_per_defecte_osi:

                    factories_view = getMultiAdapter((context, self.request), name='folder_factories') #mirem si podem afegir periodes
                    addContext = factories_view.add_context()
                    allowedTypes = _allowedTypes(self.request, addContext)
                    for item in allowedTypes:
                        item_id = item.getId()
                        if item_id == 'SurveyGenweb':
                            return True

        return False


    def selected(self):
        return False


class ConfigperiodeMenu(BrowserMenu):
    implements(IConfigperiodeMenu)

    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""
        results = []
        accio = context.absolute_url() + '/nouperiodeview'
        results.append({ 'title'       : "Afegir recull d'indicadors",
                         'description' : 'Mostra un formulari per crear i configurar un nou recull',
                         'action'      : accio,
                         'selected'    : False,
                         'icon'        : None,
                         'extra'       : {'id': 'folderDefaultPageDisplay', 'separator': 'actionSeparator', 'class': 'actionMenuSelected'},
                         'submenu'     : None,
                         })
        return results
