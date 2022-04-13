from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = ["account.analytic.line"]

    start_time = fields.Float(
        string='Fecha De Inicio',
        required=False)
    end_time = fields.Float(
        string='Fecha Fin',
        required=False)
    unit_amount = fields.Float(compute='_calculate_duration')

    @api.onchange("end_time")
    def _calculate_duration(self):
        for rec in self:
            rec.unit_amount = rec.end_time - rec.start_time
