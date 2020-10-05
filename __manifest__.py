# -*- coding: utf-8 -*-

{
    'name': 'Mining Production',
    'version': '1.0',
    'author': 'Technoindo.com',
    'category': 'Mining',
    'depends': [
        # 'shipping',
        # 'mining_qaqc',
        'fleet',
        'stock',
        'account',
        'stock_account',
    ],
    'data': [
        "views/stock_warehouse_views.xml",
        "views/stock_move_views.xml",
        'views/menu.xml',
        "views/mining_production_config.xml",
        "views/production_operation_template.xml",
        "views/ritase_order.xml",
        "views/dumptruck_activity.xml",
        "views/stock_views.xml",
        "views/hourmeter_order.xml",
        "views/cost_code.xml",
        "views/production_block.xml",
        "views/production_losstime.xml",
        "views/production_pit.xml",
        "views/production_order.xml",
        "views/procurement_views.xml",
        "views/hourmeter_log.xml",
        "views/production_cop_adjust.xml",
        "views/fleet_service_type.xml",
        "views/fleet.xml",
        "views/production_cop_tag_log.xml",
        "views/production_cop_tag.xml",

        "data/production_data.xml",

        "security/security.xml",
        "security/ir.model.access.csv",
    ],
    'qweb': [
        # 'static/src/xml/cashback_templates.xml',
    ],
    'demo': [
        # 'demo/sale_agent_demo.xml',
    ],
    "installable": True,
	"auto_instal": False,
	"application": True,
}
