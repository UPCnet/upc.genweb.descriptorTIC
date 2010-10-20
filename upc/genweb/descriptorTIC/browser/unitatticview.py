from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _

from string import join

class IUnitatticView(Interface):
    """
    UnitatticView view interface
    """

    def test():
        """ test method"""


class UnitatticView(BrowserView):
    """
    UnitatticView browser view
    """
    implements(IUnitatticView)

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
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}

    def getDocumentPrincipal(self):
        context = self.context
        path = join(context.getPhysicalPath(), '/')
        resultats = self.portal_catalog.searchResults(portal_type='Document',
                                                      path={'query':path, 'depth':1},
                                                      sort_on='getObjPositionInParent')[:1]
        for brain in resultats:
            obj = brain.getObject()
            cap_transicio = False
            dades_obj = {'titol':obj.Title(),
                         'descripcio':obj.Description(),
                         'url':obj.absolute_url()}
            return dades_obj
        return None

    def getSubcarpetes(self):
        context = self.context
        path = join(context.getPhysicalPath(), '/')
        subcarpetes = []
        resultats = self.portal_catalog.searchResults(portal_type=['FamiliaTIC','FaqContainertic'],
                                                      path={'query':path, 'depth':1},
                                                      sort_on='getObjPositionInParent')
        for brain in resultats:
            obj = brain.getObject()
            imatge = None
            path = join(obj.getPhysicalPath(), '/')
            icono = self.portal_catalog.searchResults(portal_type='Image',
                                                      path={'query':path, 'depth':1},
                                                      id='icono')[:1]
            for i in icono:
                i_obj = i.getObject()
                imatge = i_obj.absolute_url() + '/image'
            desc = obj.Description()[:110]
            if len(obj.Description())>110:
                desc = desc + '...'
            dades_obj = {'titol':obj.Title(),
                         'descripcio':desc,
                         'icono':imatge,
                         'url':obj.absolute_url()}
            subcarpetes.append(dades_obj)
        return subcarpetes
