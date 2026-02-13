// Copyright (c) 2026, jyoti and contributors
// For license information, please see license.txt

frappe.query_reports["Tower wise account receivable report"] = {
	"filters": [
        {
            fieldname: "tower",
            label: "Tower",
            fieldtype: "Link",
            options: "Tower",
            reqd: 0
        }
    ]
};
