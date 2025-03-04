from odoo import api, fields, models

class CompanyPolicyCategory(models.Model):
    _name = 'company.policy.category'
    _description = 'Categorías de Políticas (con jerarquía)'

    name = fields.Char(
        string='Nombre de la Categoría',
        required=True
    )
    parent_id = fields.Many2one(
        'company.policy.category',
        string='Categoría Padre',
        ondelete='restrict'
    )
    child_ids = fields.One2many(
        'company.policy.category',
        'parent_id',
        string='Subcategorías'
    )

    # Campo calculado para ver la jerarquía completa en nombre
    complete_name = fields.Char(
        'Nombre Completo',
        compute='_compute_complete_name',
        store=True
    )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        """
        Construye un nombre con la jerarquía: 
        Ejemplo: RECURSOS HUMANOS / Seguridad / Externa
        """
        for record in self:
            if record.parent_id:
                record.complete_name = f"{record.parent_id.complete_name} / {record.name}"
            else:
                record.complete_name = record.name
