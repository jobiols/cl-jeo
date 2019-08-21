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
    'version': '11.0e.0.0',
    'category': 'Tools',
    'summary': 'Customización Jeo Software',
    'author': 'jeo Software',
    'depends': [
        'crm',
        'sale_management',

        # localizacion
        'standard_depends_ee',
        'base_currency_inverse_rate',
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
        {'usr': 'jobiols', 'repo': 'cl-jeo', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},

        {'usr': 'jobiols', 'repo': 'adhoc-enterprise-extensions', 'branch': '11.0'},

        {'usr': 'jobiols', 'repo': 'adhoc-odoo-argentina', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-sale', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-sale', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
         'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
         'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-partner', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-partner-contact', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-web', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-tools', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-social', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-sale-workflow', 'branch': '11.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '11.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '10.1-alpine'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},

    ]

}

