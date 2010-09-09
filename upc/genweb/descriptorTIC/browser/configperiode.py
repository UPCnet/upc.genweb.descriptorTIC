from zope import interface, schema
from zope.formlib import form
from Products.Five.formlib import formbase
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from Products.CMFCore.utils import getToolByName

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _

class IconfigperiodeSchema(interface.Interface):
    # -*- extra stuff goes here -*-

    titol = schema.TextLine(
        title=u'Títol del període',
        description=u'Per exemple, Setembre-Octubre 2010',
        required=True,
        readonly=False,
        default=None,
        )

    descripcio = schema.TextLine(
        title=u'Descripcio del període',
        description=u'',
        required=True,
        readonly=False,
        default=None,
        )

    intro = schema.Text(
        title=u'Dates del període',
        description=u'Indica la data inicial, la data de fi i el termini del període',
        required=False,
        readonly=False,
        default=None,
        )

    camp1 = schema.Bool(
        title=u'camp1',
        description=u'Mostrar camp 1?',
        required=False,
        readonly=False,
        default=True,
        )
    camp2 = schema.Bool(
        title=u'camp2',
        description=u'Mostrar camp 2?',
        required=False,
        readonly=False,
        default=True,
        )
    camp3 = schema.Bool(
        title=u'camp3',
        description=u'Mostrar camp 3?',
        required=False,
        readonly=False,
        default=True,
        )
    camp4 = schema.Bool(
        title=u'camp4',
        description=u'Mostrar camp 4?',
        required=False,
        readonly=False,
        default=True,
        )
    camp5 = schema.Bool(
        title=u'camp5',
        description=u'Mostrar camp 5?',
        required=False,
        readonly=False,
        default=True,
        )
    camp6 = schema.Bool(
        title=u'camp6',
        description=u'Mostrar camp 6?',
        required=False,
        readonly=False,
        default=True,
        )
    camp7 = schema.Bool(
        title=u'camp7',
        description=u'Mostrar camp 7?',
        required=False,
        readonly=False,
        default=True,
        )
    camp8 = schema.Bool(
        title=u'camp8',
        description=u'Mostrar camp 8?',
        required=False,
        readonly=False,
        default=True,
        )
    camp9 = schema.Bool(
        title=u'camp9',
        description=u'Mostrar camp 9?',
        required=False,
        readonly=False,
        default=True,
        )
    camp10 = schema.Bool(
        title=u'camp10',
        description=u'Mostrar camp 10?',
        required=False,
        readonly=False,
        default=True,
        )
    camp11 = schema.Bool(
        title=u'camp11',
        description=u'Mostrar camp 11?',
        required=False,
        readonly=False,
        default=True,
        )
    camp12 = schema.Bool(
        title=u'camp12',
        description=u'Mostrar camp 12?',
        required=False,
        readonly=False,
        default=True,
        )
    camp13 = schema.Bool(
        title=u'camp13',
        description=u'Mostrar camp 13?',
        required=False,
        readonly=False,
        default=True,
        )
    camp14 = schema.Bool(
        title=u'camp14',
        description=u'Mostrar camp 14?',
        required=False,
        readonly=False,
        default=True,
        )
    camp15 = schema.Bool(
        title=u'camp15',
        description=u'Mostrar camp 15?',
        required=False,
        readonly=False,
        default=True,
        )




class configperiode(formbase.PageForm):
    form_fields = form.FormFields(IconfigperiodeSchema)
    label = _(u'Formulari de creació i configuració de períodes')
    description = _(u"Indica de quins indicadors vols recollir dades en el nou període.")

    @form.action('Submit')
    def actionSubmit(self, action, data):
        
        #1. copiar periode exemple
        context = self.context
        portal_types = getToolByName(context, 'portal_types')
        try:
            carpeta_base = getattr(portal_types, 'configuracio-periodes')                #carpeta on tenim base
            periode_copy = carpeta_base.manage_copyObjects(['periode-dexemple'])         #id objecte base
        except:
            context.plone_utils.addPortalMessage(_(u"El període d'exemple ha estat modificat, eliminat o mogut. Siusplau, assegura't que el període d'exemple existeix i està a la carpeta 'configuracio-periodes' de l'arrel del portal i el seu id és 'periode-dexemple'"), 'error')
            return

        #2. guardar nou periode
        periode_paste = context.manage_pasteObjects(periode_copy)    
        nou_id = periode_paste[0]['new_id']
        nou_periode = getattr(context, nou_id)

        #3. modifiquem dades
        nou_periode.edit(title = data['titol'],
                         description = data['descripcio'],
                         body = data['intro'],
                         exitUrl = nou_periode.absolute_url()
                         )

        #4. eliminem els subobjectes no marcats
        camps_a_eliminar = []
        for camp in data: #noms dels camps del formulari (camp = 'camp12')
            if data[camp] == False:
                camps_a_eliminar.append(camp)
        try:
            nou_periode.manage_delObjects(camps_a_eliminar)
        except:
            context.plone_utils.addPortalMessage(_(u"Alguns dels camps del període d'exemple han estat eliminats o modificat. Siusplau, assegura't que el període d'exemple conté els camps 'camp1', 'camp2' ... 'camp15'"), 'error')
            return

        context.plone_utils.addPortalMessage(_(u"El nou periode ha estat creat correctament"))
        context.REQUEST.RESPONSE.redirect(nou_periode.absolute_url())




