from odoo import api, fields, models


class HrHospitalDoctor(models.Model):
    _name = "hr.hospital.doctor"
    _description = "Hospital Doctor"
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
    specialty = fields.Char(
        string="Specialty",
        required=True,
        tracking=True,
    )
    phone = fields.Char(
        string="Phone",
    )
    email = fields.Char(
        string="Email",
    )
    photo = fields.Image(
        string="Photo",
        max_width=256,
        max_height=256,
    )
    visit_ids = fields.One2many(
        comodel_name="hr.hospital.visit",
        inverse_name="doctor_id",
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

    @api.depends("visit_ids")
    def _compute_visit_count(self):
        for doctor in self:
            doctor.visit_count = len(doctor.visit_ids)
