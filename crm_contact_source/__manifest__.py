{
    "name": "Crm Contact Source",
    "summary": "Module with customizations to contactus form in website",
    "version": "12.0.1.0.0",
    "category": "Crm",
    "author": "Salva Benlloch",
    "maintainers": [
        "sbenlloch",
    ],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "website_crm",
    ],
    "data": [
        "views/crm_views.xml",
        "views/website_crm_templates.xml",
        "static/src/xml/assets.xml",
    ],
}
