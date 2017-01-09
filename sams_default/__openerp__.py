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
    'name': 'sams',
    'version': '8.0.1.0',
    'category': 'Tools',
    'summary': 'Customización Jeo Software',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Customización Sams
==================
""",
    'author': 'Sams',
    'depends': [
        'l10n_ar_base',  # modulo base para localización argentina
        'disable_odoo_online',  # elimina referencias a odoo online
        'res_config_settings_enterprise_remove', # This module removes enterprise-only features
        'l10n_ar_account', #  Tiene toda la lógica de impuestos y tipos de documentos de la afip
        'account_accountant', # Da al usuario administrador acceso a todas las características de contabilidad
        'l10n_ar_afipws_fe', # Factura Electrónica Argentina
        'l10n_ar_account_vat_ledger_citi', # Argentinian CITI Reports
        'l10n_ar_bank', # Listado de bancos argentinos
        'account_cancel', # Este módulo añade el campo 'Permitir cancelar asientos'
        'l10n_ar_padron_afip', # Modulo para consulta y actualizacion desde padron AFIP
        'l10n_ar_account_withholding', # Automatic Argentinian Withholdings on Payments

        'sale', # Gestión de ventas



        # 'base_vat_unique',  # evita que duplique cuit
        # 'base_vat_unique_parent',  # evita que duplique cuit en multicompañia
        # 'invoice_order_by_id',  # ordena facturas ultima arriba
        # 'mass_mailing_partner'  # agrega menu para mandar un partner a la mailing list
        # 'account_invoice_tax_wizard',  # agrega menu add_taxes para cargar percepciones
        # 'sale_order_recalculate_prices',  # agrega boton para recalcular precios
        # 'account_journal_sequence'         # agrega un campo de secuencia en el diario para elegirlos
        # 'account_statement_move_import'    # agrega boton de importar aputnes en extractos bancarios
        # 'account_invoice_tax_wizard'       # agrega boton add_taxes para cargar percepciones
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
