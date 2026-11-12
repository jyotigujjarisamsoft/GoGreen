import frappe
from frappe import _

def execute(filters=None):
    filters = filters or {}
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("GrandParent"),
            "fieldname": "grandparent",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Cluster"),
            "fieldname": "cluster",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "label": _("Tower"),
            "fieldname": "tower",
            "fieldtype": "Data",
            "width": 180,
        },
         {
            "label": _("Ledger Name"),
            "fieldname": "ledger_name",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "label": _("Flat No"),
            "fieldname": "flat_no",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("Billing Month"),
            "fieldname": "billing_month",
            "fieldtype": "Data", # Changed to Data to support text formatting
            "width": 110,
        },
        
        
       
        {
            "label": _("Outstanding (AED)"),
            "fieldname": "outstanding",
            "fieldtype": "Currency",
            "options": "AED",
            "width": 130,
        },
        {
            "label": _("Total Customer Outstanding (AED)"),
            "fieldname": "total_customer_outstanding",
            "fieldtype": "Currency",
            "options": "AED",
            "width": 200,
        },
    ]


def get_data(filters):
    conditions = ["si.docstatus = 1", "si.outstanding_amount > 0"]
    values = {}

    # --- Filters ---
    if filters.get("grandparent_name"):
        conditions.append("c.custom_grandparent_name = %(grandparent_name)s")
        values["grandparent_name"] = filters["grandparent_name"]

    if filters.get("cluster"):
        conditions.append("c.custom_cluster = %(cluster)s")
        values["cluster"] = filters["cluster"]

    if filters.get("tower"):
        conditions.append("c.custom_tower = %(tower)s")
        values["tower"] = filters["tower"]

    if filters.get("ledger_name"):
        # Using customer_name for the filter
        conditions.append("si.customer LIKE %(ledger_name)s")
        values["ledger_name"] = f"%{filters['ledger_name']}%"

    where_clause = "WHERE " + " AND ".join(conditions)

    rows = frappe.db.sql(
        f"""
        SELECT
            COALESCE(c.custom_grandparent_name, '') AS grandparent,
            COALESCE(c.custom_cluster, '') AS cluster,
            COALESCE(c.custom_tower, '') AS tower,
            COALESCE(c.custom_flat_no, '') AS flat_no,
            DATE_FORMAT(si.posting_date, '%%b %%Y') AS billing_month, 
            si.customer AS customer_id,
            si.customer_name AS ledger_name,
            si.outstanding_amount AS outstanding
        FROM `tabSales Invoice` si
        INNER JOIN `tabCustomer` c ON c.name = si.customer
        {where_clause}
        ORDER BY
            si.customer ASC,     -- Group by Customer first
            si.posting_date ASC,      -- Then sort by date
            si.name ASC
        """,
        values,
        as_dict=True,
    )

    if not rows:
        return []

    # --- Merge logic for Total Customer Outstanding ---
    ledger_totals = {}
    for r in rows:
        key = r.get("ledger_name")
        ledger_totals[key] = ledger_totals.get(key, 0) + (r.get("outstanding") or 0)

    # Find the last row for each customer
    last_index = {}
    for idx, r in enumerate(rows):
        last_index[r.get("ledger_name")] = idx

    data = []
    for idx, r in enumerate(rows):
        ledger = r.get("ledger_name")
        total = ledger_totals.get(ledger, 0)
        is_last = last_index.get(ledger) == idx

        data.append({
            "grandparent": r.get("grandparent"),
            "cluster": r.get("cluster"),
            "tower": r.get("tower"),
            "flat_no": r.get("flat_no"),
            "billing_month": r.get("billing_month"), # Will display as "Aug 2026"
            "ledger_name": ledger,
            "outstanding": r.get("outstanding"),
            "total_customer_outstanding": total if is_last else None,
        })

    return data
