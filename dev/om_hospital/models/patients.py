from odoo import api, fields, models


class HospitalPatients(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread"]
    _description = "Patient Records"

    name = fields.Char(String='Name', required=True, tracking=True)
    age = fields.Integer(String='Age', tracking=True)
    is_child = fields.Boolean(String='Is Child ?', tracking=True)
    notes = fields.Text(String='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], String='Gender', tracking=True)

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
