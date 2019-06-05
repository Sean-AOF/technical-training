# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session Info' 
        
    name = fields.Char('Session_Name', required=True)    
    date_start = fields.Date(string='Start Date')
    end_date = fields.Date(string = 'End Date')
    course_id = fields.Many2one('open_academy.course', required=True)
    #teacher = fields.Many2one('open_academy.person', required=True)
    
#     course_name = fileds.Char(compute ='_compute_get_course_names')#
    
#     def _compute_course_names(self):
#         courses = self.mapped('course_id')
#         cources_uniquie= courses | course #union
        
        