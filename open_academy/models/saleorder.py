
# -*- coding: utf-8 -*-
 
from odoo import models, fields, api, _
 
class SaleOrder(models.Model):
    _inherit = 'sale.order'
   
    session_id = fields.Many2one('open_academy.session', string="Session")
 
 
# This is for a new xml view
 
