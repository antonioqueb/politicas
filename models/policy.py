from odoo import api, fields, models

class CompanyPolicy(models.Model):
    _name = 'company.policy'
    _description = 'Company Policies'
    # Se añaden las herencias para que este modelo soporte el chatter de Odoo
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Título de la Política',
        required=True,
        help='Nombre o título de la política',
        tracking=True  # Se habilita tracking si deseas que el nombre aparezca en las notificaciones
    )

    category_id = fields.Many2one(
        'company.policy.category',
        string='Categoría',
        help='Categoría o subcategoría de la política'
    )

    is_confidential = fields.Boolean(
        string='Confidencial',
        help='Indica si la política es confidencial o pública',
        tracking=True
    )
    version = fields.Integer(
        string='Versión',
        default=1,
        help='Número de versión de la política',
        tracking=True
    )
    description = fields.Text(
        string='Descripción',
        help='Resumen o explicación de la política',
        tracking=True
    )
    
    file = fields.Binary(
        string='Archivo PDF',
        help='Contenido del documento PDF'
    )
    filename = fields.Char(
        string='Nombre del archivo PDF',
        help='Nombre del archivo para su identificación'
    )

    authorized_user_ids = fields.Many2many(
        'res.users',
        'policy_user_rel',
        'policy_id',
        'user_id',
        string='Usuarios Autorizados',
        help='Usuarios con permiso individual para ver políticas confidenciales'
    )

    branch_id = fields.Many2one(
        'company.policy.branch',
        string='Sucursal',
        help='Sucursal donde aplica esta política'
    )

    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('review', 'En Revisión'),
            ('approved', 'Aprobada'),
            ('published', 'Publicada'),
        ],
        string='Estado',
        default='draft',
        tracking=True
    )

    @api.model
    def create(self, vals):
        """Sobrescribir create para manejar versionado u otras lógicas personalizadas."""
        return super(CompanyPolicy, self).create(vals)

    def write(self, vals):
        """
        Si se sube un nuevo PDF o se modifican campos relevantes,
        se incrementa el número de versión.
        """
        if 'file' in vals or 'description' in vals or 'name' in vals:
            vals['version'] = self.version + 1
        return super(CompanyPolicy, self).write(vals)

    def action_review(self):
        self.write({'state': 'review'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_publish(self):
        self.write({'state': 'published'})
