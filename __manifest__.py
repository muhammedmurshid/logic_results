{
    'name': "Logic Results",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['mail', 'base', 'logic_base'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/results_form.xml',
        'views/web_form_results.xml',
        'views/result_link.xml',

    ],
    'demo': [],
    'summary': "logic_exam_results",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}
