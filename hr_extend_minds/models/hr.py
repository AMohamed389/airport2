# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import requests
from datetime import date

import logging

_logger = logging.getLogger(__name__)


class hrextend(models.Model):
    _inherit = 'hr.employee'

    x_graduation_year = fields.Char(string='Year Of Graduation', index=True, tracking=True)

    x_staff_id = fields.Char(string='Staff Id', index=True, tracking=True)

    x_bank_account = fields.Char(string='Bank Account', index=True, tracking=True)

    x_religion = fields.Selection([('Muslim', 'Muslim'), ('Christian', 'Christian')],
                                  string="Religion", store=True, index=True, tracking=True)

    x_social_insurance_number = fields.Char(string='Social Insurance Number', index=True, tracking=True)

    x_social_insurance_status = fields.Selection(
        [('No', 'No'), ('New', 'New'), ('Pending', 'Pending'), ('Done', 'Done')],
        string="Social Insurance Status", store=True,
        index=True, tracking=True)

    # x_job_degree = fields.Selection(
    #     [('Degree 1', 'Degree 1'), ('Degree 2', 'Degree 2'), ('Degree 3', 'Degree 3'),
    #     ('Degree 4', 'Degree 4'), ('Degree 5', 'Degree 5'), ('Degree 6', 'Degree 6')
    #     , ('High Degree', 'High Degree'),('General Manager', 'General Manager')
    #     , ('Excellent Degree', 'Excellent Degree')],
    #     string="Job Degree", store=True,
    #     index=True, tracking=True)

    x_job_degree_id = fields.Many2one('job_degree',string="Degree", index=True, tracking=True)

    x_job_degree_date = fields.Date(string='Degree Date', index=True, tracking=True)

    x_pension_date = fields.Date(string='Pension Date', index=True, tracking=True)

    x_receiving_work_date = fields.Date(string='Receiving Work Date', index=True, tracking=True)

    # x_employee_status = fields.Selection(
    #     [('New', 'New'), ('Hired', 'Hired'), ('Interrupted From Work', 'Interrupted From Work'),
    #      ('Disability', 'Disability'), ('Leave Without Payment', 'Leave Without Payment'),
    #      ('Resigned', 'Resigned'), ('Pension', 'Pension'), ('Terminated', 'Terminated'), ('Death', 'Death')],
    #     string="Employee Status", store=True, index=True, tracking=True, default='New')

    x_hiring_date = fields.Date(string='Hiring Date', index=True, tracking=True)

    x_end_of_service_date = fields.Date(string='End Of Service Date', index=True, tracking=True)

    x_number_of_years = fields.Float(compute="get_number_of_years", string="Number Of Years", store=True)

    x_age = fields.Char(string="Age", compute="get_age_calc")

    x_employee_training = fields.One2many('employee.training', 'x_employee_id', string="Employee Training", store=True,
                                          index=True)

    x_employee_penalty = fields.One2many('employee.penalty', 'x_employee_id', string="Employee Penalty", store=True,
                                         index=True)

    x_education_certificate_level = fields.Date(string='Education Certificate Date', index=True, tracking=True)

    x_identity_issuer = fields.Char(string='Identity Issuer', index=True, tracking=True)

    x_military_status = fields.Selection([('Postponed','Postponed'),('Completed','Completed'),('Exempted','Exempted')], string='Military Status', index=True, tracking=True)

    x_mother_name = fields.Char(string='Mother Name', index=True, tracking=True)

    x_notes = fields.Text(string="Notes", tracking=True, store=True)

    x_military_start_date = fields.Date(string='Military Start Date', index=True, tracking=True)

    x_military_end_date = fields.Date(string='Military End Date', index=True, tracking=True)

    x_has_disability_condition = fields.Boolean(string='Has Disability Condition', index=True, tracking=True)

    x_is_delegated = fields.Boolean(string='Is Delegated', index=True, tracking=True)

    x_delegated_from = fields.Char(string='Delegated From', index=True, tracking=True)

    x_delegated_to = fields.Char(string='Delegated To', index=True, tracking=True)

    x_is_loaned = fields.Boolean(string='Is Loaned', index=True, tracking=True)

    x_loaned_from = fields.Char(string='Loaned From', index=True, tracking=True)

    x_loaned_to = fields.Char(string='Loaned To', index=True, tracking=True)

    x_section_name = fields.Char(index=True, string="Section", compute="_get_section_name")

    x_administration_name = fields.Char(compute="_get_administration_name", index=True, string="Administration")

    x_public_administration_name = fields.Char(compute="_get_public_administration_name", index=True, string="Public Administration")

    x_sector_name = fields.Char(compute="_get_sector_name", index=True, string="Sector")

    # x_qualitative_group_name = fields.Char(related="job_id.x_qualitative_group_id.name", index=True)

    x_qualitative_group_id = fields.Many2one('qualitative_group',string="Qualitative Group", index=True, tracking=True)

    x_oldest_hiring_date = fields.Date(string='Oldest Hiring Date', index=True, tracking=True)

    x_disability_id = fields.Char(string="Disability Id Number", index=True, tracking=True)

    x_supervision_job = fields.Many2one('hr.job',string="Supervision Job", index=True, tracking=True)

    x_hr_education_certificate_id = fields.One2many('hr_education_certificate', 'x_employee_id', string="Education Certificates", store=True,
                                          index=True)

    x_job_history = fields.One2many('job_history', 'x_employee_id', string="Job History", store=True,
                                          index=True)
    

    x_seniority_number = fields.Integer(string="Seniority Number", index=True, tracking=True)


    x_committee_employee = fields.One2many('committee_employee', 'x_employee_id', string="Comittees", store=True,
                                          index=True)


    def _get_section_name(self):
        for _rec in self:

            if _rec.department_id.x_type == "Department":
                _rec.x_section_name = _rec.department_id.name

            elif _rec.department_id.parent_id.x_type == "Department":
                _rec.x_section_name = _rec.department_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.x_type == "Department":
                _rec.x_section_name = _rec.department_id.parent_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.parent_id.x_type == "Department":
                _rec.x_section_name = _rec.department_id.parent_id.parent_id.parent_id.name
            
            else:
                _rec.x_section_name = None
    
    def _get_administration_name(self):
        for _rec in self:

            if _rec.department_id.x_type == "Administration":
                _rec.x_administration_name = _rec.department_id.name

            elif _rec.department_id.parent_id.x_type == "Administration":
                _rec.x_administration_name = _rec.department_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.x_type == "Administration":
                _rec.x_administration_name = _rec.department_id.parent_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.parent_id.x_type == "Administration":
                _rec.x_administration_name = _rec.department_id.parent_id.parent_id.parent_id.name
            
            else:
                _rec.x_administration_name = None
    
    def _get_public_administration_name(self):
        for _rec in self:

            if _rec.department_id.x_type == "Public Administration":
                _rec.x_public_administration_name = _rec.department_id.name

            elif _rec.department_id.parent_id.x_type == "Public Administration":
                _rec.x_public_administration_name = _rec.department_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.x_type == "Public Administration":
                _rec.x_public_administration_name = _rec.department_id.parent_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.parent_id.x_type == "Public Administration":
                _rec.x_public_administration_name = _rec.department_id.parent_id.parent_id.parent_id.name
            
            else:
                _rec.x_public_administration_name = None


    def _get_sector_name(self):
        for _rec in self:

            if _rec.department_id.x_type == "Sector":
                _rec.x_sector_name = _rec.department_id.name

            elif _rec.department_id.parent_id.x_type == "Sector":
                _rec.x_sector_name = _rec.department_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.x_type == "Sector":
                _rec.x_sector_name = _rec.department_id.parent_id.parent_id.name
            
            elif _rec.department_id.parent_id.parent_id.parent_id.x_type == "Sector":
                _rec.x_sector_name = _rec.department_id.parent_id.parent_id.parent_id.name
            
            else:
                _rec.x_sector_name = None

    def get_number_of_years(self):
        # _logger.info("Maged x_hiring_date !" + str(record.x_hiring_date))
        # _logger.info("Maged x_end_date !" + str(record.x_end_date))
        for record in self:
            if record.x_hiring_date:
                if record.x_end_of_service_date:
                    # _logger.info("Maged delta = record.x_end_date - record.x_hiring_date !")
                    delta = record.x_end_of_service_date - record.x_hiring_date
                    if delta and delta is not None:
                        # _logger.info("Maged delta 1 !" + str(delta))
                        record.x_number_of_years = round((delta.days / 365.25), 2)
                        return record.x_number_of_years
                else:
                    # _logger.info("Maged today = date.today() !")
                    today = date.today()
                    delta = today - record.x_hiring_date
                    if delta and delta is not None:
                        # _logger.info("Maged delta 2 !" + str(delta))
                        record.x_number_of_years = round((delta.days / 365.25), 2)
                        return record.x_number_of_years

        # _logger.info("Maged pass !")
        self.x_number_of_years = 0.0

    def get_age_calc(self):

        for record in self:
            try:
                if record.birthday:
                    #_logger.info("Maged record.birthday ! " + str(record.birthday))
                    today = date.today()
                    offset = int(record.birthday.replace(year=today.year) > today)  # int(True) == 1, int(False) == 0
                    #_logger.info("Maged offset ! " + str(offset))
                    record.x_age = str(date.today().year - record.birthday.year - offset)
                    #_logger.info("Maged record.x_age ! " + str(record.x_age))
                    return record.x_age
                else:
                    record.x_age = '0'
                    return record.x_age
            except Exception as ex:
                #_logger.info("Maged ex ! " + str(ex))
                record.x_age = '0'
                return record.x_age

    @api.constrains('identification_id')
    def _check_id_number_14(self):
        for rec in self:
            if len(str(rec.identification_id)) != 14:
                raise ValidationError("National Id number should be 14 digits !.")