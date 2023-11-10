from odoo import api, fields, models


class HospitalPatients(models.Model):
    _name = "hospital.patient"
    _description = "Patient Records"

    name = fields.Char(String='Name', required=True)
    age = fields.Integer(String='Age')
    is_child = fields.Boolean(String='Is Child ?')
    notes = fields.Text(String='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], String='Gender')
