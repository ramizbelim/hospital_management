from odoo import models,fields,api
class Contacts(models.Model):
    _inherit = 'res.partner'

    department_name = fields.Char(string="Department")
    description = fields.Char(string="Description")
    patient_entry_ids = fields.One2many('hospital.hospital', "patient_entry_id","Patient")
    p_mobile = fields.Char(string="Mobile")




