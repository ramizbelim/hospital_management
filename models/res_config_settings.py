from odoo import models, fields,api


class ResConfitSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_history_order = fields.Selection([('draft', 'Quotation State'),
                                           ('sale', 'Sale Order State')],
                                          string="Show History", comodel_name="sale.order",
                                          config_parameter='hospital_management.show_history_order')



