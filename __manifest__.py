# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Hospital Management",
    'version': '16.0.1.0.0',
    'summary': 'Hospital Management Software',
    'author': 'Ramiz Belim',
    'sequence': 10,
    'description': """
Patient & Records """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['sale_management', 'mail'],
    'data': [
        # 'security/account_security.xml',
        'security/ir.model.access.csv',
        'wizard/sale_order_wizard_views.xml',
        'views/sale_order_history_views.xml',
        'views/contact_views.xml',
        'views/hospital_department_views.xml',
        'views/hospital_views.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'views/res_config_settings_views.xml',
        'views/product_product_views.xml',
        'views/menu.xml'
    ],
    'demo': [
        # 'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
