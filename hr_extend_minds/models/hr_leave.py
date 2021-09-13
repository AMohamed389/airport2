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


class hrleaveextend(models.Model):
    _inherit = 'hr.leave'

    x_sector_name = fields.Char(related="employee_id.x_sector_name", index=True)
    x_public_administration_name = fields.Char(related="employee_id.x_public_administration_name", index=True)
    x_administration_name = fields.Char(related="employee_id.x_administration_name", index=True)
    x_section_name = fields.Char(related="employee_id.x_section_name", index=True)
    x_staff_id = fields.Char(related="employee_id.x_staff_id", index=True)
    x_issuer = fields.Char(string="Source", index=True, tracking=True)