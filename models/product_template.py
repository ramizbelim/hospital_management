from odoo import models, api,fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    unique_code = fields.Char(string="Unique Code",
                              compute="_compute_unique_code",store=True,
                              readonly=False)
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = args + ['|', '|', ('categ_id', operator, 'Office Furniture'),
                             ('name', operator, name),
                             ('default_code', operator, 'a'),
                             ('default_code', operator, 'b'),
                             ('default_code', operator, 'c'),]
            # domain = args + [('default_code', operator, 'abc')]
            # '|', ('default_code', operator, 'b'),
            # ('default_code', operator, 'c')]
        return super(ProductTemplate, self)._name_search(name, domain, operator, limit, name_get_uid)

    # @api.depends_context('company')
    @api.depends('product_variant_ids', 'product_variant_ids.unique_code')
    def _compute_unique_code(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.unique_code = template.product_variant_ids.standard_price
        for template in (self - unique_variants):
            template.unique_code = 0.0
