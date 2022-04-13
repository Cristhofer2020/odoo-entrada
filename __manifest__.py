# -*- coding: utf-8 -*-
{
    'name': "CAPW (Calculo de horas)",

    'summary': """
        Module for generating hours""",

    'description': """
        CAPW SOPORTE TECNICOS SRL.
    """,

    'author': "Cristhofer A. Nuñez Dominguez",
    'website': "http://www.capw.com.do",

    'category': 'Timesheet',
    'version': '13.0',


    'depends': ['base_setup', 'helpdesk', 'timesheet_grid', 'helpdesk_timesheet'],

    'data': [
        'views/helpdesk_ticket.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
