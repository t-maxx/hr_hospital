{
    "name": "HR Hospital",
    "version": "17.0.1.0.0",
    "author": "t-maxx",
    "website": "https://test.local",
    "category": "Healthcare",
    "license": "OPL-1",
    "depends": [
        "base",
        "mail"
    ],
    "external_dependencies": {
        "python": []
    },
    "data": [
        "security/ir.model.access.csv",
        "data/hr_hospital_sequence_data.xml",
        "data/hr_hospital_disease_data.xml",
        "views/hr_hospital_doctor_views.xml",
        "views/hr_hospital_patient_views.xml",
        "views/hr_hospital_disease_views.xml",
        "views/hr_hospital_visit_views.xml",
        "views/hr_hospital_menus.xml",
    ],
    "demo": [
        "demo/hr_hospital_doctor_demo.xml",
        "demo/hr_hospital_patient_demo.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [
        "static/description/icon.png",
    ]
}