from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _

class INouperiodeView(Interface):
    """
    Nouperiode view interface
    """

    def test():
        """ test method"""


class NouperiodeView(BrowserView):
    """
    Nouperiode browser view
    """
    __call__ = ViewPageTemplateFile('nouperiodeview.pt')

    implements(INouperiodeView)

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

    def retPeriodeExemple(self):
        """
        """
        context = self.context
        portal_types = getToolByName(context, 'portal_types')
        #try:
        carpeta_base = getattr(portal_types, 'configuracio-periodes')                #carpeta on tenim base
        periode_exemple = carpeta_base.getattr(portal_types, 'periode-dexemple')
        #except:
        #    context.plone_utils.addPortalMessage(_(u"El període d'exemple ha estat modificat, eliminat o mogut. Siusplau, assegura't que el període d'exemple existeix i està a la carpeta 'configuracio-periodes' de l'arrel del portal i el seu id és 'periode-dexemple'"), 'error')
        #    return
        return periode_exemple

    def retIndicadorsExemple(self):
        """
        """
