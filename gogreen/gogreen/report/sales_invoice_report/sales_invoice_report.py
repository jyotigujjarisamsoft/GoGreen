# Copyright (c) 2024, jyoti and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
from xml.etree.ElementTree import tostring
import frappe
from frappe import _, msgprint
from frappe.utils import flt, getdate, comma_and
from collections import defaultdict
from datetime import datetime
from datetime import date
import json 


def execute(filters=None):
	columns, data = [], []
	global posting_date
	posting_date=filters.get("posting_date")
	customer_type=filters.get("customer_type")
	grand_parent=filters.get("grand_parent")
	print("grand_parent",grand_parent)
	customer_details = fetching_customer_details(grand_parent,customer_type)
	columns = get_columns()
	for customers in customer_details:
		data.append([customers['customer_name'],
		customers['custom_customer_typee'],
		customers['custom_grand_parent'],
		customers['custom_rate']
			])
	return columns, data



@frappe.whitelist()
def create_sales_invoice(grand_parent,customer_type,posting_date):
	customer_details = fetching_customer_details(grand_parent,customer_type)
	print("customer_details",customer_details)		
	for customer_data in customer_details:
		customer_name=customer_data['customer_name']
		#rate=customer_data['rate']
		print("customer_data------",customer_data)
		tax_template_data=fetching_tax_details()
		print("tax_template_data",tax_template_data)
		default_tax_data=[]
		for tax in tax_template_data:
    		# Check if the name key in the dictionary matches 'UAE VAT 5% - GG'
			if tax.get('name') == 'UAE VAT 5% - GG':
        		# Store the dictionary if a match is found
				default_tax_data = tax
		print("default_tax_data",default_tax_data)
		outerJson_si = {
		"doctype": "Sales Invoice",
		"customer": customer_name,
		"posting_date":posting_date,
		"due_date":posting_date,
		"taxes_and_charges":"UAE VAT 5% - GG",
		"items": [],
		"taxes":[]
		}
		
		innerJson = {
			"item_code":"Services",
			"qty":1,
			"rate":customer_data['custom_rate'],
			"doctype": "Sales Invoice Item"
			}
		taxes_details={
			"charge_type":default_tax_data['charge_type'],
			"account_head":default_tax_data['account_head'],
			"rate":default_tax_data['rate'],
			"description":default_tax_data['description'],
			"doctype": "Sales Taxes and Charges"
		}
		outerJson_si['items'].append(innerJson)
		outerJson_si['taxes'].append(taxes_details)
		print("outerJson_si",outerJson_si)
		if outerJson_si.get('items'):
			for item in outerJson_si['items']:
				if item.get('rate') is not None:
					print("Rate is not empty")
					doc_new_SI = frappe.new_doc("Sales Invoice")
					print("----------------------------")
					doc_new_SI.update(outerJson_si)
					print("++++++++++++")
					doc_new_SI.save()
					#frappe.db.commit()
					doc_new_SI.submit()
					print("=============================")
					frappe.msgprint("Sales Invoice created succesfully")
				else:
					frappe.throw("Please update rate in customer master for this customer "+'"'+customer_name+'"'+ " ")
		else:
			frappe.throw("Please update rate in customer master for this customer "+'"'+customer_name+'"'+ " ")
	          
	    

			
def fetching_customer_details(grand_parent,customer_type):
	customer_data = frappe.db.sql("""
	select customer_name,custom_customer_typee,custom_grand_parent,custom_rate
	from `tabCustomer` where custom_grand_parent in (select name from `tabCustomer Group` 
	where parent_customer_group='"""+grand_parent+"""' or customer_group_name='"""+grand_parent+"""')  and 
	custom_customer_typee='"""+customer_type+"""' and custom_status="Active"
	 """, as_dict=1)
	print("customer_data",customer_data)
	print("customer_type",customer_type)
	return customer_data

@frappe.whitelist()
def fetching_tax_details():
	tax_data = frappe.db.sql("""select stt.name,stc.charge_type,stc.account_head,stc.description,stc.rate
	from `tabSales Taxes and Charges` stc,
	`tabSales Taxes and Charges Template` stt where stt.name=stc.parent 
	 """, as_dict=1)
	print("tax_data",tax_data)
	return tax_data

def get_columns():
	"""return columns"""
	columns = [
		_("Customer")+"::200",
		_("customer_type")+"::200",
		_("grand_parent")+"::200",
		_("rate")+"::200"
		]
	return columns
