# -*- coding: utf-8 -*-

from odoo.addons.website_form.controllers.main import WebsiteForm


class WebsiteForm(WebsiteForm):
    def insert_record(self, request, model, values, custom, meta=None):
        if model.model == "crm.lead":
            if "company_id" not in values:
                values["company_id"] = request.website.company_id.id
        if model.model == "crm.lead" and request.params.get("contact_source"):
            values["contact_source"] = request.params["contact_source"]
        return super(WebsiteForm, self).insert_record(
            request, model, values, custom, meta=meta
        )
