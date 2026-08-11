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
        #customer_id = reqData.get("customer_id")
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
        customer_id = frappe.db.get_value(
    "Customer",
    {"custom_id": custom_id},
    "name"
)

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
            doc.custom_license_plate = custom_license_plate_no
            doc.custom_weekdays = custom_weekdays
            doc.custom_grandparent_name = custom_grandparent_name
            doc.custom_parent_name = custom_parent_name
            doc.custom_tower_name = custom_tower
            doc.custom_cluster_name = custom_cluster
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
                "custom_license_plate": custom_license_plate_no,
                "custom_weekdays": custom_weekdays,
                "custom_grandparent_name": custom_grandparent_name,
                "custom_parent_name": custom_parent_name,
                "custom_tower_name": custom_tower,
                "custom_cluster_name": custom_cluster,
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
def old_create_sales_invoice():
    import frappe
    import json

    try:
        data = json.loads(frappe.request.data or "{}")

        ledger_id = data.get("ledger_id")
        zoho_invoice_id = data.get("zoho_invoice_id")

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
        si.custom_zoho_invoice_id = zoho_invoice_id

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

        

        return {
            "status": "success",
            "sales_invoice": si.name
           
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Create SI API")
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
        zoho_invoice_id = data.get("zoho_invoice_id")
        custom_invoice_no = data.get("invoice_no")
        custom_zoho_invoice_no = data.get("zoho_invoice_no")

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
        si.custom_zoho_invoice_no = custom_zoho_invoice_no
        si.custom_invoice_no = custom_invoice_no

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

        

        return {
            "status": "success",
            "sales_invoice": si.name
           
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Create SI API")
        return {
            "status": "error",
            "message": str(e)
        }        
@frappe.whitelist(allow_guest=True)
def create_payment_entry():
    import frappe
    import json
    from frappe.utils import flt, getdate

    try:

        # ------------------------------------------------
        # IMPORTANT
        # ------------------------------------------------
        frappe.set_user("Administrator")

        # ------------------------------------------------
        # Read Payload
        # ------------------------------------------------
        data = json.loads(frappe.request.data or "{}")

        ledger_id = data.get("ledger_id")

        customer = frappe.db.get_value(
            "Customer",
            {"custom_id": ledger_id},
            "name"
        )

        if not customer:
            return {
                "status": "error",
                "message": f"Customer not found for ledger_id: {ledger_id}"
            }

        # ------------------------------------------------
        # Fetch Customer Master Details
        # ------------------------------------------------
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

        company = data.get("company")
        posting_date = data.get("posting_date")

        invoices = data.get("sales_invoices", [])

        if not invoices:
            return {
                "status": "error",
                "message": "sales_invoices array is required"
            }

        # ------------------------------------------------
        # Get Company Default Cash Account
        # ------------------------------------------------
        paid_to_account = frappe.db.get_value(
            "Company",
            company,
            "default_cash_account"
        )

        if not paid_to_account:
            return {
                "status": "error",
                "message": "Default Cash Account not found in Company"
            }

        # ------------------------------------------------
        # Currency Details
        # ------------------------------------------------
        account_currency = frappe.db.get_value(
            "Account",
            paid_to_account,
            "account_currency"
        )

        company_currency = frappe.db.get_value(
            "Company",
            company,
            "default_currency"
        )

        # ------------------------------------------------
        # Create Payment Entry
        # ------------------------------------------------
        pe = frappe.new_doc("Payment Entry")

        pe.flags.ignore_permissions = True
        pe.flags.ignore_mandatory = True

        pe.payment_type = "Receive"
        pe.party_type = "Customer"
        pe.party = customer
        pe.company = company

        pe.posting_date = getdate(posting_date)

        pe.mode_of_payment = data.get("mode_of_payment") or "Cash"

        pe.paid_to = paid_to_account

        pe.paid_to_account_currency = account_currency
        pe.target_exchange_rate = 1

        # ------------------------------------------------
        # Autofill Custom Fields from Customer
        # ------------------------------------------------
        if customer_data:

            pe.cluster = customer_data.get(
                "custom_cluster"
            )

            pe.tower = customer_data.get(
                "custom_tower"
            )

            pe.parent_name = customer_data.get(
                "custom_parent_name"
            )

            pe.grandparent_name = customer_data.get(
                "custom_grandparent_name"
            )

            pe.greatgrandparent_name = customer_data.get(
                "custom_greatgrandparent_name"
            )

        total_paid_amount = 0
        receivable_account = None

        # ------------------------------------------------
        # Process Sales Invoices
        # ------------------------------------------------
        for inv in invoices:

            zoho_invoice_id = inv.get(
                "custom_zoho_invoice_no"
            )

            allocated_amount = flt(
                inv.get("allocated_amount")
            )

            if not zoho_invoice_id:
                continue

            # ------------------------------------------------
            # Fetch Sales Invoice
            # ------------------------------------------------
            sales_invoice = frappe.db.get_value(
                "Sales Invoice",
                {
                    "custom_zoho_invoice_no": zoho_invoice_id
                },
                "name"
            )

            if not sales_invoice:
                frappe.throw(
                    f"Sales Invoice not found for Zoho Invoice ID: {zoho_invoice_id}"
                )

            si = frappe.get_doc(
                "Sales Invoice",
                sales_invoice
            )

            if si.docstatus != 1:
                frappe.throw(
                    f"Sales Invoice {sales_invoice} is not submitted"
                )

            # ------------------------------------------------
            # Receivable Account
            # ------------------------------------------------
            if not receivable_account:
                receivable_account = si.debit_to

            total_paid_amount += allocated_amount

            # ------------------------------------------------
            # Add References
            # ------------------------------------------------
            pe.append("references", {
                "reference_doctype": "Sales Invoice",
                "reference_name": si.name,
                "due_date": si.due_date,
                "total_amount": si.grand_total,
                "outstanding_amount": si.outstanding_amount,
                "allocated_amount": allocated_amount
            })

        # ------------------------------------------------
        # Source Account
        # ------------------------------------------------
        pe.paid_from = receivable_account

        pe.paid_from_account_currency = company_currency

        pe.source_exchange_rate = 1

        # ------------------------------------------------
        # Amounts
        # ------------------------------------------------
        pe.paid_amount = total_paid_amount
        pe.received_amount = total_paid_amount
        pe.reference_no="AUTO-REF"
        pe.reference_date=getdate(posting_date)

        # ------------------------------------------------
        # SAVE ONLY
        # ------------------------------------------------
        pe.insert(ignore_permissions=True)

        frappe.db.commit()

        return {
            "status": "success",
            "payment_entry": pe.name,
            "customer": customer,
            "docstatus": pe.docstatus,
            "total_paid_amount": total_paid_amount
        }

    except Exception as e:

        frappe.db.rollback()

        frappe.log_error(
            frappe.get_traceback(),
            "Create Payment Entry API"
        )

        return {
            "status": "error",
            "message": str(e)
        }
        
@frappe.whitelist(allow_guest=True)
def update_sales_invoice():
    import frappe
    import json

    try:

        frappe.set_user("Administrator")

        # =====================================================
        # READ REQUEST DATA
        # =====================================================
        data = json.loads(frappe.request.data or "{}")

        ledger_id = data.get("ledger_id")
        zoho_invoice_id = data.get("zoho_invoice_id")

        custom_invoice_no = data.get("invoice_no")
        custom_zoho_invoice_no = data.get("zoho_invoice_no")

        invoice_no_old = data.get("invoice_no_old")

        posting_date = data.get("invoice_date")
        billed_period = data.get("billed_period")

        company = data.get("company")
        invoice_status = data.get("invoice_status")

        items = data.get("items") or []

        # =====================================================
        # VALIDATIONS
        # =====================================================
        if not ledger_id:
            frappe.throw("ledger_id is required")

        if not company:
            frappe.throw("company is required")

        if not items:
            frappe.throw("items are required")

        # =====================================================
        # GET CUSTOMER
        # =====================================================
        customer = frappe.db.get_value(
            "Customer",
            {"custom_id": ledger_id},
            "name"
        )

        if not customer:
            frappe.throw(
                f"Customer not found for ledger_id: {ledger_id}"
            )

        # =====================================================
        # FETCH CUSTOMER DIMENSIONS
        # =====================================================
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

        # =====================================================
        # CHECK EXISTING SUBMITTED INVOICE
        # =====================================================
        existing_si_name = frappe.db.get_value(
            "Sales Invoice",
            {
                "custom_zoho_invoice_no": zoho_invoice_id,
                "docstatus": 1
            },
            "name"
        )

        amended_from = None

        # =====================================================
        # CANCEL OLD INVOICE
        # =====================================================
        if existing_si_name:

            old_si = frappe.get_doc(
                "Sales Invoice",
                existing_si_name
            )

            old_si.cancel()

            amended_from = old_si.name

        # =====================================================
        # CREATE NEW AMENDED INVOICE
        # =====================================================
        si = frappe.new_doc("Sales Invoice")

        si.flags.ignore_permissions = True

        # IMPORTANT
        if amended_from:
            si.amended_from = amended_from

        # =====================================================
        # COMMON FIELDS
        # =====================================================
        si.customer = customer
        si.company = company

        si.posting_date = posting_date

        si.custom_invoice_status = invoice_status
        si.custom_invoice_no_old = invoice_no_old

        si.custom_billed_period = billed_period

        si.custom_zoho_invoice_no = custom_zoho_invoice_no
        si.custom_invoice_no = custom_invoice_no

        #si.custom_zoho_invoice_id = zoho_invoice_id

        # =====================================================
        # TAX TEMPLATE
        # =====================================================
        si.taxes_and_charges = "UAE VAT 5% - GG"

        si.append("taxes", {
            "charge_type": "On Net Total",
            "account_head": "VAT 5% - GG",
            "description": "VAT 5%",
            "rate": 5.0,
            "included_in_print_rate": 0
        })

        # =====================================================
        # ACCOUNTING DIMENSIONS
        # =====================================================
        if customer_data:

            si.cluster = customer_data.get(
                "custom_cluster"
            )

            si.tower = customer_data.get(
                "custom_tower"
            )

            si.parent_name = customer_data.get(
                "custom_parent_name"
            )

            si.grandparent_name = customer_data.get(
                "custom_grandparent_name"
            )

            si.greatgrandparent_name = customer_data.get(
                "custom_greatgrandparent_name"
            )

        # =====================================================
        # ADD ITEMS
        # =====================================================
        for d in items:

            si.append("items", {
                "item_code": d.get("item_code"),
                "qty": d.get("qty", 1),
                "rate": d.get("rate", 0)
            })

        # =====================================================
        # SAVE & SUBMIT
        # =====================================================
        si.insert(ignore_permissions=True)

        si.submit()

        frappe.db.commit()

        return {
            "status": "success",
            "sales_invoice": si.name,
            "amended_from": amended_from
        }

    except Exception as e:

        frappe.db.rollback()

        frappe.log_error(
            frappe.get_traceback(),
            "Update Sales Invoice API"
        )

        return {
            "status": "error",
            "message": str(e)
        }
        
import frappe
from frappe import _
from frappe.utils import flt, today
import frappe
import json

@frappe.whitelist(allow_guest=True)
def stripe_webhook():

    payload = frappe.request.get_json()

    frappe.log_error(
        json.dumps(payload, indent=4),
        "Stripe Webhook"
    )

    if not payload:
        frappe.throw(_("Invalid Stripe Payload"))

    event_type = payload.get("type")

    data = payload.get("data") or {}
    stripe_data = data.get("object") or {}

    # Process successful charge
    if event_type == "charge.succeeded":
    	frappe.set_user("Administrator")

        return create_documents_from_stripe_payload(
            stripe_data
        )

    # Ignore other events but return success
    return {
        "success": True,
        "message": f"Event {event_type} received"
    }


@frappe.whitelist(allow_guest=True)
def create_documents_from_stripe_payload(payload=None):

    # -----------------------------------------
    # Get Payload
    # -----------------------------------------

    if not payload:
        payload = frappe.request.get_json()

    if not payload:
        frappe.throw(_("Invalid Payload"))

    # If payload is received as JSON string
    if isinstance(payload, str):
        payload = frappe.parse_json(payload)

    # -----------------------------------------
    # Detect Stripe Object
    # -----------------------------------------

    stripe_object = payload.get("object")

    # -----------------------------------------
    # Variables
    # -----------------------------------------

    customer_name = None
    email = None
    phone = None
    amount = 0
    currency = "AED"
    stripe_payment_id = None

    # -----------------------------------------
    # CHARGE PAYLOAD
    # -----------------------------------------

    if stripe_object == "charge":

        # Payment must be successful
        if payload.get("status") != "succeeded":
            frappe.throw(_("Payment not successful"))

        if not payload.get("paid"):
            frappe.throw(_("Payment not successful"))

        # Amount
        amount = flt(payload.get("amount")) / 100

        # Currency
        currency = (
            payload.get("currency") or "aed"
        ).upper()

        # Stripe Charge ID
        stripe_payment_id = payload.get("id")

        # Customer details
        billing_details = payload.get("billing_details") or {}
        source = payload.get("source") or {}

        customer_name = (
            billing_details.get("name")
            or source.get("name")
            or "Stripe Customer"
        )

        email = (
            billing_details.get("email")
            or payload.get("receipt_email")
            or source.get("email")
        )

        phone = (
            billing_details.get("phone")
            or source.get("phone")
        )

    # -----------------------------------------
    # CHECKOUT SESSION PAYLOAD
    # -----------------------------------------

    elif stripe_object == "checkout.session":

        # Payment must be successful
        if payload.get("status") != "complete":
            frappe.throw(_("Payment not successful"))

        if payload.get("payment_status") != "paid":
            frappe.throw(_("Payment not successful"))

        # Payment Intent
        payment_intent = payload.get("payment_intent") or {}

        if isinstance(payment_intent, dict):

            # Payment Intent status
            if payment_intent.get("status") != "succeeded":
                frappe.throw(
                    _("Stripe Payment Intent is not successful")
                )

            amount = flt(
                payment_intent.get("amount", 0)
            ) / 100

            currency = (
                payment_intent.get("currency")
                or payload.get("currency")
                or "aed"
            ).upper()

            stripe_payment_id = payment_intent.get("id")

        else:

            stripe_payment_id = payment_intent

            # Fallback amount from session
            amount = flt(
                payload.get("amount_total", 0)
            ) / 100

            currency = (
                payload.get("currency")
                or "aed"
            ).upper()

        # Customer details
        customer_details = (
            payload.get("customer_details") or {}
        )

        customer_name = (
            customer_details.get("name")
            or "Stripe Customer"
        )

        email = customer_details.get("email")
        phone = customer_details.get("phone")

    # -----------------------------------------
    # Unsupported Stripe Object
    # -----------------------------------------

    else:

        frappe.throw(
            _("Unsupported Stripe object: {0}").format(
                stripe_object
            )
        )

    # -----------------------------------------
    # Basic Validation
    # -----------------------------------------

    if not stripe_payment_id:
        frappe.throw(_("Stripe payment ID not found"))

    if amount <= 0:
        frappe.throw(_("Invalid payment amount"))

    # -----------------------------------------
    # Company
    # -----------------------------------------

    company = "Go Green Cleaning Solution"

    # -----------------------------------------
    # Check Duplicate Payment
    # -----------------------------------------

    if frappe.db.exists(
        "Payment Entry",
        {"reference_no": stripe_payment_id}
    ):
        return {
            "message": "Payment already imported"
        }

    # -----------------------------------------
    # Customer
    # -----------------------------------------

    customer = None

    if email:

        customer = frappe.db.get_value(
            "Customer",
            {"custom_customer_email_id": email},
            "name"
        )

    if not customer:

        customer_doc = frappe.get_doc({

            "doctype": "Customer",

            "customer_name": customer_name,

            "customer_type": "Individual",

            "custom_phone_no": phone,

            "custom_customer_email_id": email
        })

        customer_doc.insert(
            ignore_permissions=True
        )

        customer = customer_doc.name

    # -----------------------------------------
    # Sales Invoice
    # -----------------------------------------

    invoice = frappe.get_doc({

        "doctype": "Sales Invoice",

        "company": company,

        "customer": customer,

        "currency": currency,

        "disable_rounded_total": 1,

        "items": [
            {
                "item_code": "Go Green Service",
                "qty": 1,
                "rate": amount
            }
        ]
    })

    # -----------------------------------------
    # VAT
    # -----------------------------------------

    invoice.taxes_and_charges = "UAE VAT 5% - GG"

    invoice.append("taxes", {

        "charge_type": "On Net Total",

        "account_head": "VAT 5% - GG",

        "description": "VAT 5%",

        "rate": 5
    })

    # -----------------------------------------
    # Insert & Submit Invoice
    # -----------------------------------------

    invoice.insert(
        ignore_permissions=True
    )

    invoice.submit()

    # -----------------------------------------
    # Payment Entry
    # -----------------------------------------

    payment = frappe.get_doc({

        "doctype": "Payment Entry",

        "payment_type": "Receive",

        "company": company,

        "party_type": "Customer",

        "party": customer,

        "mode_of_payment": "Stripe",

        "paid_amount": invoice.grand_total,

        "received_amount": invoice.grand_total,

        "reference_no": stripe_payment_id,

        "reference_date": today(),

        "references": [
            {
                "reference_doctype": "Sales Invoice",

                "reference_name": invoice.name,

                "allocated_amount": invoice.grand_total
            }
        ]
    })

    # -----------------------------------------
    # Exchange Rate
    # -----------------------------------------

    payment.target_exchange_rate = 1
    payment.source_exchange_rate = 1

    # -----------------------------------------
    # Paid To Account
    # -----------------------------------------

    payment.paid_to = "Stripe Clearing - GG"

    # -----------------------------------------
    # Insert & Submit Payment
    # -----------------------------------------

    payment.insert(
        ignore_permissions=True
    )

    payment.submit()

    # -----------------------------------------
    # Commit
    # -----------------------------------------

    frappe.db.commit()

    # -----------------------------------------
    # Response
    # -----------------------------------------

    return {

        "success": True,

        "stripe_object": stripe_object,

        "stripe_payment_id": stripe_payment_id,

        "customer": customer,

        "sales_invoice": invoice.name,

        "payment_entry": payment.name,

        "amount": amount,

        "currency": currency
    }


@frappe.whitelist(allow_guest=True)
def old_create_documents_from_stripe_payload(payload):

    payload = frappe.request.get_json()

    if not payload:
        frappe.throw(_("Invalid Payload"))

    if payload.get("status") != "succeeded":
        frappe.throw(_("Payment not successful"))

    source = payload.get("source", {})

    customer_name = source.get("customer") or source.get("name")
    email = source.get("email")
    phone = source.get("phone")

    amount = flt(payload.get("amount")) / 100
    stripe_charge_id = payload.get("id")
    currency = "AED"

    company = "Go Green Cleaning Solution"

    # -----------------------------------------
    # Check duplicate payment
    # -----------------------------------------

    if frappe.db.exists(
        "Payment Entry",
        {"reference_no": stripe_charge_id}
    ):
        return {
            "message": "Payment already imported"
        }

    # -----------------------------------------
    # Customer
    # -----------------------------------------

    customer = None

    if email:
        customer = frappe.db.get_value(
            "Customer",
            {"email_id": email},
            "name"
        )

    if not customer:

        customer_doc = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": customer_name,
            "customer_type": "Individual",
            "custom_phone_no": email,
            "custom_customer_email_id": phone
        })

        customer_doc.insert(ignore_permissions=True)

        customer = customer_doc.name

    # -----------------------------------------
    # Sales Invoice
    # -----------------------------------------

    invoice = frappe.get_doc({

        "doctype": "Sales Invoice",

        "company": company,

        "customer": customer,

        "currency": currency,

        "disable_rounded_total": 1,
        

        

        "items": [
            {
                "item_code": "Go Green Service",
                "qty": 1,
                "rate": amount
            }
        ]
    })
    invoice.taxes_and_charges = "UAE VAT 5% - GG"
    invoice.append("taxes", {
    "charge_type": "On Net Total",
    "account_head": "VAT 5% - GG",
    "description": "VAT 5%",
    "rate": 5
})

    invoice.insert(ignore_permissions=True)
    invoice.submit()

    # -----------------------------------------
    # Payment Entry
    # -----------------------------------------

    payment = frappe.get_doc({

        "doctype": "Payment Entry",

        "payment_type": "Receive",

        "company": company,

        "party_type": "Customer",

        "party": customer,

        "mode_of_payment": "Stripe",

        "paid_amount": invoice.grand_total,

        "received_amount": invoice.grand_total,

        "reference_no": stripe_charge_id,

        "reference_date": today(),

        "references": [
            {
                "reference_doctype": "Sales Invoice",
                "reference_name": invoice.name,
                "allocated_amount": invoice.grand_total
            }
        ]
    })
    payment.target_exchange_rate = 1
    payment.source_exchange_rate = 1
    payment.paid_to = "Stripe Clearing - GG"

    payment.insert(ignore_permissions=True)
    payment.submit()

    frappe.db.commit()

    return {
        "customer": customer,
        "sales_invoice": invoice.name,
        "payment_entry": payment.name
    }
