#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType
from datetime import datetime, date, time
import tempfile
import csv

class writeCSV(BrowserView):

    def __call__(self):
        data = self.context.portal_catalog.searchResults(portal_type='Folder', path = dict(query=self.context.absolute_url_path()+'/unitats', depth=1))
        file_name = 'csv_data_' + '_'.join(datetime.now().strftime("%d %B %Y").split(' ')) + '.csv'
        res = ['Carpeta','Unitat','Familia','Serveis','Colectius']
        dataWriter = csv.writer(open('/tmp/'+file_name, 'w'), delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dataWriter.writerow(res)
        for folder in data:
            unitat_data = self.context.portal_catalog.searchResults(portal_type='UnitatTIC',path=folder.getPath())
            for unitat in unitat_data:
                familia_data = self.context.portal_catalog.searchResults(portal_type='FamiliaTIC',path=unitat.getPath())
                for familia in familia_data:
                    servei_data = self.context.portal_catalog.searchResults(portal_type='ServeiTIC',path=familia.getPath()) 
                    for servei in servei_data:
                        tmp = []
                        servei_title = servei.Title
                        servei_colectiu = ' '.join(servei.getColectiu)
                        tmp.append(folder.Title)
                        tmp.append(unitat.Title)
                        tmp.append(familia.Title)
                        tmp.append(servei_title)
                        tmp.append(servei_colectiu)               
                        dataWriter.writerow(tmp)
        portal = getToolByName(self,'portal_url').getPortalObject()
        acomulat = portal['indicadors']
        fichero_csv = self.crearObjecte(acomulat,'fichero_csv','File',file_name,'')
        f = open('/tmp/'+file_name, 'r+')
        fichero_csv.setFile(f.read())
        fichero_csv.setFilename(file_name)
        fichero_csv.reindexObject()
        f.close()
        return ''

    def crearObjecte(self,context,id,type_name,title,description,exclude=True,constrains=None):
        pt = getToolByName(context,'portal_types')
        if not getattr(context,id,False) and type_name in pt.listTypeTitles().keys():
            #creem l'objecte i el publiquem
            _createObjectByType(type_name, context, id)
        #populem l'objecte
        created = context[id]
        created.setTitle(title)
        created.setDescription(description)
        created._at_creation_flag=False
        created.setExcludeFromNav(exclude)
        if constrains:
            created.setConstrainTypesMode(1)
            created.setLocallyAllowedTypes(tuple(constrains[0]+constrains[1]))
            created.setImmediatelyAddableTypes(tuple(constrains[0]))

        created.reindexObject()
        return created


