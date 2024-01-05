from odoo import models,fields,api

class SaleLine(models.Model):
    _inherit = 'sale.order.line'

    total_one = fields.Text(string="Stock On Quantity",compute="_compute_on_hand_quantity_count",store=True)
    @api.depends('product_template_id','product_id')
    def _compute_on_hand_quantity_count(self):
        for rec in self:
            # quat = rec.product_id.mapped("stock_quant_ids").filtered(lambda qty : qty.location_id.usage == "Internal Location").mapped("quant_ids").filtered(lambda quant : quant.quantity)
            quat = rec.product_id.mapped("stock_quant_ids").filtered(lambda qty : qty.location_id.usage == "internal").quantity
        if quat != 0 :
            rec.total_one = quat
            # print("==============",quat)
        else:
            rec.total_one = 0

