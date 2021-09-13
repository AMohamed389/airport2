# -*- coding: utf-8 -*-

from odoo import api, fields, models


class hr_employee_report(models.TransientModel):
    _name = 'hr_statement_document'
    
    x_employee_id = fields.Many2one('hr.employee', string="Employee", store=True, tracking=True, index=True)

    is_full_department_name = fields.Boolean(string="Full Department Name")
    is_sector = fields.Boolean(string="Sector", default=True)
    is_public_administartion = fields.Boolean(string="Public Administration")
    is_administration = fields.Boolean(string="Administration")
    is_section = fields.Boolean(string="Section")
    is_manager = fields.Boolean(string="Manager")
    is_staff_id = fields.Boolean(string="Staff Id", default=True)
    is_insurance_number = fields.Boolean(string="Insurance Number", default=True)
    is_qualitative_group = fields.Boolean(string="Qualitative Group", default=True)
    is_degree = fields.Boolean(string="Degree", default=True)
    is_job_position = fields.Boolean(string="Job Position", default=True)
    is_employee_name = fields.Boolean(string="Employee Name", default=True)
    is_supervision_job = fields.Boolean(string="Supervision job")
    is_hiring_date = fields.Boolean(string="Hiring Date", default=True)
    is_birth_date = fields.Boolean(string="Birth Date", default=True)
    is_gender = fields.Boolean(string="Gender", default=True)
    is_pension_date = fields.Boolean(string="Pension Date", default=True)
    is_marital_status = fields.Boolean(string="Marital Status", default=True)
    is_employee_address = fields.Boolean(string="Employee Address", default=True)
    is_national_id = fields.Boolean(string="National Id", default=True)
    is_id_issuer = fields.Boolean(string="National Id Issuer", default=True)
    is_military_status = fields.Boolean(string="Military Statys", default=True)
    is_place_of_birth = fields.Boolean(string="Place Of Birth", default=True)
    is_mother_name = fields.Boolean(string="Mother Name", default=True)
    is_receiving_Working_date = fields.Boolean(string="Receiving Working Date", default=True)
    is_employee_pic = fields.Boolean(string="Employee Pic")
    is_oldest_hiring_date = fields.Boolean(string="Oldest Hiring Date")
    is_training = fields.Boolean(string="Trainings")
    is_penalties = fields.Boolean(string="Penalties")
    is_job_history = fields.Boolean(string="Job History")
    is_education_certificates = fields.Boolean(string="Education Certificates")
    is_committee = fields.Boolean(string="Committees")
    is_education_certificate_level = fields.Boolean(string="Education Certificate Level")
    is_age = fields.Boolean(string="Age")
    is_email = fields.Boolean(string="Email")
    is_phone = fields.Boolean(string="Phone")
    is_mobile_phone = fields.Boolean(string="Mobile Phone")
    is_work_phone = fields.Boolean(string="Work Phone")