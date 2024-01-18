from odoo import models, fields, api


class SaleOrderHistory(models.TransientModel):
    _name = 'sale.order.history'

    name = fields.Many2one('res.partner', string="Customer")
    product_id = fields.Many2one('product.template', string="Product")
    product_details_ids = fields.Many2many('sale.order.line', string="Product History")

    # def action_show_history(self):
    #     product_history_id = self.env["sale.order.line"].search(
    #         [('product_template_id.name', '=', self.product), ('order_id.partner_id.name', '=', self.name)])
    #     print("===============================================", product_history_id)
    #     for rec in product_history_id:
    #         # print("===============================================",product_history_id.name)
    #         print("===============================================", rec.name)
    #         print("===============================================", rec.product_uom_qty)

    @api.model
    def default_get(self, fields_list):
        sale_order_line_id = self.env.context.get("active_id")

        record = self.env["sale.order.line"].browse(sale_order_line_id)
        res = super().default_get(fields_list)
        res["name"] = record.order_id.partner_id
        res["product_id"] = record.product_template_id
        show_order_history = self.env['ir.config_parameter'].get_param('hospital_management.show_history_order')
        # test = self.env["res.config.settings"].show_history
        # store_record = self.env["sale.order.line"].search([],limit=3)
        product_order_history = self.env["sale.order.line"].search([('order_id.partner_id.name', '=', res["name"].name),
                                                                    ('product_template_id.name', '=',
                                                                     res["product_id"].name),
                                                                    ('order_id.state', '=', show_order_history)])
        # print('\n============',fields.Command.set([int(record) for record in store_record]))
        # print("-----------------",product_order_history)
        # print("-----------------",show_order_history)
        # print("-----------------",record.order_id.state)
        res.update({
            'product_details_ids': [(fields.Command.set([int(rec) for rec in product_order_history]))]
        })

        return res
