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
    'images': ['images/accounts.jpeg', 'images/bank_statement.jpeg', 'images/cash_register.jpeg',
               'images/chart_of_accounts.jpeg', 'images/customer_invoice.jpeg', 'images/journal_entries.jpeg'],
    'depends': ['sale_management', 'mail'],
    'data': [
        # 'security/account_security.xml',

        'security/ir.model.access.csv',
        'views/hospital_views.xml',
        'views/hospital_department_views.xml',
        'views/contact_views.xml',
        'views/sale_views.xml',
        'views/menu.xml'
    ],
    'demo': [
        # 'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
