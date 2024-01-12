from odoo import models,fields,api

class Sale(models.Model):
    _inherit = 'sale.order'

    name_id = fields.Char(string="Department")
    send_mail = fields.Boolean(string="Send Mail")
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    # def _name_search(self,name,args=None,operator='like', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if self.env.context.get('check_condition'):
    #         domain = args + [('gender',operator,'male')]
    #     return self._name_search(domain+args, limit=limit, access_rights_uid=name_get_uid)




class SentMail(models.TransientModel):
    _inherit = 'mail.compose.message'

    def action_send_mail(self):
        sale_id = self.env["sale.order"].browse(self.res_id)
        sale_id.send_mail = True



