# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WizzardModel(models.Model):
    _name = 'open_academy.wizzard'
    _description = 'wizzard info.'
    

    def _get_courses(self):
        return self.env["open_academy.course"].browse(self.env.context.get('active_ids'))

    course_ids = fields.Many2many('open_academy.course',string='Cources',default=_get_courses)


    level = fields.Selection([
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    ], string='Difficulty')

#wizard changes the course level from self from the check box next to the courses on the UI
    @api.multi
    def set_level(self):
        for record in self:
            if record.course_ids:
                for course in record.course_ids:
                    course.level = self.level