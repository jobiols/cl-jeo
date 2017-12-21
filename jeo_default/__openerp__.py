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
    'version': '9.0.1.0',
    'category': 'Tools',
    'summary': 'Customización Jeo Software',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Customización jeo Software
==========================
""",
    'author': 'jeo Software',
    'depends': [
        'support_branding_jeosoft',  # soporte de jeosoft y + modulos utilitarios

#        'account_voucher'  esto pone un recibo choto no me gusta
#       'account_debt_management',  #muestra la deuda del partner de varias formas pero instala account_payment_group
        # para instalar esto tuve que borrar esto SELECT * FROM mail_followers where partner_id = 3 and res_model ='account.payment.group'
        # l10n_ar_aeroo_payment_group este tiene el reporte de recibos pero se instala con el account_payment_group
        # estos tres rompen los pagos
#        account_payment_group deberia poderse instalas solo pero mete todo esto
#report_extended_payment_group : to install
#account_financial_amount : to install
#account_payment_group : to install
#account_payment_group_document : to install
#        report_extended_payment_group
#        account_payment_group_document
        # utilidades
#        'server_mode',              # habilitar uso de parametro server_mode = "some value" en config.
#        'disable_odoo_online',  # elimina referencias a odoo online
#        'res_config_settings_enterprise_remove',  # This module removes enterprise-only features

        # aplicaciones
#        'sale',
#        'l10n_ar_afipws_fe_cancel', # cancela factura electronica???
#        'l10n_ar_account_vat_ledger',  # Creates Sale and Purchase VAT report menus
#        'l10n_ar_account_vat_ledger_citi',  # Argentinian CITI Reportsto comply with RG3685
#        'l10n_ar_account_withholding',  # Automatic Argentinian Withholdings on Payments
#        'account_payment_group',  #  Account Payment with Multiple methods !!!!! esto rompe los pagos de cliente !!!!!
#        'l10n_ar_aeroo_payment_group',  #
#        'l10n_ar_bank',  # Listado de bancos argentinos
#        'account_cancel',  # Este módulo añade el campo 'Permitir cancelar asientos'
#        'account_clean_cancelled_invoice_number',  # permite cancelar una factura
#        'account_transfer_unreconcile',  #Unreconcile Moves on Transfer cancellation
        #'report_custom_filename',  # This addon allows for custom filenames for reports.


        # instalacion de aplicaciones

        'sale', 'l10n_ar_aeroo_sale',           # ventas
        'account_accountant',                   # permisos para contabilidad
        'web_export_view',                      # reportes de vistas en excel

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
