# -*- coding: utf-8 -*-
{
    'name': "Entrada y Salida",

    'summary': """
        Module for generating hours""",

    'description': """
        TEST.
    """,

    'author': "Cristhofer Nuñez",
    'website': "http://www.capw.com.do",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base_setup', 'board', 'helpdesk', 'account', 'timesheet_grid', 'helpdesk_timesheet'],

    # always loaded
    'data': [
        'views/helpdesk_ticket.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
