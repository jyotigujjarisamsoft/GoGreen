// Copyright (c) 2026, jyoti and contributors
// For license information, please see license.txt

frappe.query_reports["Cluster wise account receivable report"] = {
	 "filters": [
        {
            fieldname: "cluster",
            label: "Cluster",
            fieldtype: "Link",
            options: "Cluster",
            reqd: 0
        }
    ]
};
