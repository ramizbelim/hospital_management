from odoo import models, fields, api


class SaleHistory(models.TransientModel):
    _name = 'sale.history'

    name = fields.Char(string="Sale Order")
    product = fields.Char(string="Product")


