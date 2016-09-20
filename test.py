# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
from xml.dom import minidom

tst_repo = {'name': 'jeo', 'port': '8000', 'odoover': '8.0',
       'repos': [
           {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'adhoc-crm', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'adhoc-partner', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'serviciosbaeza-odoo-addons', 'branch': '8.0'},
           {'usr': 'jobiols', 'repo': 'crm', 'branch': '8.0'},
       ],
       'images': [
           {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
           {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
           {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
           {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
       ]
       }

def read_xml_client(filename):
    """ Lee un archivo xml con la definicion del cliente y devuelve un diccionario
    :param filename: Archivo xml a leer
    :return: diccionario con loa datos
    """
    def get_tag(tag, il):
        """ devuelve el dato que hay en un nodo dado el tag
        """
        node = il.getElementsByTagName(tag)[0]
        return node.firstChild.data

    def get_list(tag, il):
        """ Devuelve un diccionario con lo que hay en un nodo dado el tag
        """
        list = []
        nodes = il.getElementsByTagName(tag)
        for node in nodes:
            dict = {}
            for r in node.childNodes:
                if r.nodeType == r.ELEMENT_NODE:
                    dict[r.tagName] = r.firstChild.data
            list.append(dict)
        return list

    ret = {}
    itemllist = minidom.parse('example.xml')
    ret['name'] = get_tag('name', itemllist)
    ret['port'] = get_tag('port', itemllist)
    ret['odoover'] = get_tag('odoover', itemllist)
    ret['repos'] = get_list('repo', itemllist)
    ret['images'] = get_list('image', itemllist)

    return ret

ret = read_xml_client('example.xml')

if ret['name'] != 'jeo': print 'error'
if ret['port'] != '8000': print 'error'
if ret['odoover'] != '8.0': print 'error'
rep = img = 0
for repo in ret['repos']:
    if chck_repo(repo): rep += 1
for repo in ret['repos']:
    if not chck_image(repo): img += 1


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
