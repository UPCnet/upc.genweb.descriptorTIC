from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _

class IIndicadorsunitatView(Interface):
    """ Indicadorsunitat view interface
    """

    def test():
        """ test method"""


class IndicadorsunitatView(BrowserView):
    """ Indicadorsunitat browser view
    """
    __call__ = ViewPageTemplateFile('indicadorsunitatview.pt')

    implements(IIndicadorsunitatView)

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


    def retUsuari(self, periode):
        """ retorna l'usuari de la unitat que ha respost el periode
        """
        questions = periode.getAllQuestionsInOrder()
        for user in periode.getRespondents():
            for question in questions:
                answer = ""
                if question.getInputType() in ['text', 'area'] and question.getId() == 'indica-la-teva-unitat':
                    if question.getAnswerFor(user):
                        answer = question.getAnswerFor(user)
                        if answer.lower() == self.context.getId().lower():
                            return user
                        else:
                            return False
        return False
                    

    def getDadesPeriode(self, user, periode):
        """ retorna llistat amb les dades del periode:
            [
                [
                    'dsf', 
                    [
                        ['Indica la teva unitat', 'FIB'], 
                        ['N\xc3\xbamero de PC a aules inform\xc3\xa0tiques', '5'], 
                        ...
                    ]
                ], 
                [
                    'estiu 2010', 
                    [
                        ['Indica la teva unitat', 'FIB'], 
                        ['N\xc3\xbamero de PC a aules inform\xc3\xa0tiques', '5'], 
                        ...
                    ]
                ]
            ] 


        """
        llistat = []
        llistat.append(periode.Title())
        llistat_preg = []
        questions = periode.getAllQuestionsInOrder()
        for question in questions:
            answer = question.getAnswerFor(user)
            llistat_preg.append([question.Title(), answer])
        llistat.append(llistat_preg)
        return llistat
    

    def retIndicadorsPeriode(self):
        """ retorna una llista amb les dades dels periodes que ha contestat la unitat
        """
        id_periode = self.context.REQUEST.get('periode')
        context = self.context
        periodes = context.portal_catalog.searchResults(portal_type='Periode', id = id_periode)
        resp = None
        for p in periodes:
            obj = p.getObject()
            user = self.retUsuari(obj)
            resp = self.getDadesPeriode(user, obj)
        return resp








