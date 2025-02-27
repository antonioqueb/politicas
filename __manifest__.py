{
    'name': 'Políticas',
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
    ],
    'data': [
        'security/policy_security.xml',
        'security/ir.model.access.csv',
        'views/policy_views.xml',
        'views/policy_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
