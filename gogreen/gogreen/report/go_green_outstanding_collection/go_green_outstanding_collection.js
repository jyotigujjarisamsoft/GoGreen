// Copyright (c) 2026, Your Company
// For license information, please see license.txt

frappe.query_reports["Go Green Outstanding Collection"] = {
    filters: [
        {
            fieldname: "grandparent_name",
            label: __("GrandParent"),
            fieldtype: "Link",
            options: "GrandParent Name", // <--- Replace with your actual GrandParent DocType name
            width: 150,
        },
        {
            fieldname: "cluster",
            label: __("Cluster"),
            fieldtype: "Link",
            options: "Cluster", // <--- Replace with your actual Cluster DocType name
            width: 150,
        },
        {
            fieldname: "tower",
            label: __("Tower"),
            fieldtype: "Link",
            options: "Tower", // <--- Replace with your actual Tower DocType name
            width: 180,
        },
        {
            fieldname: "ledger_name",
            label: __("Ledger Name"),
            fieldtype: "Link",
            options: "Customer", // Standard ERPNext DocType for Ledger/Customer
            width: 200,
        },
    ],

    // Optional: format the merged total column to be bold
    formatter: function (value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);
        if (column.fieldname === "total_customer_outstanding" && value) {
            value = `<span style="font-weight:600;">${value}</span>`;
        }
        return value;
    },
};
