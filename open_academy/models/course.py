# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course info'
    
    name = fields.Char(string='Title', required=True)
    
#     descriptions = fields.Char(string='description', required=True,default="a value")
    
    level = fields.Selection([
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    ], string='Difficulty')