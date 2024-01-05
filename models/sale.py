from odoo import models,fields,api

class Sale(models.Model):
    _inherit = 'sale.order'

    name_id = fields.Char(string="Department")
    send_mail = fields.Boolean(string="Send Mail")

class SentMail(models.TransientModel):
    _inherit = 'mail.compose.message'

    def action_send_mail(self):
        sale_id = self.env["sale.order"].browse(self.res_id)
        sale_id.send_mail = True

