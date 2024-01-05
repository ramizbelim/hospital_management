from datetime import date

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class hospital_management(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital Management"

    name = fields.Char(string="Patient Name")
    name_hospital = fields.Char(string="Hospital Name", compute='name_hospitals')
    patient_id = fields.Many2one("res.partner", string="Patient Name")
    mobile = fields.Char(string="Mobile No.", related="patient_id.phone")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="age_find")
    address = fields.Char(string="Address", required=True, help="Enter the Age")
    child = fields.Boolean(string="Is_child?")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    partner_id = fields.Many2one(comodel_name='hospital.hospital', string="Demo")
    tag_ids = fields.Many2many(comodel_name='res.partner.category', string="category")
    doc_attachement = fields.Binary(string="Attachement")
    patient_entry_id = fields.Many2one('res.partner', string="Patient Id")
    city = fields.Selection([('surat', 'Surat'), ('ahmedabad', 'Ahmedavad'), ('vadodara', 'Vadodara')],
                            string="City", )
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')],
        string='Status', required=True, readonly=True, copy=False,
        default='draft')

    @api.depends('dob')
    def age_find(self):
        # self.age = False
        for record in self:
            record.age = relativedelta(date.today(), record.dob).years

    @api.onchange('age')
    def _onchange_child(self):
        if self.age >= 18:
            self.child = False
        else:
            self.child = True

    @api.onchange('address')
    def onchange_button_action(self):
        print("Button Clicked ........")
        print("Value of self.address:", self.address)
        try:
            if len(self.address) > 5:
                print(len(self.address))
            else:
                print("Nothing to show........")
        except TypeError:
            print("Error: Unable to calculate length of address.")

    def button_action_second(self):
        print("Second Button Clicked!!!!!!!!!!!!!!!!!!!!!!!!")

    @api.onchange("patient_id")
    def onchange_name(self):
        if self.patient_id:
            self.update({'address': self.patient_id.email})

    def button_in_progress(self):
        self.write({
            'state': "in_progress"
        })

    def name_hospitals(self):
        self.name_hospital = "ABCD Hospital"


    @api.model
    def name_get(self):
        res = []
        for rec in self:
            name = rec.name_hospital + '/' + rec.patient_id.name
            res.append((rec.id, name))
            print("==============",rec.name)
            print("==============",rec.id)
            print("==============",name)
        return res

