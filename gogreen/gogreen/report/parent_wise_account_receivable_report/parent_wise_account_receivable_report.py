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
            "label": _("Parent Name"),
            "fieldname": "parent_name",
            "fieldtype": "Data",
            "width": 200
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

    # Apply Parent Name filter
    if filters and filters.get("parent_name"):
        conditions += " AND parent_name = %(parent_name)s"
        values["parent_name"] = filters.get("parent_name")

    # Get Parent totals
    parent_totals = frappe.db.sql(f"""
        SELECT
            parent_name,
            SUM(outstanding_amount) as total
        FROM `tabSales Invoice`
        WHERE docstatus = 1
        {conditions}
        GROUP BY parent_name
        ORDER BY parent_name
    """, values, as_dict=True)

    for pt in parent_totals:
        # Parent Row
        data.append({
            "parent_name": pt.parent_name,
            "outstanding_amount": pt.total,
            "indent": 0
        })

        # Child Rows (Invoices under Parent)
        invoices = frappe.db.sql("""
            SELECT
                name,
                customer,
                outstanding_amount
            FROM `tabSales Invoice`
            WHERE docstatus = 1
            AND parent_name = %s
            ORDER BY name
        """, pt.parent_name, as_dict=True)

        for inv in invoices:
            data.append({
                "parent_name": "",
                "sales_invoice": inv.name,
                "customer": inv.customer,
                "outstanding_amount": inv.outstanding_amount,
                "indent": 1
            })

    return data