@frappe.whitelist(allow_guest=True)
def create_documents_from_stripe():

    payload = frappe.request.get_json()

    if not payload:
        frappe.throw(_("Invalid Payload"))

    if payload.get("status") != "succeeded":
        frappe.throw(_("Payment not successful"))

    source = payload.get("source", {})

    customer_name = source.get("customer") or source.get("name")
    email = source.get("email")
    phone = source.get("phone")

    amount = flt(payload.get("amount")) / 100
    stripe_charge_id = payload.get("id")
    currency = "AED"

    company = "Go Green Cleaning Solution"

    # -----------------------------------------
    # Check duplicate payment
    # -----------------------------------------

    if frappe.db.exists(
        "Payment Entry",
        {"reference_no": stripe_charge_id}
    ):
        return {
            "message": "Payment already imported"
        }

    # -----------------------------------------
    # Customer
    # -----------------------------------------

    customer = None

    if email:
        customer = frappe.db.get_value(
            "Customer",
            {"email_id": email},
            "name"
        )

    if not customer:

        customer_doc = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": customer_name,
            "customer_group": "All Customer Groups",
            "territory": "All Territories",
            "customer_type": "Individual",
            "email_id": email,
            "mobile_no": phone
        })

        customer_doc.insert(ignore_permissions=True)

        customer = customer_doc.name

    # -----------------------------------------
    # Sales Invoice
    # -----------------------------------------

    invoice = frappe.get_doc({

        "doctype": "Sales Invoice",

        "company": company,

        "customer": customer,

        "currency": currency,

        "disable_rounded_total": 1,
        

        

        "items": [
            {
                "item_code": "Go Green Service",
                "qty": 1,
                "rate": amount
            }
        ]
    })
    invoice.taxes_and_charges = "UAE VAT 5% - GG"
    invoice.append("taxes", {
    "charge_type": "On Net Total",
    "account_head": "VAT 5% - GG",
    "description": "VAT 5%",
    "rate": 5
})

    invoice.insert(ignore_permissions=True)
    invoice.submit()

    # -----------------------------------------
    # Payment Entry
    # -----------------------------------------

    payment = frappe.get_doc({

        "doctype": "Payment Entry",

        "payment_type": "Receive",

        "company": company,

        "party_type": "Customer",

        "party": customer,

        "mode_of_payment": "Stripe",

        "paid_amount": invoice.grand_total,

        "received_amount": invoice.grand_total,

        "reference_no": stripe_charge_id,

        "reference_date": today(),

        "references": [
            {
                "reference_doctype": "Sales Invoice",
                "reference_name": invoice.name,
                "allocated_amount": invoice.grand_total
            }
        ]
    })
    payment.target_exchange_rate = 1
    payment.source_exchange_rate = 1
    payment.paid_to = "Stripe Clearing - GG"

    payment.insert(ignore_permissions=True)
    payment.submit()

    frappe.db.commit()

    return {
        "customer": customer,
        "sales_invoice": invoice.name,
        "payment_entry": payment.name
    }
