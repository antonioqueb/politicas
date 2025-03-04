from odoo import fields, models

class CompanyPolicyBranch(models.Model):
    _name = 'company.policy.branch'
    _description = 'Sucursales para Políticas'

    name = fields.Char(
        string='Sucursal',
        required=True
    )
    description = fields.Text(
        string='Descripción'
    )
