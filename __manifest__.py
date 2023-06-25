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

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],
    'license': 'AGPL-3',
    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/optometry.xml',
        'views/optometrist.xml',
        'views/shop.xml',
        'report/optometry_order_template.xml',
        'report/report.xml',
        
        # 'views/templates.xml',
    ],
    'assets': {},
    # only loaded in demonstration mode
    'qweb': [],
    'demo': [
        'demo/demo.xml',
    ],
}
