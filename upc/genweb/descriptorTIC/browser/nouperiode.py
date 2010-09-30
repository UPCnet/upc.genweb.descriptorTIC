from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _
from Products.CMFCore.utils import getToolByName
from string import join

class INouperiodeView(Interface):
    """ Nouperiode view interface
    """

    def test():
        """ test method
        """


class NouperiodeView(BrowserView):
    """ Nouperiode browser view
    """

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
        """ test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}

    def retPeriodeExemple(self):
        """
        """
        try:
            portal_types = getToolByName(self.context, 'portal_types')
            carpeta_unitats = getattr(portal_types, 'unitats')
            carpeta_base = getattr(carpeta_unitats, 'osi')                               #carpeta on guardem periode exemple
            periode_exemple = getattr(carpeta_base, 'periode-dexemple')
            return periode_exemple
        except:
            context.plone_utils.addPortalMessage(_(u"El període d'exemple ha estat modificat, eliminat o mogut. Siusplau, assegura't que el període d'exemple existeix i està a la carpeta 'configuracio-periodes' de l'arrel del portal i el seu id és 'periode-dexemple'"), 'error')
            return



    def retPreguntes(self):
        """
        """
        context = self.context
        periode_exemple = self.retPeriodeExemple()
        url = join(periode_exemple.getPhysicalPath(), '/')
        preguntas = context.portal_catalog.searchResults(path=url, portal_type='SurveyTextQuestionGenweb', sort_on='getObjPositionInParent')
        return preguntas

