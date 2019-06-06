# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Person(models.Model):
    _name = 'open_academy.person'
    
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    name = fields.Char(compute='_compute_name', store=True)
    
    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = "{} {}".format(rec.first_name, rec.last_name)
    
#     @api.multi
#     def name_get(self):
#         return [o
#             (rec.id, "{} {}".format(rec.first_name, rec.last_name))
#             for rec in self
#         ]
            
    