// Copyright (c) 2026, jyoti and contributors
// For license information, please see license.txt

frappe.query_reports["GreatGrandParent Name wise account receivable report"] = {
	"filters": [
        {
            fieldname: "greatgrandparent_name",
            label: "GreatGrandParent Name",
            fieldtype: "Link",
            options: "GreatGrandParent Name",
            reqd: 0
        }
    ]
};
