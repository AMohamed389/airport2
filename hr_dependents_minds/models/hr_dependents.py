# -*- coding: utf-8 -*-

from odoo import models, fields, api

from datetime import datetime
from datetime import date
import logging
_logger = logging.getLogger(__name__)


class hrdependents(models.Model):
    _name = 'hr.dependents'
    _order = 'name asc'

    employee_id = fields.Many2one('hr.employee', string="Employee Id", store=True, index=True,
                                 help="Employee Id", copy=True, track_visibility='always')

    name = fields.Char(string="Name", store=True, index=True,
                              help="Dependent Name", track_visibility='always', required=True)

    birth_date = fields.Date(string="Birth Date", store=True, index=True,
                       help="Dependent Birth Date", track_visibility='always', required=False)

    ssn = fields.Char(string="SSN", store=True, index=True,
                             help="Dependent SSN", track_visibility='always', required=False)

    mobile = fields.Char(string="Mobile Number", store=True, index=True,
                      help="Dependent Mobile Number", track_visibility='always', required=False)

    phone = fields.Char(string="Phone Number", store=True, index=True,
                         help="Dependent Phone Number", copy=True, track_visibility='always', required=False)

    ssn = fields.Char(string="SSN", store=True, index=True,
                      help="Dependent SSN", track_visibility='always', required=False)

    address = fields.Text(string="Address", store=True, index=True,
                      help="Dependent Address", copy=True, track_visibility='always', required=False)

    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')], string="Gender", store=True,
                              required=True, index=True, track_visibility='always')

    relationship = fields.Selection([('Spouse', 'Spouse'), ('Child', 'Child'), ('Domestic Partner', 'Domestic Partner')
                                     , ('Step Child', 'Step Child'), ('Foster Child', 'Foster Child')], string="Relationship", store=True,
                              required=True, index=True, track_visibility='always')
    
    has_disability_condition = fields.Boolean(string='Has Disability Condition', index=True, tracking=True)

    class hrextend(models.Model):
        _inherit = 'hr.employee'

        employee_dependents = fields.One2many('hr.dependents', 'employee_id',
                                                  string='Employee Dependents',
                                                  help="Employee Dependents", index=True, store=True,
                                                  track_visibility="always")
