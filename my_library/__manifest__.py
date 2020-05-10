# -*- coding: utf-8 -*-
{
    'name': "My Library",

    'summary': """My Library module will assist to manage books easily.""",

    'description': """
        The purpose of the My Library module is to assist in managing book in the easiest way.
    """,

    'author': "Numan Ibn Mazid",
    'website': "http://www.facebook.com/numanibnmazid",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    # 'data': [
    #     # 'security/ir.model.access.csv',
    #     # 'views/views.xml',
    #     # 'views/templates.xml',
    # ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'data/data.xml',
        'views/library_book_rent.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
