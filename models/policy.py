from odoo import api, fields, models

class CompanyPolicy(models.Model):
    _name = 'company.policy'
    _description = 'Company Policies'

    name = fields.Char(
        string='Título de la Política',
        required=True,
        help='Nombre o título de la política'
    )
    category = fields.Char(
        string='Categoría',
        help='Categoría o etiqueta de la política (ej: Seguridad, Interna, etc.)'
    )
    is_confidential = fields.Boolean(
        string='Confidencial',
        help='Indica si la política es confidencial o pública'
    )
    version = fields.Integer(
        string='Versión',
        default=1,
        help='Número de versión de la política'
    )
    description = fields.Text(
        string='Descripción',
        help='Resumen o explicación de la política'
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
