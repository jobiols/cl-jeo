# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2017  jeo Software  (http://www.jeosoft.com.ar)
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
    'name': 'Power Oils',
    'version': '8.0.1.0',
    'category': 'Tools',
    'summary': 'Customización Power Oils',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Customización Power Oils
========================
""",
    'author': 'jeo Software',
    'depends': [
        'l10n_ar_base',  # modulo base para localización argentina
        'base_vat_unique',  # evita que duplique cuit
        # 'base_vat_unique_parent',  # evita que duplique cuit en multicompañia
        'disable_openerp_online',  # elimina referencias a odoo online
        'account_cancel',  # Muestra el check en los diarios que permite cancelar asientos
        'sale',      # ventas
        'purchase',  # compras
        # 'product_pricelist_import',  # Importa lista de precios y carga productos
        # 'hide_product_variants',  # oculta las variantes
        # 'im_chat',  # mensajeria instantanea entre usuarios de odoo
        #        'express_checkout',         # Facturación express
        #'invoice_order_by_id',  # ordena facturas ultima arriba
        #        'sale_order_recalculate_prices',  # agrega boton para recalcular precios
        #        'consult_product_price',    # consulta de precios
        #        'partner_search',            # permite buscar partners por varios criterios
        # 'account_journal_sequence'  # agrega un campo de secuencia en el diario para elegirlos
        #'account_statement_move_import',  # agrega boton de importar aputnes en extractos bancarios
        # 'account_journal_sequence', #Adds sequence field on account journal and it is going to be considered when choosing journals in differents models.
        #        'po_custom_reports',        # dependencia requerida
        #        'custom_vat_ledger',        # dependencia requerida
        #        'odoo_argentina_fix',       # patch a la localización
        #        'account_invoice_tax_add',  # agrega insercion manual de impuestos para factura de compras
        #        'ticket_citi_fix',          # corrige citi para pv impresor fiscal
        'product_unique_default_code',  # impide que se duplique el default_code
        'hide_messaging',  # oculta el menu de mensajeria
        #'base_multi_store',  # agrega capacidad de multitienda analogo a multicompañia
        #'voucher_payment_check_fix',  # evita que aparezca cheques propios en medios de pago de cliente
        #'point_of_sale',  # Terminal punto de venta
        #'mrp',  # planificacion de producción.
        #'pos_pricelist',
        #'pos_discount',
        #'pos_order_pricelist_change',
        #'web_pdf_preview',  # vista previa de los pdf antes de imprimir
        #'account_partner_account_summary',  # Imprime el resumen de cuenta de un partner
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
