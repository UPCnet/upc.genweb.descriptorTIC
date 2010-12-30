from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _
from Acquisition import aq_inner, aq_parent

from DateTime import DateTime

class IPeticionscreadesView(Interface):
    """ Peticionscreades view interface
    """

    def test():
        """ test method"""


class PeticionscreadesView(BrowserView):
    """ Peticionscreades browser view
    """
    __call__ = ViewPageTemplateFile('peticionscreadesview.pt')

    implements(IPeticionscreadesView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """ test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}

    def retPeticionsCreades(self):
        """ Retorna el SurveyGenweb creats a la carpeta actual
        """
        context = self.context
        path = '/'.join(context.getPhysicalPath())
        peticions = context.portal_catalog.searchResults(portal_type='SurveyGenweb', path={'query':path, 'depth':1}, sort_on='modified', sort_order='reverse')
        resultat = []
        for peticio in peticions:
            peticio_obj = peticio.getObject()
            workflowTool = getToolByName(self.portal, "portal_workflow")
            status = workflowTool.getStatusOf("genweb_simple", peticio_obj)
            data = DateTime(peticio_obj.modification_date).strftime('%d/%m/%Y');
            dades_peticio = {'titol':peticio_obj.title, 'url':peticio_obj.absolute_url(), 'estat':status['review_state'], 'data_creacio':data}
            resultat.append(dades_peticio)
        return resultat
