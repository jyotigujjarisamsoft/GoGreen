# Copyright (c) 2026, jyoti and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Tower"),
            "fieldname": "tower",
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

    # Apply tower filter if selected
    if filters and filters.get("tower"):
        conditions += " AND tower = %(tower)s"
        values["tower"] = filters.get("tower")

    # Get Tower totals
    tower_totals = frappe.db.sql(f"""
        SELECT
            tower,
            SUM(outstanding_amount) as total
        FROM `tabSales Invoice`
        WHERE docstatus = 1
        {conditions}
        GROUP BY tower
        ORDER BY tower
    """, values, as_dict=True)

    for tt in tower_totals:
        # Parent Row (Tower)
        data.append({
            "tower": tt.tower,
            "outstanding_amount": tt.total,
            "indent": 0
        })

        # Child Rows (Invoices under tower)
        invoices = frappe.db.sql("""
            SELECT
                name,
                customer,
                outstanding_amount
            FROM `tabSales Invoice`
            WHERE docstatus = 1
            AND tower = %s
            ORDER BY name
        """, tt.tower, as_dict=True)

        for inv in invoices:
            data.append({
                "tower": "",
                "sales_invoice": inv.name,
                "customer": inv.customer,
                "outstanding_amount": inv.outstanding_amount,
                "indent": 1
            })

    return data

