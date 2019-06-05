# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Person(models.Model):
    _name = 'open_academy.person'
    _description = 'Person Info'
    _rec_name = 'title'

    title = fields.Char(string = 'Title',require=True)
    first_name = fields.Char(string ='First Name')
    last_name = fields.Char(string='Last Name')
	@api.multi
	def name_get(self):
		reutn[
			(rec.id, "{}" {}".format(rec.first_name,rec.last_name))
			for rec in self
		]
		
		