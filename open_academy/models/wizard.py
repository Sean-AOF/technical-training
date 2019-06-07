# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'open_academy.wizard'
    _description = "Wizard: Set Difficulty for Multiple Courses"
    
    
    def _get_courses(self):
        return self.env['open_academy.course'].browse(self.env.context.get('active_ids'))
    
    course_ids = fields.Many2many('open_academy.course', string="Courses", default=_get_courses)
    level = fields.Selection([
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    ], string='Difficulty')
    
    @api.multi
    def set_level(self):
        for record in self: 
            if record.course_ids:
                for course in record.course_ids:
                    course.level = self.level