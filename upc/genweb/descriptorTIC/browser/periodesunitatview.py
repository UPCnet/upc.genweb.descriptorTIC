from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _
from upc.genweb.descriptorTIC.interfaces import IUnitatTIC

from Acquisition import aq_inner, aq_parent

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

    def retUnitat(self):
        """ retorna la unitat
        """
        context = aq_inner(self.context)
        unitat = aq_parent(context)
        if IUnitatTIC.providedBy(unitat):
            return unitat
        else:
            return False
        
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
                        unitat = self.retUnitat()
                        if unitat:
                            if answer.lower() == unitat.getId().lower():
                                return True
                            else:
                                return False
        return False


    def retPeriodesTancats(self):
        """ retorna una llista amb els periodes que ha contestat la unitat
        """
        resultats = []
        context = self.context
        periodes = context.portal_catalog.searchResults(portal_type='SurveyGenweb', review_state='published', sort_on='created', sort_order='reverse', Language=['ca', 'es', 'en', ''])
        for p in periodes:
            obj = p.getObject()
            if obj.getId() != 'periode-dexemple':
                resp = self.teRespostaUnitat(obj)
                if resp != False:
                    resultats.append(obj)
                else:
                    continue
        return resultats


    def retPeriodesPendentsRevisio(self):
        """ retorna una llista amb els periodes que ha contestat la unitat
        """
        resultats = []
        context = self.context
        periodes = context.portal_catalog.searchResults(portal_type='SurveyGenweb', review_state='enproces', sort_on='created', sort_order='reverse', Language=['ca', 'es', 'en', ''])
        for p in periodes:
            obj = p.getObject()
            if obj.getId() != 'periode-dexemple':
                resp = self.teRespostaUnitat(obj)
                if resp != False:
                    resultats.append(obj)
                else:
                    continue
        return resultats


    def retPeriodesPendentsResposta(self):
        """ retorna una llista amb els periodes que ha contestat la unitat
        """
        resultats = []
        context = self.context
        periodes = context.portal_catalog.searchResults(portal_type='SurveyGenweb', review_state='enproces', sort_on='created', sort_order='reverse', Language=['ca', 'es', 'en', ''])
        for p in periodes:
            obj = p.getObject()
            if obj.getId() != 'periode-dexemple':
                resp = self.teRespostaUnitat(obj)
                if resp == False:
                    resultats.append(obj)
                else:
                    continue
        return resultats








