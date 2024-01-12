from odoo import models, fields


class ResConfitSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_history_order = fields.Selection([('quotation_state', 'Quotation State'),
                                           ('sale_order_state', 'Sale Order State')],
                                          string="Show History", comodel_name="sale.order",
                                          config_parameter='hospital_management.show_history_order')
