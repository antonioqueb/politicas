from odoo import api, fields, models

class CompanyPolicyCategory(models.Model):
    _name = 'company.policy.category'
    _description = 'Categorías de Políticas (con jerarquía)'
    _parent_name = 'parent_id'
    _parent_store = True
    _order = 'parent_left'

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

    # Campos auxiliares para guardar la jerarquía
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)

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

    def name_get(self):
        """
        Para que en los Many2one se muestre la ruta completa, 
        en lugar de solo el nombre de la subcategoría.
        """
        result = []
        for record in self:
            result.append((record.id, record.complete_name))
        return result
