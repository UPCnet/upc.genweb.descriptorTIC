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
        user = self.context.REQUEST.get('user')
        context = self.context
        periodes = context.portal_catalog.searchResults(portal_type='Periode', id = id_periode)
        for p in periodes:
            obj = p.getObject()
            resp = self.getDadesPeriode(obj, user)
        return resp








