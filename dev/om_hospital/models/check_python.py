from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


import re

class HospitalCheckPython(models.Model):
    _name = "hospital.check_python"

    def check_code(self):
        print("Button clicked!")



