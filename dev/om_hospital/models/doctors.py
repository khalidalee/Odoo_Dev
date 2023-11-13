from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


import re

class HospitalDoctors(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread"]
    _description = "Doctor Records"
    _rec_name = 'reference'

    name = fields.Char(String='Name', required=True, tracking=True)
    reference = fields.Char(String='Reference', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], String='Gender', tracking=True)
    email = fields.Char(String='Email ID', tracking=True)

    active = fields.Boolean(default=True)

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.reference} - {rec.name}'
            res.append((rec.id, name))
        return res


    @api.constrains('email_id')
    def ValidateEmail(self):
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) != None:
            return True
        else:
            raise ValidationError(_("Invalid Email - Please enter a valid email address !"))


