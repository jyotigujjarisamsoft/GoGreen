import frappe
from twilio.rest import Client

@frappe.whitelist(allow_guest=True)
def create_or_update_customer():
    try:
        import json
        from frappe.utils import cstr

        reqData = json.loads(frappe.request.data or "{}")

        # ==========================================================
        # FIELDS (ONLY WHAT YOU REQUESTED)
        # ==========================================================
        customer_id = reqData.get("customer_id")
        customer_name = cstr(reqData.get("customer_name")).strip()
        customer_type = reqData.get("type") or "Individual"

        custom_status = reqData.get("custom_status")
        custom_balance_updated_date = reqData.get("custom_balance_updated_date")
        custom_car_make = reqData.get("custom_car_make")
        custom_license_plate_no = reqData.get("custom_license_plate_no")
        custom_weekdays = reqData.get("custom_weekdays")
        custom_grandparent_name = reqData.get("custom_grandparent_name")
        custom_parent_name = reqData.get("custom_parent_name")
        custom_tower = reqData.get("custom_tower")
        custom_cluster = reqData.get("custom_cluster")
        custom_greatgrandparent_name = reqData.get("custom_greatgrandparent_name")
        custom_ledger_name = reqData.get("custom_ledger_name")
        custom_new_mobile_no = reqData.get("custom_new_mobile_no")
        custom_notes = reqData.get("custom_notes")
        custom_model = reqData.get("custom_model")
        custom_color = reqData.get("custom_color")
        custom_parking_bay = reqData.get("custom_parking_bay")
        custom_added_user = reqData.get("custom_added_user")
        custom_altered_date = reqData.get("custom_altered_date")
        custom_created_date = reqData.get("custom_created_date")
        custom_online_payment_status = reqData.get("custom_online_payment_status")
        custom_added_time = reqData.get("custom_added_time")
        custom_modified_time = reqData.get("custom_modified_time")
        custom_modified_user = reqData.get("custom_modified_user")
        custom_team_leader_name = reqData.get("custom_team_leader_name")
        custom_rate = reqData.get("custom_rate")
        custom_email = reqData.get("custom_email")
        custom_partial_start_date = reqData.get("custom_partial_start_date")
        custom_cleaner_name = reqData.get("custom_cleaner_name")
        custom_stop_reason = reqData.get("custom_stop_reason")
        custom_new_mobile_no_text = reqData.get("custom_new_mobile_no_text")
        custom_id = reqData.get("custom_id")
        custom_type_of_customer = reqData.get("custom_type_of_customer")

        # ==========================================================
        # UPDATE CUSTOMER
        # ==========================================================
        if customer_id:

            if not frappe.db.exists("Customer", customer_id):
                return {"status": "error", "message": "Customer not found"}

            doc = frappe.get_doc("Customer", customer_id)

            # Update only required fields
            doc.customer_name = customer_name
            doc.customer_type = customer_type
            doc.custom_status = custom_status
            doc.custom_balance_updated_date = custom_balance_updated_date
            doc.custom_car_make = custom_car_make
            doc.custom_license_plate_no = custom_license_plate_no
            doc.custom_weekdays = custom_weekdays
            doc.custom_grandparent_name = custom_grandparent_name
            doc.custom_parent_name = custom_parent_name
            doc.custom_tower = custom_tower
            doc.custom_cluster = custom_cluster
            doc.custom_greatgrandparent_name = custom_greatgrandparent_name
            doc.custom_ledger_name = custom_ledger_name
            doc.custom_new_mobile_no = custom_new_mobile_no
            doc.custom_notes = custom_notes
            doc.custom_model = custom_model
            doc.custom_color = custom_color
            doc.custom_parking_bay = custom_parking_bay
            doc.custom_added_user = custom_added_user
            doc.custom_altered_date = custom_altered_date
            doc.custom_created_date = custom_created_date
            doc.custom_online_payment_status = custom_online_payment_status
            doc.custom_added_time = custom_added_time
            doc.custom_modified_time = custom_modified_time
            doc.custom_modified_user = custom_modified_user
            doc.custom_team_leader_name = custom_team_leader_name
            doc.custom_rate = custom_rate
            doc.custom_email = custom_email
            doc.custom_partial_start_date = custom_partial_start_date
            doc.custom_cleaner_name = custom_cleaner_name
            doc.custom_stop_reason = custom_stop_reason
            doc.custom_new_mobile_no_text = custom_new_mobile_no_text
            doc.custom_id = custom_id
            doc.custom_type_of_customer = custom_type_of_customer

            doc.save(ignore_permissions=True)
            frappe.db.commit()

            return {
                "status": "success",
                "message": "Customer updated successfully",
                "customer_id": doc.name
            }

        # ==========================================================
        # CREATE NEW CUSTOMER
        # ==========================================================
        else:

            if not customer_name:
                return {"status": "error", "message": "Customer Name is required"}

            doc = frappe.get_doc({
                "doctype": "Customer",
                "customer_name": customer_name,
                "customer_type": customer_type,
                "custom_status": custom_status,
                "custom_balance_updated_date": custom_balance_updated_date,
                "custom_car_make": custom_car_make,
                "custom_license_plate_no": custom_license_plate_no,
                "custom_weekdays": custom_weekdays,
                "custom_grandparent_name": custom_grandparent_name,
                "custom_parent_name": custom_parent_name,
                "custom_tower": custom_tower,
                "custom_cluster": custom_cluster,
                "custom_greatgrandparent_name": custom_greatgrandparent_name,
                "custom_ledger_name": custom_ledger_name,
                "custom_new_mobile_no": custom_new_mobile_no,
                "custom_notes": custom_notes,
                "custom_model": custom_model,
                "custom_color": custom_color,
                "custom_parking_bay": custom_parking_bay,
                "custom_added_user": custom_added_user,
                "custom_altered_date": custom_altered_date,
                "custom_created_date": custom_created_date,
                "custom_online_payment_status": custom_online_payment_status,
                "custom_added_time": custom_added_time,
                "custom_modified_time": custom_modified_time,
                "custom_modified_user": custom_modified_user,
                "custom_team_leader_name": custom_team_leader_name,
                "custom_rate": custom_rate,
                "custom_email": custom_email,
                "custom_partial_start_date": custom_partial_start_date,
                "custom_cleaner_name": custom_cleaner_name,
                "custom_stop_reason": custom_stop_reason,
                "custom_new_mobile_no_text": custom_new_mobile_no_text,
                "custom_id": custom_id,
                "custom_type_of_customer": custom_type_of_customer,
            })

            doc.insert(ignore_permissions=True)
            frappe.db.commit()

            return {
                "status": "success",
                "message": "Customer created successfully",
                "customer_id": doc.name
            }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Customer API Error")
        return {
            "status": "error",
            "message": str(e)
        }
        
