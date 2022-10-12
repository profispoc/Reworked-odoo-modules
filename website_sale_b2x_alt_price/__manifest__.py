# Copyright 2020 Jairo Llopis - Tecnativa
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Alternative (un)taxed prices display on eCommerce",
    "summary": "Display prices with(out) taxes in eCommerce, complementing normal mode",
    "version": "15.0.1.0.0",
    "development_status": "Beta",
    "category": "Website",
    "website": "https://github.com/OCA/e-commerce",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "maintainers": ["Yajo"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["website_sale"],
    "data": [
        "templates/product.xml"
    ],
    'assets': {
        'web.assets_frontend': [
            'website_sale_b2x_alt_price/static/src/js/product_configurator_mixin.js',
        ],
        'web.assets_tests': [
            'website_sale_b2x_alt_price/static/tours/b2b.js',
            'website_sale_b2x_alt_price/static/tours/b2c.js',
        ],
    },
}
