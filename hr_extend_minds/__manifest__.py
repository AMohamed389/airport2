{
    'name': 'HR_EXTEND_MINDS',
    'description': 'HR_EXTEND_MINDS',
    'author': 'Minds Solutions',
    'depends': ['base','hr','documents'],
    'application': True,
    'data': [

    'views/ir_actions_act_window.xml',
    'views/ir_ui_view.xml',
    'views/ir_ui_menu.xml',
    'security/hr_extend_access.xml',
    'security/ir.model.access.csv',
    'report/report_employment_status.xml',
    'data/job_degree.xml',
    'data/document_folder.xml',

        ],
    'installable':True,
    'application':True
}
