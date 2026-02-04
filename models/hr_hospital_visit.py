from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HrHospitalVisit(models.Model):
    _name = "hr.hospital.visit"
    _description = "Patient Visit"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "date_visit desc, id desc"

    name = fields.Char(
        string="Reference",
        required=True,
        copy=False,
        readonly=True,
        default="New",
    )
    date_visit = fields.Datetime(
        string="Visit Date",
        required=True,
        default=fields.Datetime.now,
        tracking=True,
    )
    patient_id = fields.Many2one(
        comodel_name="hr.hospital.patient",
        string="Patient",
        required=True,
        tracking=True,
    )
    doctor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        string="Doctor",
        required=True,
        tracking=True,
    )
    disease_id = fields.Many2one(
        comodel_name="hr.hospital.disease",
        string="Diagnosis",
        tracking=True,
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("scheduled", "Scheduled"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="draft",
        required=True,
        tracking=True,
    )
    symptoms = fields.Text(
        string="Symptoms",
    )
    diagnosis_description = fields.Text(
        string="Diagnosis Description",
    )
    treatment = fields.Text(
        string="Prescribed Treatment",
    )
    notes = fields.Text(
        string="Notes",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "hr.hospital.visit"
                ) or "New"
        return super().create(vals_list)

    def action_schedule(self):
        for visit in self:
            visit.state = "scheduled"

    def action_start(self):
        for visit in self:
            visit.state = "in_progress"

    def action_done(self):
        for visit in self:
            if not visit.disease_id:
                raise ValidationError(
                    "Please set a diagnosis before completing the visit."
                )
            visit.state = "done"

    def action_cancel(self):
        for visit in self:
            visit.state = "cancelled"

    def action_draft(self):
        for visit in self:
            visit.state = "draft"
