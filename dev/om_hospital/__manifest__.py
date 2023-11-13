{
    'name': 'Hospital Management System',
    'author': 'Khalid Ali',
    'website': 'https://nouvellesols.com',
    'summary': 'Odoo 16 Module to manage hospital facility',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/actions.xml'
    ],
    'assets':{
        "web.assets_backend":[
            "/om_hospital/static/src/css/om_hospital.css",
        ],
    }

}
