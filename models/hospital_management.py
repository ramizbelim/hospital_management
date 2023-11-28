from odoo import models,fields,api
class hospital_management(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital Management"

    name = fields.Many2one('res.partner',string="Patient Name")
    age = fields.Integer(string="age")
    address = fields.Char(string="Address")

