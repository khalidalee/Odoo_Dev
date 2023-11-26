{
    'name': 'Hospital Management System',
    'author': 'Khalid Ali',
    'website': 'https://nouvellesols.com',
    'summary': 'Odoo 16 Module to manage hospital facility',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/checkPythonWizard.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/check_python.xml'
    ],
    'assets':{
        "web.assets_backend":[
            "/om_hospital/static/src/css/om_hospital.css",
            # "/om_hospital/common/util/shopify/shopify_read.py",
            # "/om_hospital/models/shopify_read.py",
            # "om_hospital/models/testPython.py",
        ],
    }

}
