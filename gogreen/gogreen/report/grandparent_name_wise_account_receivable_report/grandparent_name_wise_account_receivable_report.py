# Copyright (c) 2026, jyoti and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Grandparent Name"),
            "fieldname": "grandparent_name",
            "fieldtype": "Data",
            "width": 220
        },
        {
            "label": _("Sales Invoice"),
            "fieldname": "sales_invoice",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 180
        },
        {
            "label": _("Customer"),
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 180
        },
        {
            "label": _("Outstanding Amount"),
            "fieldname": "outstanding_amount",
            "fieldtype": "Currency",
            "width": 150
        },
    ]


def get_data(filters):
    data = []

    conditions = ""
    values = {}

    # Apply Grandparent filter
    if filters and filters.get("grandparent_name"):
        conditions += " AND grandparent_name = %(grandparent_name)s"
        values["grandparent_name"] = filters.get("grandparent_name")

    # Get Grandparent totals
    totals = frappe.db.sql(f"""
        SELECT
            grandparent_name,
            SUM(outstanding_amount) as total
        FROM `tabSales Invoice`
        WHERE docstatus = 1
        {conditions}
        GROUP BY grandparent_name
        ORDER BY grandparent_name
    """, values, as_dict=True)

    for row in totals:
        # Parent Row
        data.append({
            "grandparent_name": row.grandparent_name,
            "outstanding_amount": row.total,
            "indent": 0
        })

        # Child Rows (Invoices under Grandparent)
        invoices = frappe.db.sql("""
            SELECT
                name,
                customer,
                outstanding_amount
            FROM `tabSales Invoice`
            WHERE docstatus = 1
            AND grandparent_name = %s
            ORDER BY name
        """, row.grandparent_name, as_dict=True)

        for inv in invoices:
            data.append({
                "grandparent_name": "",
                "sales_invoice": inv.name,
                "customer": inv.customer,
                "outstanding_amount": inv.outstanding_amount,
                "indent": 1
            })

    return data

