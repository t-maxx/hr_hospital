from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HrHospitalPatient(models.Model):
    _name = "hr.hospital.patient"
    _description = "Hospital Patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(
        string="Full Name",
        required=True,
        tracking=True,
    )
    first_name = fields.Char(
        string="First Name",
    )
    last_name = fields.Char(
        string="Last Name",
    )
    date_of_birth = fields.Date(
        string="Date of Birth",
    )
    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True,
    )
    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
    )
    phone = fields.Char(
        string="Phone",
    )
    email = fields.Char(
        string="Email",
    )
    address = fields.Text(
        string="Address",
    )
    photo = fields.Image(
        string="Photo",
        max_width=256,
        max_height=256,
    )
    passport_number = fields.Char(
        string="Passport / ID Number",
    )
    personal_doctor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        string="Personal Doctor",
        tracking=True,
    )
    disease_ids = fields.Many2many(
        comodel_name="hr.hospital.disease",
        relation="hr_hospital_patient_disease_rel",
        column1="patient_id",
        column2="disease_id",
        string="Diseases",
    )
    visit_ids = fields.One2many(
        comodel_name="hr.hospital.visit",
        inverse_name="patient_id",
        string="Visits",
    )
    visit_count = fields.Integer(
        string="Visit Count",
        compute="_compute_visit_count",
        store=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    notes = fields.Text(
        string="Notes",
    )

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = fields.Date.today()
        for patient in self:
            if patient.date_of_birth:
                delta = relativedelta(today, patient.date_of_birth)
                patient.age = delta.years
            else:
                patient.age = 0

    @api.depends("visit_ids")
    def _compute_visit_count(self):
        for patient in self:
            patient.visit_count = len(patient.visit_ids)

    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        for patient in self:
            if patient.date_of_birth and patient.date_of_birth > fields.Date.today():
                raise ValidationError(
                    "Date of birth cannot be in the future."
                )
