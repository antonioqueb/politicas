from odoo import api, fields, models

class CompanyPolicy(models.Model):
    _name = 'company.policy'
    _description = 'Company Policies'
    _inherit = ['mail.thread']  # Opcional si deseas integrar seguimiento y mensajería de Odoo

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
    attachment_id = fields.Many2one(
        'ir.attachment',
        string='Archivo PDF',
        help='Archivo PDF que contiene el documento de la política'
    )
    # Relación con los usuarios a los que se les concede acceso directamente
    authorized_user_ids = fields.Many2many(
        'res.users',
        'policy_user_rel',
        'policy_id',
        'user_id',
        string='Usuarios Autorizados',
        help='Usuarios con permiso individual para ver políticas confidenciales'
    )
    # Estado para manejar flujo de aprobación (opcional)
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
        Ejemplo: si se sube un nuevo PDF o se modifican campos relevantes,
        podríamos incrementar el número de versión.
        """
        if 'attachment_id' in vals or 'description' in vals or 'name' in vals:
            vals['version'] = self.version + 1
        return super(CompanyPolicy, self).write(vals)

    def action_review(self):
        self.write({'state': 'review'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_publish(self):
        self.write({'state': 'published'})
