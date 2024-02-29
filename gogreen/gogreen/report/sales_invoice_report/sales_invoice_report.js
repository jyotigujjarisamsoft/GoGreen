// Copyright (c) 2024, jyoti and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["sales invoice report"] = {
	"filters": [
		{
			"fieldname": "posting_date",
			"label": __("Posting Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
		
		{
            "label": __("Customer Type"),
            "fieldname": "customer_type",
            "fieldtype": "Select",
            "options": ["", "Regular",
                "Advance"
                
            ],
			"reqd": 1
        },
		{
			"fieldname": "grand_parent",
			"label": __("Grand Parent"),
			"fieldtype": "Link",
			"options": "Customer Group",
			"reqd": 1,
			"get_query": function() {
				return {
				"doctype": "Customer Group",
				"filters": {
				"is_group": 1,
				"name": ["!=", "All Customer Groups"]
				}
				}
				}
		}
		
	],
	onload: function(report) {
		report.page.add_inner_button(__("Create Sales Invoice"), function() {
			var customer_type = frappe.query_report.get_filter_value('customer_type');
        console.log("customer_type----",customer_type)
		var grand_parent = frappe.query_report.get_filter_value('grand_parent');
        console.log("grand_parent----",grand_parent)
		var posting_date = frappe.query_report.get_filter_value('posting_date');
        console.log("posting_date----",posting_date)
			create_multiple_sales_invoices(grand_parent,customer_type,posting_date);
			;}
		)
	}
};

function create_multiple_sales_invoices(grand_parent,customer_type,posting_date) {
    frappe.call({
        method: 'gogreen.gogreen.report.sales_invoice_report.sales_invoice_report.create_sales_invoice',
        args: {
            "grand_parent":grand_parent,
			"customer_type":customer_type,
			"posting_date":posting_date
        },
        async: false,
        callback: function(r) {
            console.log("updated")

        }
    });
}





