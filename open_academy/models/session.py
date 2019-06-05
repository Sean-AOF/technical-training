session
# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session Info' 
      
    title = fields.Char(string = 'Title',require=True)
    
    date_start = fields.Date(string='Start Date')
    end_date = fields.Date(string = 'End Date')
   