# -*- coding: utf-8 -*-
{
    'name': "Fish Farm Manager 2",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description':
        "Fish Farm Manager is a module dedicated to help in managing processes on fish farming enterprises and its installations",

    'author': "Emilio Jose Roldan Olivares",
    'website': "https://github.com/Blaucel",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/farm_views.xml',
        'views/pool_views.xml',
        'views/fish_views.xml',
        'views/fish_manager_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
