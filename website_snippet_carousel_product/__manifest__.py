# Copyright 2020 Tecnativa - Alexandre D. Díaz
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Website Snippet Carousel Product",
    "version": "13.0.1.0.0",
    "category": "Website",
    "author": "Tecnativa, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/e-commerce",
    "license": "LGPL-3",
    "summary": "Adds a new snippet to insert a carousel of products",
    "depends": ["website_sale"],
    "data": [
        #"templates/assets.xml",
        "templates/snippet.xml"
    ],
    "installable": True,
    "maintainers": ["Tardo"],
    'assets': {
        'web.assets_frontend': [
            'website_snippet_carousel_product/static/src/scss/s_product_carousel.scss',
            'website_snippet_carousel_product/static/src/js/s_product_carousel_frontend.js',
        ],
        'website.assets_editor': [
            'website_snippet_carousel_product/static/src/js/snippet.options.js',
        ],
    },
}
