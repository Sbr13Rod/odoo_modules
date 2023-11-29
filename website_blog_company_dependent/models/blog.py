from odoo import api, fields, models, _


class Blog(models.Model):
    _inherit = "blog.blog"

    company_id = fields.Many2one("res.company", string="Company")


class BlogPost(models.Model):
    _inherit = "blog.post"

    company_id = fields.Many2one(
        "res.company", string="Company", related="blog_id.company_id"
    )
