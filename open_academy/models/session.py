# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session info.'
    
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string='End Date')
    course = fields.Many2one('open_academy.course', required=True)
    
    instructor_id = fields.Many2one('res.users', string="Instructor")
