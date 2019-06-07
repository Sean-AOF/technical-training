
# SAMPLE ODOO API MRP SCRIPT
import xmlrpc.client
from datetime import datetime

# Replace these with your own information.
url = 'http://localhost:8069'
db = 'dbname'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Odoo Version Information: " + str(common.version()))

# Get the user id
uid = common.authenticate(db, username, password, {})

# call methods of odoo models via the execute_kw RPC function
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Checks if the user has the access rights to run script
access = models.execute_kw(db, uid, password,
    'mrp.production', 'check_access_rights',
    ['write'], {'raise_exception': False})
print("MRP access: " + str(access))

# Checks if the user has the access rights for lots to run script
access_lot = models.execute_kw(db, uid, password,
    'stock.production.lot', 'check_access_rights',
    ['write'], {'raise_exception': False})
print("Lot access: " + str(access_lot))

# Example Lot number
cur_lot_num = "12001566103"
# Example of the product_id for lot
product_id = 29

# Create the lot/serial number that relates to the current product.
lot_id = models.execute_kw(db, uid, password,
        'stock.production.lot','create', [{
    'name': cur_lot_num, 'product_id': product_id}])

print("Id of the new Lot:" + str(lot_id))


##
## SAMPLE CODE FOR CONFIRMING A MO
##

# MO ID is the ID of the existing manufacturing order
mo_id = 5

# Check the avaliablity of the Materials
check_mo = models.execute_kw(db, uid, password,
    'mrp.production', 'action_assign', [mo_id])

print(check_mo)

# Create a context for the wizard which pops up when "PRODUCE" button is clicked

context = {'active_id': mo_id, 'active_ids': [mo_id], 'active_model': 'mrp.production'}
# Create the "produce" id through the wizard, note that the lot id that was created is passed through here
produce_id = models.execute_kw(db, uid, password,
'mrp.product.produce', 'create',
[{'product_id':product_id, 'product_qty': 1.0, 'mode': 'consume_produce', 'lot_id':lot_id}, context])

print(produce_id)

# Actually do the produce through the wizard.
wizard_result = models.execute_kw(db, uid, password, 'mrp.product.produce', 'do_produce', [[produce_id], context])

print(wizard_result)

# Mark the MO as done
if_done = models.execute_kw(db, uid, password,
    'mrp.production', 'button_mark_done', [mo_id])

print(if_done)
