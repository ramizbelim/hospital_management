from odoo import models, fields, api


class SaleOrderHistory(models.TransientModel):
    _name = 'sale.order.history'

    name = fields.Char(string="Customer")
    product = fields.Char(string="Product")
    product_details_ids = fields.Many2many('sale.order.line')

    # name = fields.Many2one('sale.history', string="Customer")
    # product = fields.Char(string="Product")
    # product_details_ids = fields.Many2many('sale.order.line')
    @api.model
    def default_get(self, fields):
        res = super(SaleOrderHistory, self).default_get(fields)
        res["name"] = self.env["sale.order.line"].browse(self.env.context.get("active_id")).order_id.partner_id.name
        res["product"] = self.env["sale.order.line"].browse(self.env.context.get("active_id")).name
        # product_history_ids = self.env["sale.order.line"].search(
        #     [('product_template_id.name', '=', self.product), ('order_id.partner_id.name', '=', self.name)])
        return res

    # def action_show_history(self):
    #     product_history_id = self.env["sale.order.line"].search(
    #         [('product_template_id.name', '=', self.product), ('order_id.partner_id.name', '=', self.name)])
    #     print("===============================================", product_history_id)
    #     for rec in product_history_id:
    #         # print("===============================================",product_history_id.name)
    #         print("===============================================", rec.name)
    #         print("===============================================", rec.product_uom_qty)
