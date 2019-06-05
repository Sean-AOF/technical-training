# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Person(models.Model):
    _name = 'open_academy.person'
    _description = 'Person Info'
    
    first_name = fields.Char(string ='First Name',require=True)
    last_name = fields.Char(string='Last Name',require=True)

    person_typ=fields.Selection([
        ('teacher','Teacher'),
        ('student','Student'),
    ],string='Type')
    
    name = fields.Char(compute='_compute_name', store=True)
    
    
    @api.depends('first_name','last_name')
    def _compute_name(self):
        for rec in self:
            rec.name="{} {}".format(rec.first_name,rec.last_name)


		
		