@frappe.whitelist(allow_guest=True)
def create_sales_invoice():
    import frappe
    import json

    try:
        data = json.loads(frappe.request.data or "{}")

        ledger_id = data.get("ledger_id")

        customer = frappe.db.get_value(
            "Customer",
            {"custom_id": ledger_id},
            "name"
        )

        invoice_no_old = data.get("invoice_no_old")
        posting_date = data.get("invoice_date")
        billed_period = data.get("billed_period")
        company = data.get("company")
        invoice_status = data.get("invoice_status")

        paid_amount = float(data.get("paid_amount", 0))
        paid_date = data.get("paid_date")

        items = data.get("items")

        if not customer or not company or not items:
            frappe.throw("customer, company and items are required")

        # -------------------------
        # Fetch Customer Dimensions
        # -------------------------
        customer_data = frappe.db.get_value(
            "Customer",
            customer,
            [
                "custom_cluster",
                "custom_tower",
                "custom_parent_name",
                "custom_grandparent_name",
                "custom_greatgrandparent_name"
            ],
            as_dict=True
        )

        # -------------------------
        # Create Sales Invoice
        # -------------------------
        si = frappe.new_doc("Sales Invoice")
        si.customer = customer
        si.company = company
        si.posting_date = posting_date
        si.custom_invoice_status = invoice_status
        si.custom_invoice_no_old = invoice_no_old
        si.custom_billed_period = billed_period

        # Sales Tax Template
        si.taxes_and_charges = "UAE VAT 5% - GG"

        si.append("taxes", {
            "charge_type": "On Net Total",
            "account_head": "VAT 5% - GG",
            "description": "VAT 5%",
            "rate": 5.0,
            "included_in_print_rate": 0
        })

        # -------------------------
        # Set Accounting Dimensions
        # -------------------------
        if customer_data:
            si.cluster = customer_data.get("custom_cluster")
            si.tower = customer_data.get("custom_tower")
            si.parent_name = customer_data.get("custom_parent_name")
            si.grandparent_name = customer_data.get("custom_grandparent_name")
            si.greatgrandparent_name = customer_data.get("custom_greatgrandparent_name")

        # -------------------------
        # Add Items
        # -------------------------
        for d in items:
            si.append("items", {
                "item_code": d.get("item_code"),
                "qty": d.get("qty", 1),
                "rate": d.get("rate", 0)
            })

        si.insert(ignore_permissions=True)
        si.submit()

        payment_entry_name = None

        # -------------------------
        # Create Payment Entry
        # -------------------------
        if paid_amount > 0:

            paid_to_account = frappe.db.get_value(
                "Company",
                company,
                "default_cash_account"
            )

            pe = frappe.new_doc("Payment Entry")
            pe.payment_type = "Receive"
            pe.party_type = "Customer"
            pe.party = customer
            pe.company = company

            pe.posting_date = paid_date if paid_date else posting_date
            pe.mode_of_payment = "Cash"

            pe.paid_to = paid_to_account

            pe.paid_amount = paid_amount
            pe.received_amount = paid_amount

            # Link Sales Invoice
            pe.append("references", {
                "reference_doctype": "Sales Invoice",
                "reference_name": si.name,
                "total_amount": si.grand_total,
                "allocated_amount": paid_amount
            })

            pe.insert(ignore_permissions=True)
            pe.submit()

            payment_entry_name = pe.name

        return {
            "status": "success",
            "sales_invoice": si.name,
            "payment_entry": payment_entry_name
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Create SI API")
        return {
            "status": "error",
            "message": str(e)
        }
