from odoo import models, api, fields
class ProductTemplate(models.Model):
    _inherit = "product.product"

    unique_code = fields.Char(string="Unique Code", copy=False)


