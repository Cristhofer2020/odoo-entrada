# -*- coding: utf-8 -*-
{
    'name': "Entrada y Salida",

    'summary': """
        Module for generating hours""",

    'description': """
        CAPW SOPORTE TECNICOS SRL.
    """,

    'author': "Cristhofer A. Nuñez Dominguez",
    'website': "http://www.capw.com.do",

    'category': 'Timesheet',
    'version': '1.0',


    'depends': ['base_setup', 'board', 'helpdesk', 'account', 'timesheet_grid', 'helpdesk_timesheet'],

    'data': [
        'views/helpdesk_ticket.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
