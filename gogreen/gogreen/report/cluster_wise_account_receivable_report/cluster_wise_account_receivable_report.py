import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Cluster"),
            "fieldname": "cluster",
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

    # Apply cluster filter if selected
    if filters and filters.get("cluster"):
        conditions += " AND cluster = %(cluster)s"
        values["cluster"] = filters.get("cluster")

    # Get Cluster totals
    cluster_totals = frappe.db.sql(f"""
        SELECT
            cluster,
            SUM(outstanding_amount) as total
        FROM `tabSales Invoice`
        WHERE docstatus = 1
        {conditions}
        GROUP BY cluster
        ORDER BY cluster
    """, values, as_dict=True)

    for ct in cluster_totals:
        # Parent Row (Cluster)
        data.append({
            "cluster": ct.cluster,
            "outstanding_amount": ct.total,
            "indent": 0
        })

        # Child Rows (Invoices under cluster)
        invoices = frappe.db.sql("""
            SELECT
                name,
                customer,
                outstanding_amount
            FROM `tabSales Invoice`
            WHERE docstatus = 1
            AND cluster = %s
            ORDER BY name
        """, ct.cluster, as_dict=True)

        for inv in invoices:
            data.append({
                "cluster": "",
                "sales_invoice": inv.name,
                "customer": inv.customer,
                "outstanding_amount": inv.outstanding_amount,
                "indent": 1
            })

    return data

