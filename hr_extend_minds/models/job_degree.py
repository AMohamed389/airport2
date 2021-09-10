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


class job_degree(models.Model):
    _name = 'job_degree'
    _order = 'create_date DESC'

    name = fields.Char(string="Degree", index=True, required=True, tracking=True)
    x_qualitative_group_id = fields.Many2one('qualitative_group', string="Qualitative Group", index=True, tracking=True)

    active = fields.Boolean(string='Active',index=True,default=True,tracking=True)
