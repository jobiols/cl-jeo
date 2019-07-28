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
{
    'name': 'jeo Software',
    'version': '12.0e.0.0',
    'category': 'Tools',
    'summary': 'Customización Jeo Software',
    'author': 'jeo Software',
    'depends': [
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-jeo', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '12.0'},

        {'usr': 'jobiols', 'repo': 'adhoc-odoo-argentina', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-sale', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-sale', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
         'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
         'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-partner', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-partner-contact', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-web', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-tools', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-social', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-sale-workflow', 'branch': '12.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '12.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '10.1-alpine'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},

    ]

}

