
# -*- coding: utf-8 -*-
 
from odoo import models, fields, api, _
 
class SaleOrder(models.Model):
    _inherit = 'sale.order'
   
    session_id = fields.Many2one('open_academy.session', string="Session")
 
 
# This is for a new xml view
 
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <record id="sale_order_form_inherit" model="ir.ui.view">
    <field name="name">sale.order.form.inherit</field>
    <field name="model">sale.order</field>
    <field name="inherit_id" ref="sale.view_order_form"/>
    <field name="arch" type="xml">
        <xpath expr="//group//group[2]/field[@name='payment_term_id']" position="after">
          <field name="session_id" string="Session"/>
        </xpath>
       
        <xpath expr="//field[@name='confirmation_date']" position="replace"/>
    </field>
</record>
</odoo>