{
    "name": "Yantra ERP",
    "author": "Jay",
    "category": "Custom",
    "summary": "Basic Yantra ERP",
    "depends": ["base","mail","product","sale"],
    "data":[
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/product_product.xml',
        'views/product_template_search_view.xml',
        'views/product_template_button.xml',
        'views/sale_quotation_custom.xml',
    ],
    "installable": True,
    "application": True,
}
