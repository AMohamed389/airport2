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


class hr_report(models.Model):
    _name = 'hr_report'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date DESC'

    name = fields.Selection([('بيان حالة','بيان حالة')], string="Statement Document", index=True, required=True, tracking=True)
    x_employee_id = fields.Many2one('hr.employee', string="Employee", store=True, required=True, tracking=True, index=True)
    state = fields.Selection([
        ('Draft', 'Draft'),('Submit', 'Submit'),('Completed', 'Completed')
    ], string='Report State' ,default='Draft', index=True, tracking=True)

    active = fields.Boolean(string='Active',index=True,default=True)



    def submit_report(self):
        for _rec in self:
            _rec.state = 'Submit'


    
