from odoo import models, api, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    unique_code = fields.Char(string="Unique Code", copy=False)

    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        # if name:
        #     domain = args + ['|', '|', ('categ_id', operator, 'Office Furniture'),
        #                      ('name', operator, name),
        #                      ('default_code', operator, 'a'),
        #                      ('default_code', operator, 'b'),
        #                      ('default_code', operator, 'c'), ]
        # domain = args + [('default_code', operator, 'abc')]
        # '|', ('default_code', operator, 'b'),
        # ('default_code', operator, 'c')]

        if self.env.context.get('check_condition'):
            domain = args + [('gender', operator, 'male')]
        return super(ProductTemplate, self)._name_search(name, domain + args, operator, limit, name_get_uid)


