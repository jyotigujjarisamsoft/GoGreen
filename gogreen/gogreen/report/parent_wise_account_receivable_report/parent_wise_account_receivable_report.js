// Copyright (c) 2026, jyoti and contributors
// For license information, please see license.txt

frappe.query_reports["Parent wise account receivable report"] = {
	"filters": [
        {
            fieldname: "parent_name",
            label: "Parent Name",
            fieldtype: "Link",
            options: "Parent Name",
            reqd: 0
        }
    ]
};
