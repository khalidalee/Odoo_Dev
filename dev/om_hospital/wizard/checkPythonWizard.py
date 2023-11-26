from odoo import api, fields, models, _

# class HospitalCheckPython(models.Model):
class CheckPythonWizard(models.TransientModel):
    _name = "check.python.wizard"
    _description = "Check Python Wizard"

    output = fields.Text(String='Name')

    def testPython(self):
        self.output = "Testing Python using wizard"

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'check.python.wizard',
            'name': 'Check Python Wizard',
            'target': 'new',
            'res_id': self.id
        }
