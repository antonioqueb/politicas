{
    'name': 'politicas',
    'version': '1.0.0',
    'summary': 'Gestión de políticas públicas y confidenciales de la empresa',
    'description': """
Módulo para gestionar documentos PDF de políticas empresariales con control 
de confidencialidad, asignación de usuarios, historial de versiones y más.
    """,
    'author': 'Alphaqueb Consulting SAS',
    'website': 'https://alphaqueb.com',
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/policy_security.xml',
        'security/ir.model.access.csv',
        'views/policy_views.xml',
        'views/policy_menus.xml',
        'views/policy_category_views.xml',
        'views/policy_branch_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
