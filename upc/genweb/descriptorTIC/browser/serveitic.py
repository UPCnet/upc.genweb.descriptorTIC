from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component import getMultiAdapter, getUtility
from Products.CMFCore.utils import getToolByName
from upc.genweb.descriptorTIC.interfaces import IServeiTIC

from plone.memoize.instance import memoize

class ServeiTICView(BrowserView):
    """Default view of a fitxa
    """

    # This template will be used to render the view. An implicit variable
    # 'view' will be available in this template, referring to an instance
    # of this class. The variable 'context' will refer to the cinema folder
    # being rendered.

    __call__ = ViewPageTemplateFile('serveiTIC-view.pt')

    def getTICFamily(self):
        tools = getMultiAdapter((self.context, self.request),name=u'plone_context_state')
        return tools.parent().title

    def getTICUnitat(self):
        tools = getMultiAdapter((self.context, self.request),name=u'plone_context_state')
        return tools.parent().getParentNode().title

    def eliminaUltimo(self, cad):
        new_cad = []
        lon = len(cad)
        for ii in cad[:len(cad)-1]:
            new_cad.append(ii)
        return new_cad


# Buscador de servicios por categoria
class cercaServeis(BrowserView):
    __call__ = ViewPageTemplateFile('cerca-serveis.pt')


class searchServeis(BrowserView):
    __call__ = ViewPageTemplateFile('searching_serveis.pt')

# Buscador de servicios por familia
class cercaFamilias(BrowserView):
    __call__ = ViewPageTemplateFile('cerca-familias.pt')


class searchfamilias(BrowserView):
    __call__ = ViewPageTemplateFile('searching_familias.pt')

