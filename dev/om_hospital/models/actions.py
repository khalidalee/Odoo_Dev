from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


import re

class HospitalActions(models.Model):
    _name = "hospital.actions"

    def check_code(self):
        print("Button clicked!")



