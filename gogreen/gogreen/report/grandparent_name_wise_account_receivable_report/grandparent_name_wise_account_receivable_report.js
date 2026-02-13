// Copyright (c) 2026, jyoti and contributors
// For license information, please see license.txt

frappe.query_reports["GrandParent Name wise account receivable report"] = {
	"filters": [
        {
            fieldname: "grandparent_name",
            label: "GrandParent Name",
            fieldtype: "Link",
            options: "GrandParent Name",
            reqd: 0
        }
    ]
};
