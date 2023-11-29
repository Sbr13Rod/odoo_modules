from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_source = fields.Selection(
        [
            ("third", "Third parties"),
            ("social_networks", "Social Networks"),
            ("internet_search", "Internet search"),
        ],
        string="Contact source",
    )
