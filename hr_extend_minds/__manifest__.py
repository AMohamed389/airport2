{
    'name': 'HR_EXTEND_MINDS',
    'description': 'HR_EXTEND_MINDS',
    'author': 'Minds Solutions',
    'depends': ['base','hr'],
    'application': True,
    'data': [

    'views/ir_actions_act_window.xml',
    'views/ir_ui_view.xml',
    'views/ir_ui_menu.xml',
    'security/hr_extend_access.xml',
    'security/ir.model.access.csv',
    'report/report_employment_status.xml',

        ],
    'installable':True,
    'application':True
}
