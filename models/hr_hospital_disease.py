from odoo import fields, models


class HrHospitalDisease(models.Model):
    _name = "hr.hospital.disease"
    _description = "Disease Type"
    _order = "name"
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char(
        string="Disease Name",
        required=True,
    )
    code = fields.Char(
        string="Disease Code",
    )
    description = fields.Text(
        string="Description",
    )
    parent_id = fields.Many2one(
        comodel_name="hr.hospital.disease",
        string="Parent Category",
        index=True,
        ondelete="cascade",
    )
    child_ids = fields.One2many(
        comodel_name="hr.hospital.disease",
        inverse_name="parent_id",
        string="Subcategories",
    )
    parent_path = fields.Char(
        index=True,
        unaccent=False,
    )
    patient_ids = fields.Many2many(
        comodel_name="hr.hospital.patient",
        relation="hr_hospital_patient_disease_rel",
        column1="disease_id",
        column2="patient_id",
        string="Patients",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
