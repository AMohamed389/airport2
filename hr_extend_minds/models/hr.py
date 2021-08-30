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

    x_job_degree = fields.Selection(
        [('Degree 1', 'Degree 1'), ('Degree 2', 'Degree 2'), ('Degree 3', 'Degree 3'),
         ('General Manager', 'General Manager')],
        string="Job Degree", store=True,
        index=True, tracking=True)

    x_job_degree_date = fields.Date(string='Job Degree Date', index=True, tracking=True)

    x_pension_date = fields.Date(string='Pension Date', index=True, tracking=True)

    x_receiving_work_date = fields.Date(string='Receiving Work Date', index=True, tracking=True)

    x_employee_status = fields.Selection(
        [('New', 'New'), ('Hired', 'Hired'), ('Interrupted From Work', 'Interrupted From Work'),
         ('Disability', 'Disability'), ('Leave Without Payment', 'Leave Without Payment'),
         ('Resigned', 'Resigned'), ('Pension', 'Pension'), ('Terminated', 'Terminated'), ('Death', 'Death')],
        string="Employee Status", store=True, index=True, tracking=True, default='New')

    x_hiring_date = fields.Date(string='Hiring Date', index=True, tracking=True)

    x_end_of_service_date = fields.Date(string='End Of Service Date', index=True, tracking=True)

    x_number_of_years = fields.Float(compute="get_number_of_years", string="Number Of Years", store=True)

    x_age = fields.Integer(string="Age", compute="get_age_calc")

    x_employee_training = fields.One2many('employee.training', 'x_employee_id', string="Employee Training", store=True,
                                          index=True)

    x_employee_penalty = fields.One2many('employee.penalty', 'x_employee_id', string="Employee Penalty", store=True,
                                         index=True)

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
                    record.x_age = date.today().year - record.birthday.year - offset
                    #_logger.info("Maged record.x_age ! " + str(record.x_age))
                    return record.x_age
                else:
                    record.x_age = 0
                    return record.x_age
            except Exception as ex:
                #_logger.info("Maged ex ! " + str(ex))
                record.x_age = 0
                return record.x_age
