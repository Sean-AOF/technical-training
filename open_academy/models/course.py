# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class open_academy(models.Model):
#     _name = 'open_academy.open_academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100



#from odoo import models,fields,api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course Info'
    _rec_name = 'title'

    title = fields.Char()
    level = fields.Selection([
        ('easy','Easy'),
        ('normal','Normal'),
        ('hard','Hard')
    ])
