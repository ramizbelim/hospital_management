from odoo import models,fields,api
class hospital_department(models.Model):
    _name = "hospital.department"
    _description = "Hospital Management for Department"

    # name = fields.Many2one("hospital.hospital",string="Department Name")
    name = fields.Char("Department Name")
    number_of_doctor = fields.Integer(string="Number of Docter")
    address = fields.Char(string="Address")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    # decription = fields.Char(string="Description")

