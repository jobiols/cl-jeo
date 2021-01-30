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
    'version': '11.0.0.0',
    'category': 'Tools',
    'summary': 'Customización Jeo Software',
    'author': 'jeo Software',
    'depends': [
        'crm',
        'sale_management',
        'web_decimal_numpad_dot',

        # localizacion
        'standard_depends_ee',

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],


    # manifest version, if omitted it is backward compatible but
    # oe will show a deprecation warning
    'env-ver': '2',

    # Configuration data for odoo.conf
    'config': [
        'workers = 2'
    ],

    # Default to CE, can be ommited
    'odoo-license': 'EE',

    'port': '8069',
    'git-repos': [
        'https://github.com/jobiols/cl-jeo.git',
        'https://github.com/jobiols/odoo-addons.git',
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/product.git',
        'https://github.com/ingadhoc/miscellaneous.git',
        'https://github.com/ingadhoc/argentina-reporting.git',
        'https://github.com/ingadhoc/reporting-engine.git',
        'https://github.com/ingadhoc/reporting-engine.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/partner.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/stock.git',

        'https://github.com/oca/server-ux.git',
        'https://github.com/oca/partner-contact.git',
        'https://github.com/oca/web.git',
        'https://github.com/oca/server-tools.git',
        'https://github.com/oca/social.git',
        'https://github.com/oca/sale-workflow.git',
        'https://github.com/oca/contract.git',

        'https://github.com/it-projects-llc/mail-addons.git',

    ],
    'docker-images': [
        'odoo jobiols/odoo-ent:11.0e',
        'postgres postgres:10.1-alpine',
        'aeroo adhoc/aeroo-docs'
    ]

}
