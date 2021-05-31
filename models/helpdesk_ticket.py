from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = ["account.analytic.line"]

    start_time = fields.Float(
        string='start_time',
        required=False)
    end_time = fields.Float(
        string='End_time',
        required=False)
    unit_amount = fields.Float(compute='_calculate_duration')

    def _calculate_duration(self):
        for rec in self:
            rec.unit_amount = rec.end_time - rec.start_time
