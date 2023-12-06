from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta
class hospital_management(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital Management"

    name = fields.Char(string="Patient Name")
    patient_id = fields.Many2one('res.partner',string="Patient Name")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age",compute="age_find")
    address = fields.Char(string="Address",required=True)
    child = fields.Boolean(string="Is_child?")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    partner_id  = fields.Many2one(comodel_name='hospital.hospital',string="Demo")
    tag_ids = fields.Many2many(comodel_name='res.partner.category',string="category")
    patient_entry_id = fields.Many2one('res.partner',string="Patient Id")

    @api.depends('dob')
    def age_find(self):
        # self.age = False
        for record in self:
            record.age = relativedelta(date.today(),record.dob).years
    @api.onchange('age')
    def _onchange_child(self):
        if self.age>=18:
            self.child = False
        else:
            self.child = True
    @api.onchange('address')
    def button_action(self):
        print("Button Clicked ........")
        print("Value of self.address:", self.address)
        # if len(self.address)>5:
        #     print(len(self.address))

    def button_action_second(self):
        print("Second Button Clicked!!!!!!!!!!!!!!!!!!!!!!!!")



