from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalDoctors(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread"]
    _description = "Doctor Records"
    _rec_name = 'reference'

    name = fields.Char(String='Name', required=True, tracking=True)
    reference = fields.Char(String='Reference', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], String='Gender', tracking=True)

    active = fields.Boolean(default=True)

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.reference} - {rec.name}'
            res.append((rec.id, name))
        return res



