# -*- coding: utf-8 -*-
{
    'name': "optometry",
    'summary': """
        偉太科技驗光單作業""",
    'description': """
        偉太科技驗光單作業
    """,
    'author': "偉太科技",
    'website': "http://www.webtai.cc",
    'category': 'tools',
    'version': '15.0',
    'depends': ['base','contacts'],
    'license': 'AGPL-3',
     'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/optometry.xml',
        'views/optometrist.xml',
        'views/shop.xml',
        'report/optometry_order_template.xml',
        'report/report.xml',
    ],
    'assets': {},
    'qweb': [],
    'demo': [
     ],
}
