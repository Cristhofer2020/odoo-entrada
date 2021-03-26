from odoo import api, fields, models


class HelpdeskTickets(models.Model):
    _inherit = ["helpdesk.ticket"]

    start_time = fields.Float(
        string='start_time',
        required=False)
    end_time = fields.Float(
        string='End_time',
        required=False)
    unit_amount = fields.Float(compute='_calculate_duration')

    def _calculate_duration(self):
        for rec in self:
            rec.unit_amount = rec.emd_time - rec.start_time

