from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import re

class HospitalPatients(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread"]
    _description = "Patient Records"

    name = fields.Char(String='Name', required=True, tracking=True)
    age = fields.Integer(String='Age', tracking=True)
    is_child = fields.Boolean(String='Is Child ?', tracking=True)
    notes = fields.Text(String='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], String='Gender', tracking=True)
    capitalized_name = fields.Char(String='Capitalized Name', compute='_compute_capitalized_name', store=True)
    doctor_id = fields.Many2one('hospital.doctor', String="Doctor")
    tag_ids = fields.Many2many("res.partner.industry", string="Tags")
    email = fields.Char(String='Email ID', tracking=True)

    @api.constrains('is_child', 'age', 'email')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))

        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) != None:
            return True
        else:
            raise ValidationError(_("Invalid Email - Please enter a valid email address !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ""

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False


