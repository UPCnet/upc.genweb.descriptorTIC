from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _

class IPeriodesunitatView(Interface):
    """ Periodesunitat view interface
    """

    def test():
        """ test method"""


class PeriodesunitatView(BrowserView):
    """ Periodesunitat browser view
    """
    __call__ = ViewPageTemplateFile('periodesunitatview.pt')

    implements(IPeriodesunitatView)

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


    def teRespostaUnitat(self, periode):
        """ retorna True si la pregunta 'indica la teva unitat' conte la unitat on estem
        """
        questions = periode.getAllQuestionsInOrder()
        for user in periode.getRespondents():
            for question in questions:
                answer = ""
                if question.getInputType() in ['text', 'area'] and question.getId() == 'indica-la-teva-unitat':
                    if question.getAnswerFor(user):
                        answer = question.getAnswerFor(user)
                        if answer.lower() == self.context.getId().lower():
                            return True
                        else:
                            return False
        return False


    def retPeriodesUnitat(self):
        """ retorna una llista amb els periodes que ha contestat la unitat
        """
        resultats = []
        context = self.context
        periodes = context.portal_catalog.searchResults(portal_type='Periode', sort_on='created', sort_order='reverse')
        for p in periodes:
            obj = p.getObject()
            resp = self.teRespostaUnitat(obj)
            if resp != False:
                resultats.append(obj)
            else:
                continue
        return resultats








