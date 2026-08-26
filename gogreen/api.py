import frappe
from twilio.rest import Client
import frappe
import json

from frappe import _
from frappe.utils import flt, today

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
@frappe.whitelist(allow_guest=True)
def stripe_webhook():

    # -----------------------------------------
    # Get Stripe Request Body
    # -----------------------------------------

    payload = frappe.request.get_json()

    frappe.log_error(
        json.dumps(payload, indent=4),
        "Stripe Webhook"
    )

    if not payload:
        frappe.throw(_("Invalid Stripe Payload"))

    # -----------------------------------------
    # Get Event Type
    # -----------------------------------------

    event_type = payload.get("type")

    # -----------------------------------------
    # Get Stripe Object
    # -----------------------------------------

    data = payload.get("data") or {}
    stripe_data = data.get("object") or {}

    # -----------------------------------------
    # Process Checkout Session Completed
    # -----------------------------------------

    if event_type == "checkout.session.completed":

        frappe.set_user("Administrator")

        return create_documents_from_stripe_payload(
            payload=stripe_data
        )

    # -----------------------------------------
    # Ignore Other Events
    # -----------------------------------------

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

    car_plate = None
    tower_name = None
    flat_no = None

    amount = 0
    currency = "AED"

    stripe_payment_id = None

    # -----------------------------------------
    # CHECKOUT SESSION PAYLOAD
    # -----------------------------------------

    if stripe_object == "checkout.session":

        # -----------------------------------------
        # Payment Validation
        # -----------------------------------------

        if payload.get("status") != "complete":
            frappe.throw(_("Payment not successful"))

        if payload.get("payment_status") != "paid":
            frappe.throw(_("Payment not successful"))

        # -----------------------------------------
        # Payment Intent
        # -----------------------------------------

        stripe_payment_id = payload.get("payment_intent")

        if not stripe_payment_id:
            frappe.throw(_("Stripe Payment Intent not found"))

        # -----------------------------------------
        # Amount
        # -----------------------------------------

        amount = flt(payload.get("amount_total", 0)) / 100

        if amount <= 0:
            frappe.throw(_("Invalid payment amount"))

        # -----------------------------------------
        # Currency
        # -----------------------------------------

        currency = (
            payload.get("currency") or "aed"
        ).upper()

        # -----------------------------------------
        # Customer Details
        # -----------------------------------------

        customer_details = payload.get("customer_details") or {}

        email = customer_details.get("email")
        customer_name = customer_details.get("name")
        phone = customer_details.get("phone")

        # -----------------------------------------
        # Stripe Custom Fields
        # -----------------------------------------

        custom_fields = payload.get("custom_fields") or []

        for field in custom_fields:

            field_key = field.get("key")

            text_data = field.get("text") or {}

            field_value = text_data.get("value")

            # -------------------------------------
            # Car Plate
            # -------------------------------------

            if field_key == "carplate":
                car_plate = field_value

            # -------------------------------------
            # Tower Name
            # -------------------------------------

            elif field_key == "towername":
                tower_name = field_value

            # -------------------------------------
            # Flat No
            # -------------------------------------

            elif field_key == "flatno":
                flat_no = field_value

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

    existing_payment = frappe.db.exists(
        "Payment Entry",
        {
            "reference_no": stripe_payment_id
        }
    )

    if existing_payment:

        return {
            "success": True,
            "message": "Payment already imported",
            "stripe_payment_id": stripe_payment_id,
            "payment_entry": existing_payment
        }

    # -----------------------------------------
    # Find Customer By Email
    # -----------------------------------------

    customer = None

    if email:

        customer = frappe.db.get_value(
            "Customer",
            {
                "custom_customer_email_id": email
            },
            "name"
        )

    # -----------------------------------------
    # Create Customer
    # -----------------------------------------

    if not customer:

        # -----------------------------------------
        # Customer Validation
        # -----------------------------------------

        if not customer_name:
            customer_name = email or "Stripe Customer"

        if not car_plate:
            car_plate = "NO-PLATE"

        # -----------------------------------------
        # Create Customer
        # -----------------------------------------

        customer_doc = frappe.get_doc({
            "doctype": "Customer",

            "customer_name": customer_name,

            "customer_type": "Individual",

            "custom_phone_no": phone,

            "custom_customer_email_id": email,

            "custom_license_plate": car_plate,

            "custom_car_plate": car_plate,

            "custom_created_by_stripe": 1,

            "custom_stripe_tower_name": tower_name,

            "custom_flat_no": flat_no
        })

        customer_doc.insert(
            ignore_permissions=True
        )

        customer = customer_doc.name

    # -----------------------------------------
    # Update Existing Customer
    # -----------------------------------------

    else:

        customer_doc = frappe.get_doc(
            "Customer",
            customer
        )

        customer_doc.custom_created_by_stripe = 1

        if phone:
            customer_doc.custom_phone_no = phone

        if car_plate:
            customer_doc.custom_license_plate = car_plate
            customer_doc.custom_car_plate = car_plate

        if tower_name:
            customer_doc.custom_stripe_tower_name = tower_name

        if flat_no:
            customer_doc.custom_flat_no = flat_no

        customer_doc.save(
            ignore_permissions=True
        )

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

        "rate": 5,

        "included_in_print_rate": 1
    })

    # -----------------------------------------
    # Insert Invoice
    # -----------------------------------------

    invoice.insert(
        ignore_permissions=True
    )

    # -----------------------------------------
    # Submit Invoice
    # -----------------------------------------

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
    # Insert Payment
    # -----------------------------------------

    payment.insert(
        ignore_permissions=True
    )

    # -----------------------------------------
    # Submit Payment
    # -----------------------------------------

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

        "customer_name": customer_name,

        "email": email,

        "phone": phone,

        "car_plate": car_plate,

        "tower_name": tower_name,

        "flat_no": flat_no,

        "sales_invoice": invoice.name,

        "payment_entry": payment.name,

        "amount": amount,

        "currency": currency
    }
@frappe.whitelist(allow_guest=True)
def oldd_create_documents_from_stripe_payload(payload):

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
    
import frappe
from frappe import _


# =========================================================
# START MONTHLY SALES INVOICE CREATION
# =========================================================

@frappe.whitelist()
def new_generate_monthly_sales_invoices(docname):

    """
    This API only starts the background job.

    It does NOT create invoices inside the web request.
    """

    if not frappe.db.exists(
        "Monthly Invoice Creation",
        docname
    ):
        frappe.throw(
            _("Monthly Invoice Creation {0} does not exist.")
            .format(docname)
        )

    # -----------------------------------------------------
    # CHECK CURRENT STATUS
    # -----------------------------------------------------

    current_status = frappe.db.get_value(
        "Monthly Invoice Creation",
        docname,
        "status"
    )

    if current_status == "Processing":
        return {
            "status": "already_processing",
            "message": "Invoice creation is already running."
        }

    # -----------------------------------------------------
    # SET STATUS
    # -----------------------------------------------------

    frappe.db.set_value(
        "Monthly Invoice Creation",
        docname,
        "status",
        "Processing"
    )

    frappe.db.commit()

    # -----------------------------------------------------
    # QUEUE BACKGROUND JOB
    # -----------------------------------------------------

    frappe.enqueue(
        "gogreen.api.create_monthly_sales_invoices_background",
        queue="long",
        timeout=3600,
        is_async=True,
        docname=docname
    )


    return {
        "status": "queued",
        "message": (
            "Sales Invoice creation has been "
            "started in background."
        )
    }


# =========================================================
# BACKGROUND JOB
# =========================================================

def create_monthly_sales_invoices_background(docname):

    print("=" * 100)
    print("STARTING MONTHLY SALES INVOICE CREATION")
    print("Document:", docname)
    print("=" * 100)

    created = 0
    skipped = 0
    failed = 0

    try:

        # -------------------------------------------------
        # GET MONTHLY INVOICE CREATION DOCUMENT
        # -------------------------------------------------

        doc = frappe.get_doc(
            "Monthly Invoice Creation",
            docname
        )

        print(
            "Customer Type:",
            doc.customer_type
        )

        print(
            "Billed Period:",
            doc.billed_period
        )

        print(
            "Posting Date:",
            doc.date
        )

        # -------------------------------------------------
        # GET CUSTOMERS
        # -------------------------------------------------

        customers = frappe.get_all(
            "Customer",
            filters={
                "custom_customer_typee":
                    doc.customer_type
            },
            fields=[
                "name",
                "customer_name",
                "custom_rate",
                "custom_cluster",
                "custom_tower",
                "custom_parent_name",
                "custom_grandparent_name",
                "custom_greatgrandparent_name"
            ],
            order_by="name asc"
        )

        total_customers = len(customers)

        print(
            "Total Customers:",
            total_customers
        )

        # -------------------------------------------------
        # PROCESS ONE CUSTOMER AT A TIME
        # -------------------------------------------------

        for index, customer in enumerate(
            customers,
            start=1
        ):

            print("")
            print("=" * 80)
            print(
                f"Processing Customer "
                f"{index}/{total_customers}"
            )
            print(
                f"Customer Name : {customer.name}"
            )
            print(
                f"Customer       : "
                f"{customer.customer_name}"
            )
            print(
                f"Rate           : "
                f"{customer.custom_rate}"
            )
            print("=" * 80)

            try:

                # =========================================
                # CHECK EXISTING SALES INVOICE
                # =========================================

                existing_invoice = frappe.db.exists(
                    "Sales Invoice",
                    {
                        "customer": customer.name,
                        "custom_billed_period":
                            doc.billed_period,
                        "docstatus": ["!=", 2]
                    }
                )

                if existing_invoice:

                    print(
                        "Invoice already exists:",
                        existing_invoice
                    )

                    skipped += 1

                    continue

                # =========================================
                # VALIDATE RATE
                # =========================================

                rate = float(
                    customer.custom_rate or 1
                )

                if rate <= 0:

                    raise Exception(
                        f"Invalid rate for customer "
                        f"{customer.name}: {rate}"
                    )

                # =========================================
                # CREATE SALES INVOICE
                # =========================================

                print(
                    "Creating Sales Invoice..."
                )

                si = frappe.new_doc(
                    "Sales Invoice"
                )

                # -----------------------------------------
                # COMPANY
                # -----------------------------------------

                si.company = "Go Green Cleaning Solution"

                # -----------------------------------------
                # CURRENCY
                # -----------------------------------------

                # Keeping your existing currency.
                #
                # If your invoice should actually be AED,
                # change this to:
                #
                # si.currency = "AED"

                si.currency = "AED"

                # -----------------------------------------
                # CUSTOMER
                # -----------------------------------------

                si.customer = customer.name

                si.posting_date = doc.date

                # =========================================
                # CUSTOM FIELDS
                # =========================================

                si.custom_billed_period = (
                    doc.billed_period
                )

                si.cluster = (
                    customer.custom_cluster
                )

                si.tower = (
                    customer.custom_tower
                )

                si.parent_name = (
                    customer.custom_parent_name
                )

                si.grandparent_name = (
                    customer.custom_grandparent_name
                )

                si.greatgrandparent_name = (
                    customer.custom_greatgrandparent_name
                )

                si.disable_rounded_total = 1

                # =========================================
                # TAX
                # =========================================

                si.taxes_and_charges = (
                    "UAE VAT 5% - GG"
                )

                si.append("taxes", {
		    "charge_type": "On Net Total",
		    "account_head": "VAT 5% - GG",
		    "description": "VAT 5%",
		    "rate": 5
		})

                # =========================================
                # ITEM
                # =========================================

                si.append(
                    "items",
                    {
                        "item_code":
                            "Go Green Service",

                        "qty":
                            1,

                        "rate":
                            rate
                    }
                )

                print(
                    "Item added successfully."
                )

                # =========================================
                # INSERT
                # =========================================

                print(
                    "Inserting Sales Invoice..."
                )

                si.insert(
                    ignore_permissions=True
                )

                print(
                    "Invoice inserted:",
                    si.name
                )

                # =========================================
                # CALCULATE TAXES AND TOTALS
                # =========================================

                print(
                    "Calculating taxes and totals..."
                )

                si.calculate_taxes_and_totals()

                print(
                    "Net Total:",
                    si.net_total
                )

                print(
                    "Tax Total:",
                    si.total_taxes_and_charges
                )

                print(
                    "Grand Total:",
                    si.grand_total
                )

                # =========================================
                # SAVE
                # =========================================

                si.save(
                    ignore_permissions=True
                )

                # =========================================
                # COMMIT THIS INVOICE
                # =========================================

                frappe.db.commit()

                created += 1

                print(
                    f"SUCCESS: {si.name}"
                )

                # =========================================
                # PROGRESS
                # =========================================

                print(
                    f"Progress: "
                    f"{index}/{total_customers}"
                )

            except Exception:

                failed += 1

                error_message = (
                    frappe.get_traceback()
                )

                print("")
                print(
                    f"FAILED CUSTOMER: "
                    f"{customer.name}"
                )
                print(
                    error_message
                )

                frappe.log_error(
                    error_message,
                    (
                        "Monthly Sales Invoice "
                        f"Creation Failed - "
                        f"{customer.name}"
                    )
                )

                # -----------------------------------------
                # ROLLBACK ONLY CURRENT TRANSACTION
                # -----------------------------------------

                frappe.db.rollback()

                # -----------------------------------------
                # CONTINUE NEXT CUSTOMER
                # -----------------------------------------

                continue

        # -------------------------------------------------
        # FINAL COMMIT
        # -------------------------------------------------

        frappe.db.commit()

        # -------------------------------------------------
        # UPDATE STATUS
        # -------------------------------------------------

        frappe.db.set_value(
            "Monthly Invoice Creation",
            docname,
            "status",
            "Completed"
        )

        frappe.db.commit()

        # -------------------------------------------------
        # FINAL LOG
        # -------------------------------------------------

        print("")
        print("=" * 100)
        print("MONTHLY SALES INVOICE CREATION COMPLETED")
        print("=" * 100)

        print(
            "Total Customers:",
            total_customers
        )

        print(
            "Created:",
            created
        )

        print(
            "Skipped:",
            skipped
        )

        print(
            "Failed:",
            failed
        )

        print("=" * 100)

        return {
            "total_customers":
                total_customers,

            "created":
                created,

            "skipped":
                skipped,

            "failed":
                failed
        }

    except Exception:

        error_message = (
            frappe.get_traceback()
        )

        print("")
        print(
            "MONTHLY INVOICE JOB FAILED"
        )
        print(
            error_message
        )

        frappe.log_error(
            error_message,
            "Monthly Sales Invoice Background Job"
        )

        # -------------------------------------------------
        # UPDATE STATUS TO FAILED
        # -------------------------------------------------

        try:

            frappe.db.set_value(
                "Monthly Invoice Creation",
                docname,
                "status",
                "Failed"
            )

            frappe.db.commit()

        except Exception:
            pass

        return {
            "status": "failed",
            "error": error_message
        }

import frappe
import requests


@frappe.whitelist()
def create_payment_links_for_billed_period(docname):

    print("\n" + "=" * 100)
    print("STARTING PAYMENT LINK CREATION")
    print("=" * 100)

    # ---------------------------------------------------------
    # GET MONTHLY INVOICE CREATION DOCUMENT
    # ---------------------------------------------------------

    print(f"[1] Getting Monthly Invoice Creation document: {docname}")

    doc = frappe.get_doc(
        "Monthly Invoice Creation",
        docname
    )

    billed_period = doc.name

    print(f"[2] Monthly Invoice Creation : {doc.name}")
    print(f"[3] Billed Period             : {billed_period}")

    # ---------------------------------------------------------
    # STRIPE KEY
    # ---------------------------------------------------------

    print("[4] Checking Stripe Secret Key...")

    stripe_secret_key = frappe.conf.get(
        "stripe_secret_key"
    )

    if not stripe_secret_key:
        print("[ERROR] Stripe Secret Key is NOT configured!")

        frappe.throw(
            "Stripe Secret Key is not configured."
        )

    print("[5] Stripe Secret Key found.")

    stripe_url = (
        "https://api.stripe.com/v1/checkout/sessions"
    )

    created = 0
    failed = 0
    batch_number = 0

    # ---------------------------------------------------------
    # KEEP TAKING 50 RECORDS
    # ---------------------------------------------------------

    print("\n" + "-" * 100)
    print("STARTING BATCH PROCESSING")
    print("Batch Size : 50")
    print("-" * 100)

    while True:

        batch_number += 1

        print("\n")
        print("#" * 100)
        print(f"BATCH {batch_number} STARTED")
        print("#" * 100)

        # -----------------------------------------------------
        # GET NEXT 50 INVOICES
        # -----------------------------------------------------

        print(
            f"[Batch {batch_number}] Fetching next 50 Sales Invoices..."
        )

        invoices = frappe.get_all(
            "Sales Invoice",
            filters={
                "custom_billed_period": billed_period,
                "docstatus": ["!=", 2],

                # IMPORTANT:
                # Only get invoices which don't have payment link
                "custom_payment_link": ["is", "not set"]
            },
            fields=[
                "name",
                "customer",
                "customer_name",
                "grand_total"
            ],
            order_by="creation asc",
            limit_page_length=50
        )

        print(
            f"[Batch {batch_number}] Invoices fetched: "
            f"{len(invoices)}"
        )

        # -----------------------------------------------------
        # NO MORE INVOICES
        # -----------------------------------------------------

        if not invoices:

            print("\n" + "=" * 100)
            print("NO MORE INVOICES FOUND")
            print("=" * 100)

            break

        # -----------------------------------------------------
        # SHOW BATCH DETAILS
        # -----------------------------------------------------

        print(
            f"[Batch {batch_number}] Processing "
            f"{len(invoices)} invoices..."
        )

        print(
            f"[Batch {batch_number}] First Invoice : "
            f"{invoices[0].name}"
        )

        print(
            f"[Batch {batch_number}] Last Invoice  : "
            f"{invoices[-1].name}"
        )

        # -----------------------------------------------------
        # PROCESS EACH INVOICE
        # -----------------------------------------------------

        for index, invoice in enumerate(invoices, start=1):

            print("\n")
            print("-" * 90)

            print(
                f"[Batch {batch_number}] "
                f"Invoice {index}/{len(invoices)}"
            )

            print(
                f"Invoice Name   : {invoice.name}"
            )

            print(
                f"Customer       : {invoice.customer}"
            )

            print(
                f"Customer Name  : {invoice.customer_name}"
            )

            print(
                f"Grand Total    : {invoice.grand_total}"
            )

            print("-" * 90)

            try:

                # -------------------------------------------------
                # GET CUSTOMER EMAIL
                # -------------------------------------------------

                print(
                    f"[{invoice.name}] Getting customer email..."
                )

                customer_email = frappe.db.get_value(
                    "Customer",
                    invoice.customer,
                    "custom_email"
                )

                print(
                    f"[{invoice.name}] Customer Email: "
                    f"{customer_email}"
                )

                # -------------------------------------------------
                # CHECK AMOUNT
                # -------------------------------------------------

                print(
                    f"[{invoice.name}] Calculating Stripe amount..."
                )

                stripe_amount = int(
                    round(
                        float(invoice.grand_total) * 1
                    )
                )

                print(
                    f"[{invoice.name}] ERPNext Amount: "
                    f"{invoice.grand_total}"
                )

                print(
                    f"[{invoice.name}] Stripe Amount: "
                    f"{stripe_amount}"
                )

                if stripe_amount <= 0:

                    print(
                        f"[{invoice.name}] ERROR: "
                        f"Invalid Stripe amount!"
                    )

                    failed += 1

                    frappe.log_error(
                        f"Invalid Stripe amount: "
                        f"{stripe_amount}",
                        f"Payment Link Error - {invoice.name}"
                    )

                    continue

                # -------------------------------------------------
                # CREATE STRIPE PAYLOAD
                # -------------------------------------------------

                print(
                    f"[{invoice.name}] Preparing Stripe payload..."
                )

                payload = {

                    "line_items[0][price_data][product_data][name]":
                        "Go Green Service",

                    "line_items[0][quantity]":
                        "1",

                    "line_items[0][price_data][unit_amount]":
                        str(stripe_amount),

                    "line_items[0][price_data][currency]":
                        "aed",

                    "mode":
                        "payment",

                    "customer_email":
                        customer_email or "",

                    # -------------------------------------------------
                    # SALES INVOICE METADATA
                    # -------------------------------------------------

                    "metadata[sales_invoice_no]":
                        invoice.name,

                    "metadata[internal_reference]":
                        invoice.name,

                    # -------------------------------------------------
                    # PAYMENT INTENT METADATA
                    # -------------------------------------------------

                    "payment_intent_data[metadata][sales_invoice_no]":
                        invoice.name,

                    "payment_intent_data[metadata][order_id]":
                        invoice.name,

                    "success_url":
                        "https://gogreen.frappe.cloud/success",

                    "cancel_url":
                        "https://gogreen.frappe.cloud/cancel"
                }

                print(
                    f"[{invoice.name}] Stripe payload prepared."
                )

                # -------------------------------------------------
                # CALL STRIPE
                # -------------------------------------------------

                print(
                    f"[{invoice.name}] Sending request to Stripe..."
                )

                response = requests.post(
                    stripe_url,

                    headers={
                        "Authorization":
                            f"Bearer {stripe_secret_key}",

                        "Content-Type":
                            "application/x-www-form-urlencoded"
                    },

                    data=payload,

                    timeout=30
                )

                print(
                    f"[{invoice.name}] Stripe HTTP Status: "
                    f"{response.status_code}"
                )

                # -------------------------------------------------
                # RESPONSE
                # -------------------------------------------------

                try:

                    data = response.json()

                    print(
                        f"[{invoice.name}] Stripe response received."
                    )

                except Exception:

                    print(
                        f"[{invoice.name}] ERROR: "
                        f"Stripe response is not valid JSON."
                    )

                    print(
                        f"[{invoice.name}] Raw response:"
                    )

                    print(response.text)

                    failed += 1

                    frappe.log_error(
                        response.text,
                        f"Stripe Invalid Response - {invoice.name}"
                    )

                    continue

                # -------------------------------------------------
                # STRIPE ERROR
                # -------------------------------------------------

                if response.status_code >= 400:

                    print(
                        f"[{invoice.name}] STRIPE ERROR!"
                    )

                    print(
                        f"[{invoice.name}] Stripe Response:"
                    )

                    print(
                        frappe.as_json(data)
                    )

                    failed += 1

                    frappe.log_error(
                        frappe.as_json(data),
                        f"Stripe Error - {invoice.name}"
                    )

                    continue

                # -------------------------------------------------
                # GET STRIPE SESSION ID
                # -------------------------------------------------

                checkout_session_id = data.get("id")

                print(
                    f"[{invoice.name}] "
                    f"Stripe Checkout Session: "
                    f"{checkout_session_id}"
                )

                # -------------------------------------------------
                # GET PAYMENT LINK
                # -------------------------------------------------

                payment_link = data.get("url")

                print(
                    f"[{invoice.name}] "
                    f"Payment Link: "
                    f"{payment_link}"
                )

                if not payment_link:

                    print(
                        f"[{invoice.name}] ERROR: "
                        f"Payment link missing from Stripe response!"
                    )

                    print(
                        f"[{invoice.name}] Full Stripe Response:"
                    )

                    print(
                        frappe.as_json(data)
                    )

                    failed += 1

                    frappe.log_error(
                        frappe.as_json(data),
                        f"Payment Link Missing - {invoice.name}"
                    )

                    continue

                # -------------------------------------------------
                # UPDATE SALES INVOICE
                # -------------------------------------------------

                print(
                    f"[{invoice.name}] "
                    f"Updating custom_payment_link..."
                )

                frappe.db.set_value(
                    "Sales Invoice",
                    invoice.name,
                    "custom_payment_link",
                    payment_link,
                    update_modified=False
                )

                print(
                    f"[{invoice.name}] "
                    f"Payment link updated successfully."
                )

                created += 1

                print(
                    f"[{invoice.name}] SUCCESS"
                )

                print(
                    f"Total Created : {created}"
                )

                print(
                    f"Total Failed  : {failed}"
                )

            except Exception:

                failed += 1

                error_message = frappe.get_traceback()

                print("\n")
                print("!" * 100)

                print(
                    f"EXCEPTION FOR INVOICE: {invoice.name}"
                )

                print("!" * 100)

                print(error_message)

                frappe.log_error(
                    error_message,
                    f"Payment Link Error - {invoice.name}"
                )

                continue

        # ---------------------------------------------------------
        # COMMIT AFTER EACH 50
        # ---------------------------------------------------------

        print("\n")
        print("-" * 100)

        print(
            f"BATCH {batch_number} COMPLETED"
        )

        print(
            f"Batch Size       : {len(invoices)}"
        )

        print(
            f"Total Created    : {created}"
        )

        print(
            f"Total Failed     : {failed}"
        )

        print(
            f"Committing Batch {batch_number}..."
        )

        frappe.db.commit()

        print(
            f"Batch {batch_number} COMMITTED SUCCESSFULLY"
        )

        print("-" * 100)

    # ---------------------------------------------------------
    # FINAL COMMIT
    # ---------------------------------------------------------

    print("\n")
    print("=" * 100)
    print("PAYMENT LINK CREATION COMPLETED")
    print("=" * 100)

    frappe.db.commit()

    print(
        f"Billed Period : {billed_period}"
    )

    print(
        f"Total Created : {created}"
    )

    print(
        f"Total Failed  : {failed}"
    )

    print(
        f"Total Batches : {batch_number}"
    )

    print("=" * 100)

    return {
        "billed_period": billed_period,
        "created": created,
        "failed": failed,
        "batches": batch_number
    }  
    
    
import concurrent.futures
import time
import requests
import frappe

from decimal import Decimal, ROUND_HALF_UP


import concurrent.futures
import time
import requests
import frappe

from decimal import Decimal, ROUND_HALF_UP


# =================================================================
# MAIN FUNCTION
# Frappe DB operations happen ONLY in this main thread
# =================================================================

@frappe.whitelist()
def stripe_create_payment_links_for_billed_period(docname):

    print("\n" + "=" * 100)
    print("STARTING PAYMENT LINK CREATION")
    print("=" * 100)

    # -------------------------------------------------------------
    # GET MONTHLY INVOICE CREATION DOCUMENT
    # -------------------------------------------------------------

    print(
        f"[1] Getting Monthly Invoice Creation document: {docname}"
    )

    doc = frappe.get_doc(
        "Monthly Invoice Creation",
        docname
    )

    billed_period = doc.name

    print(
        f"[2] Monthly Invoice Creation : {doc.name}"
    )

    print(
        f"[3] Billed Period             : {billed_period}"
    )

    # -------------------------------------------------------------
    # STRIPE SECRET KEY
    # -------------------------------------------------------------

    print("[4] Checking Stripe Secret Key...")

    stripe_secret_key = frappe.conf.get(
        "stripe_secret_key"
    )

    if not stripe_secret_key:

        print(
            "[ERROR] Stripe Secret Key is NOT configured!"
        )

        frappe.throw(
            "Stripe Secret Key is not configured."
        )

    print(
        "[5] Stripe Secret Key found."
    )

    stripe_url = (
        "https://api.stripe.com/v1/checkout/sessions"
    )

    # -------------------------------------------------------------
    # COUNTERS
    # -------------------------------------------------------------

    created = 0
    failed = 0
    batch_number = 0

    # -------------------------------------------------------------
    # BATCH SETTINGS
    # -------------------------------------------------------------

    BATCH_SIZE = 50
    MAX_WORKERS = 10

    print("\n" + "-" * 100)
    print("STARTING BATCH PROCESSING")
    print(f"Batch Size    : {BATCH_SIZE}")
    print(f"Workers       : {MAX_WORKERS}")
    print("-" * 100)

    # =============================================================
    # KEEP PROCESSING UNTIL NO INVOICES ARE LEFT
    # =============================================================

    while True:

        batch_number += 1

        print("\n")
        print("#" * 100)
        print(
            f"BATCH {batch_number} STARTED"
        )
        print("#" * 100)

        # ---------------------------------------------------------
        # GET NEXT 50 SALES INVOICES
        #
        # IMPORTANT:
        # This DB query is executed in the MAIN Frappe thread.
        # ---------------------------------------------------------

        print(
            f"[Batch {batch_number}] "
            f"Fetching next {BATCH_SIZE} Sales Invoices..."
        )

        invoices = frappe.get_all(
            "Sales Invoice",
            filters={
                "custom_billed_period": billed_period,

                # Only submitted invoices
                "docstatus": 0,

                # Do not create duplicate payment links
                "custom_payment_link": ["is", "not set"]
            },
            fields=[
                "name",
                "customer",
                "customer_name",
                "grand_total"
            ],
            order_by="creation asc",
            limit_page_length=BATCH_SIZE
        )

        print(
            f"[Batch {batch_number}] "
            f"Invoices fetched: {len(invoices)}"
        )

        # ---------------------------------------------------------
        # NO MORE INVOICES
        # ---------------------------------------------------------

        if not invoices:

            print("\n" + "=" * 100)
            print("NO MORE INVOICES FOUND")
            print("=" * 100)

            break

        print(
            f"[Batch {batch_number}] "
            f"Processing {len(invoices)} invoices..."
        )

        print(
            f"[Batch {batch_number}] "
            f"First Invoice : {invoices[0].name}"
        )

        print(
            f"[Batch {batch_number}] "
            f"Last Invoice  : {invoices[-1].name}"
        )

        batch_created = 0
        batch_failed = 0

        # =========================================================
        # IMPORTANT:
        #
        # Fetch ALL customer emails BEFORE creating threads.
        #
        # This prevents:
        #
        # RuntimeError: object is not bound
        #
        # because frappe.db.get_value() stays in the main thread.
        # =========================================================

        print("\n")
        print(
            f"[Batch {batch_number}] "
            f"Loading customer emails..."
        )

        invoice_tasks = []

        for index, invoice in enumerate(
            invoices,
            start=1
        ):

            try:

                # -------------------------------------------------
                # MAIN THREAD - SAFE Frappe DB CALL
                # -------------------------------------------------

                customer_email = frappe.db.get_value(
                    "Customer",
                    invoice.customer,
                    "custom_email"
                )

                print(
                    f"[Batch {batch_number}] "
                    f"[{invoice.name}] "
                    f"Customer Email: "
                    f"{customer_email}"
                )

                # -------------------------------------------------
                # Store everything needed by worker
                #
                # Worker will NOT access frappe.db
                # -------------------------------------------------

                invoice_tasks.append({
                    "invoice": invoice,
                    "customer_email": customer_email,
                    "index": index
                })

            except Exception:

                batch_failed += 1
                failed += 1

                error_message = frappe.get_traceback()

                print(
                    f"[{invoice.name}] "
                    f"Failed to get customer email"
                )

                print(error_message)

                frappe.log_error(
                    error_message,
                    f"Customer Email Error - {invoice.name}"
                )

        # =========================================================
        # START 10 CONCURRENT STRIPE WORKERS
        # =========================================================

        print("\n")
        print(
            f"[Batch {batch_number}] "
            f"Starting {MAX_WORKERS} concurrent workers..."
        )

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=MAX_WORKERS
        ) as executor:

            future_to_invoice = {}

            # -----------------------------------------------------
            # SUBMIT STRIPE REQUESTS
            # -----------------------------------------------------

            for task in invoice_tasks:

                invoice = task["invoice"]
                customer_email = task["customer_email"]
                index = task["index"]

                print(
                    f"[Batch {batch_number}] "
                    f"Submitting "
                    f"Invoice {index}/{len(invoices)}: "
                    f"{invoice.name}"
                )

                future = executor.submit(
                    create_single_payment_link,
                    invoice,
                    customer_email,
                    stripe_secret_key,
                    stripe_url,
                    batch_number,
                    index,
                    len(invoices)
                )

                future_to_invoice[future] = invoice

                # -------------------------------------------------
                # Small rate limiting delay
                # -------------------------------------------------

                time.sleep(0.05)

            # -----------------------------------------------------
            # PROCESS COMPLETED STRIPE REQUESTS
            # -----------------------------------------------------

            for future in concurrent.futures.as_completed(
                future_to_invoice
            ):

                invoice = future_to_invoice[future]

                try:

                    result = future.result()

                    # =================================================
                    # SUCCESS
                    # =================================================

                    if result.get("success"):

                        payment_link = result.get(
                            "payment_link"
                        )

                        session_id = result.get(
                            "session_id"
                        )

                        print("\n")
                        print(
                            f"[{invoice.name}] SUCCESS"
                        )

                        print(
                            f"[{invoice.name}] "
                            f"Checkout Session: "
                            f"{session_id}"
                        )

                        print(
                            f"[{invoice.name}] "
                            f"Payment Link: "
                            f"{payment_link}"
                        )

                        # -------------------------------------------------
                        # MAIN THREAD - SAFE Frappe DB UPDATE
                        # -------------------------------------------------

                        frappe.db.set_value(
                            "Sales Invoice",
                            invoice.name,
                            "custom_payment_link",
                            payment_link,
                            update_modified=False
                        )

                        batch_created += 1
                        created += 1

                        print(
                            f"[{invoice.name}] "
                            f"custom_payment_link updated."
                        )

                        print(
                            f"Total Created : {created}"
                        )

                    # =================================================
                    # FAILED
                    # =================================================

                    else:

                        batch_failed += 1
                        failed += 1

                        error_message = result.get(
                            "error",
                            "Unknown error"
                        )

                        print("\n")
                        print(
                            f"[{invoice.name}] FAILED"
                        )

                        print(
                            f"[{invoice.name}] "
                            f"Error: {error_message}"
                        )

                        frappe.log_error(
                            error_message,
                            f"Payment Link Error - {invoice.name}"
                        )

                except Exception:

                    batch_failed += 1
                    failed += 1

                    error_message = frappe.get_traceback()

                    print("\n")
                    print("!" * 100)

                    print(
                        f"EXCEPTION FOR INVOICE: "
                        f"{invoice.name}"
                    )

                    print("!" * 100)

                    print(error_message)

                    frappe.log_error(
                        error_message,
                        f"Payment Link Exception - {invoice.name}"
                    )

        # =========================================================
        # COMMIT AFTER EACH BATCH
        #
        # This is in the MAIN Frappe thread.
        # =========================================================

        print("\n")
        print("-" * 100)

        print(
            f"BATCH {batch_number} COMPLETED"
        )

        print(
            f"Batch Size       : {len(invoices)}"
        )

        print(
            f"Batch Created    : {batch_created}"
        )

        print(
            f"Batch Failed     : {batch_failed}"
        )

        print(
            f"Total Created    : {created}"
        )

        print(
            f"Total Failed     : {failed}"
        )

        print(
            f"Committing Batch {batch_number}..."
        )

        frappe.db.commit()

        print(
            f"Batch {batch_number} "
            f"COMMITTED SUCCESSFULLY"
        )

        print("-" * 100)

    # =============================================================
    # FINAL COMMIT
    # =============================================================

    print("\n")
    print("=" * 100)
    print("PAYMENT LINK CREATION COMPLETED")
    print("=" * 100)

    frappe.db.commit()

    print(
        f"Billed Period : {billed_period}"
    )

    print(
        f"Total Created : {created}"
    )

    print(
        f"Total Failed  : {failed}"
    )

    print(
        f"Total Batches : {batch_number}"
    )

    print("=" * 100)

    return {
        "billed_period": billed_period,
        "created": created,
        "failed": failed,
        "batches": batch_number
    }


# =================================================================
# STRIPE WORKER
#
# IMPORTANT:
# This function must NOT call:
#
# frappe.db.get_value()
# frappe.db.set_value()
# frappe.get_doc()
# frappe.get_all()
# frappe.db.commit()
#
# It only communicates with Stripe.
# =================================================================

def create_single_payment_link(
    invoice,
    customer_email,
    stripe_secret_key,
    stripe_url,
    batch_number,
    index,
    total
):

    max_retries = 3
    retry_delay = 1

    for attempt in range(
        1,
        max_retries + 1
    ):

        try:

            print(
                f"[Batch {batch_number}] "
                f"[{invoice.name}] "
                f"Attempt {attempt}/{max_retries}"
            )

            # -----------------------------------------------------
            # CUSTOMER EMAIL
            #
            # Already fetched by MAIN Frappe thread.
            # -----------------------------------------------------

            print(
                f"[{invoice.name}] "
                f"Customer Email: "
                f"{customer_email}"
            )

            # -----------------------------------------------------
            # CALCULATE STRIPE AMOUNT
            # -----------------------------------------------------

            amount = Decimal(
                str(invoice.grand_total)
            )

            stripe_amount = int(
                (
                    amount * Decimal("100")
                ).quantize(
                    Decimal("1"),
                    rounding=ROUND_HALF_UP
                )
            )

            print(
                f"[{invoice.name}] "
                f"ERPNext Amount: "
                f"{invoice.grand_total}"
            )

            print(
                f"[{invoice.name}] "
                f"Stripe Amount: "
                f"{stripe_amount}"
            )

            if stripe_amount <= 0:

                return {
                    "success": False,
                    "invoice": invoice.name,
                    "error": (
                        f"Invalid Stripe amount: "
                        f"{stripe_amount}"
                    )
                }

            # -----------------------------------------------------
            # STRIPE PAYLOAD
            # -----------------------------------------------------

            payload = {

                # -------------------------------------------------
                # PRODUCT
                # -------------------------------------------------

                "line_items[0][price_data][product_data][name]":
                    "Go Green Service",

                "line_items[0][quantity]":
                    "1",

                # -------------------------------------------------
                # AMOUNT
                # -------------------------------------------------

                "line_items[0][price_data][unit_amount]":
                    str(stripe_amount),

                "line_items[0][price_data][currency]":
                    "aed",

                # -------------------------------------------------
                # MODE
                # -------------------------------------------------

                "mode":
                    "payment",

                # -------------------------------------------------
                # CUSTOMER EMAIL
                # -------------------------------------------------

                "customer_email":
                    customer_email or "",

                # -------------------------------------------------
                # CHECKOUT SESSION METADATA
                # -------------------------------------------------

                "metadata[sales_invoice_no]":
                    invoice.name,

                "metadata[internal_reference]":
                    invoice.name,

                # -------------------------------------------------
                # PAYMENT INTENT METADATA
                # -------------------------------------------------

                "payment_intent_data[metadata][sales_invoice_no]":
                    invoice.name,

                "payment_intent_data[metadata][order_id]":
                    invoice.name,

                # -------------------------------------------------
                # SUCCESS URL
                # -------------------------------------------------

                "success_url":
                    "https://gogreen.frappe.cloud/success",

                # -------------------------------------------------
                # CANCEL URL
                # -------------------------------------------------

                "cancel_url":
                    "https://gogreen.frappe.cloud/cancel"
            }

            print(
                f"[{invoice.name}] "
                f"Stripe payload prepared."
            )

            # -----------------------------------------------------
            # STRIPE REQUEST
            # -----------------------------------------------------

            print(
                f"[{invoice.name}] "
                f"Sending request to Stripe..."
            )

            response = requests.post(
                stripe_url,

                headers={
                    "Authorization":
                        f"Bearer {stripe_secret_key}",

                    "Content-Type":
                        "application/x-www-form-urlencoded",

                    # -------------------------------------------------
                    # IDEMPOTENCY KEY
                    #
                    # If Stripe receives the request but ERPNext
                    # does not receive the response, retrying the
                    # same invoice will not create another session.
                    # -------------------------------------------------

                    "Idempotency-Key":
                        f"erpnext-payment-session-{invoice.name}"
                },

                data=payload,

                timeout=30
            )

            print(
                f"[{invoice.name}] "
                f"Stripe HTTP Status: "
                f"{response.status_code}"
            )

            # -----------------------------------------------------
            # PARSE STRIPE RESPONSE
            # -----------------------------------------------------

            try:

                data = response.json()

                print(
                    f"[{invoice.name}] "
                    f"Stripe response received."
                )

            except Exception:

                print(
                    f"[{invoice.name}] "
                    f"Stripe response is not valid JSON."
                )

                if attempt < max_retries:

                    print(
                        f"[{invoice.name}] "
                        f"Retrying in "
                        f"{retry_delay} seconds..."
                    )

                    time.sleep(
                        retry_delay
                    )

                    continue

                return {
                    "success": False,
                    "invoice": invoice.name,
                    "error": (
                        "Invalid JSON response from Stripe: "
                        f"{response.text[:500]}"
                    )
                }

            # -----------------------------------------------------
            # STRIPE ERROR
            # -----------------------------------------------------

            if response.status_code >= 400:

                error_data = data.get(
                    "error",
                    {}
                )

                error_type = error_data.get(
                    "type",
                    "unknown"
                )

                error_message = error_data.get(
                    "message",
                    "Unknown Stripe error"
                )

                print(
                    f"[{invoice.name}] "
                    f"Stripe Error Type: "
                    f"{error_type}"
                )

                print(
                    f"[{invoice.name}] "
                    f"Stripe Error Message: "
                    f"{error_message}"
                )

                # -------------------------------------------------
                # RATE LIMIT
                # -------------------------------------------------

                if (
                    error_type == "rate_limit_error"
                    and attempt < max_retries
                ):

                    wait_time = retry_delay * 2

                    print(
                        f"[{invoice.name}] "
                        f"Rate limit reached."
                    )

                    print(
                        f"[{invoice.name}] "
                        f"Retrying in "
                        f"{wait_time} seconds..."
                    )

                    time.sleep(
                        wait_time
                    )

                    continue

                # -------------------------------------------------
                # TEMPORARY STRIPE/API ERROR
                # -------------------------------------------------

                if (
                    error_type in [
                        "api_error",
                        "api_connection_error"
                    ]
                    and attempt < max_retries
                ):

                    print(
                        f"[{invoice.name}] "
                        f"Temporary Stripe error."
                    )

                    print(
                        f"[{invoice.name}] "
                        f"Retrying in "
                        f"{retry_delay} seconds..."
                    )

                    time.sleep(
                        retry_delay
                    )

                    continue

                # -------------------------------------------------
                # PERMANENT ERROR
                # -------------------------------------------------

                return {
                    "success": False,
                    "invoice": invoice.name,
                    "error": (
                        f"Stripe Error "
                        f"({error_type}): "
                        f"{error_message}"
                    )
                }

            # -----------------------------------------------------
            # GET CHECKOUT SESSION ID
            # -----------------------------------------------------

            checkout_session_id = data.get(
                "id"
            )

            print(
                f"[{invoice.name}] "
                f"Checkout Session: "
                f"{checkout_session_id}"
            )

            # -----------------------------------------------------
            # GET PAYMENT URL
            # -----------------------------------------------------

            payment_link = data.get(
                "url"
            )

            print(
                f"[{invoice.name}] "
                f"Payment Link: "
                f"{payment_link}"
            )

            # -----------------------------------------------------
            # PAYMENT URL MISSING
            # -----------------------------------------------------

            if not payment_link:

                return {
                    "success": False,
                    "invoice": invoice.name,
                    "error": (
                        "Payment link missing from Stripe response. "
                        f"Session ID: "
                        f"{checkout_session_id}"
                    )
                }

            # -----------------------------------------------------
            # SUCCESS
            # -----------------------------------------------------

            print(
                f"[{invoice.name}] "
                f"Stripe Checkout Session created successfully."
            )

            return {
                "success": True,
                "invoice": invoice.name,
                "payment_link": payment_link,
                "session_id": checkout_session_id
            }

        # =========================================================
        # TIMEOUT
        # =========================================================

        except requests.exceptions.Timeout:

            print(
                f"[{invoice.name}] "
                f"Stripe request timeout."
            )

            if attempt < max_retries:

                print(
                    f"[{invoice.name}] "
                    f"Retrying in "
                    f"{retry_delay} seconds..."
                )

                time.sleep(
                    retry_delay
                )

                continue

            return {
                "success": False,
                "invoice": invoice.name,
                "error": (
                    f"Stripe request timeout "
                    f"after {max_retries} attempts"
                )
            }

        # =========================================================
        # NETWORK ERROR
        # =========================================================

        except requests.exceptions.RequestException as e:

            print(
                f"[{invoice.name}] "
                f"Network error: {str(e)}"
            )

            if attempt < max_retries:

                print(
                    f"[{invoice.name}] "
                    f"Retrying in "
                    f"{retry_delay} seconds..."
                )

                time.sleep(
                    retry_delay
                )

                continue

            return {
                "success": False,
                "invoice": invoice.name,
                "error": (
                    f"Network error: {str(e)}"
                )
            }

        # =========================================================
        # UNEXPECTED ERROR
        # =========================================================

        except Exception as e:

            print(
                f"[{invoice.name}] "
                f"Unexpected error: {str(e)}"
            )

            return {
                "success": False,
                "invoice": invoice.name,
                "error": (
                    f"Unexpected error: {str(e)}"
                )
            }

    # -------------------------------------------------------------
    # MAX RETRIES EXHAUSTED
    # -------------------------------------------------------------

    return {
        "success": False,
        "invoice": invoice.name,
        "error": (
            f"Failed after "
            f"{max_retries} attempts"
        )
    }
    
import frappe
from frappe.utils import today


@frappe.whitelist(allow_guest=True)
def payment_stripe_webhook():

    try:

        # -----------------------------------------
        # Get Stripe Payload
        # -----------------------------------------

        payload = frappe.request.get_json()

        event_type = payload.get("type")

        data = payload.get("data") or {}

        stripe_data = data.get("object") or {}

        # -----------------------------------------
        # Only Process Successful Payment Intent
        # -----------------------------------------

        if event_type != "payment_intent.succeeded":

            return {
                "success": True,
                "message": f"Event {event_type} ignored"
            }

        # -----------------------------------------
        # Stripe Payment Intent ID
        # -----------------------------------------

        stripe_payment_id = stripe_data.get("id")

        if not stripe_payment_id:

            frappe.throw(
                "Stripe Payment Intent ID not found"
            )

        # -----------------------------------------
        # Check Payment Status
        # -----------------------------------------

        if stripe_data.get("status") != "succeeded":

            frappe.throw(
                "Stripe payment is not successful"
            )

        # -----------------------------------------
        # Get Metadata
        # -----------------------------------------

        metadata = stripe_data.get("metadata") or {}

        invoice_name = metadata.get(
            "sales_invoice_no"
        )

        if not invoice_name:

            frappe.throw(
                "Sales Invoice number not found in Stripe metadata"
            )

        # -----------------------------------------
        # Get Sales Invoice
        # -----------------------------------------

        invoice = frappe.get_doc(
            "Sales Invoice",
            invoice_name
        )

        # -----------------------------------------
        # Customer
        # -----------------------------------------

        customer = invoice.customer

        company = invoice.company

        # -----------------------------------------
        # Payment Amount
        # -----------------------------------------

        stripe_amount = (
            stripe_data.get("amount_received")
            or stripe_data.get("amount")
            or 0
        )

        # Stripe amount is in smallest currency unit
        # Example:
        # 15000 = AED 150.00

        payment_amount = float(stripe_amount) / 100

        # -----------------------------------------
        # Check Duplicate Payment
        # -----------------------------------------

        existing_payment = frappe.db.exists(
            "Payment Entry",
            {
                "reference_no": stripe_payment_id
            }
        )

        if existing_payment:

            return {
                "success": True,
                "message": "Payment Entry already exists",
                "payment_entry": existing_payment
            }

        # -----------------------------------------
        # Create Payment Entry
        # -----------------------------------------

        payment = frappe.get_doc({

            "doctype": "Payment Entry",

            "payment_type": "Receive",

            "company": company,

            "party_type": "Customer",

            "party": customer,

            "mode_of_payment": "Stripe",

            "paid_amount": payment_amount,

            "received_amount": payment_amount,

            "reference_no": stripe_payment_id,

            "reference_date": today(),

            "references": [
                {
                    "reference_doctype": "Sales Invoice",

                    "reference_name": invoice.name,

                    "allocated_amount": payment_amount
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

        payment.paid_to = "Bank of Baroda- Go Green - GG"

        # -----------------------------------------
        # Paid From Account
        # -----------------------------------------

        payment.paid_from = invoice.debit_to

        # -----------------------------------------
        # Insert Payment
        # -----------------------------------------

        payment.insert(
            ignore_permissions=True
        )

        # -----------------------------------------
        # Submit Payment
        # -----------------------------------------

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

            "message": "Payment Entry created successfully",

            "payment_entry": payment.name,

            "sales_invoice": invoice.name,

            "customer": customer,

            "amount": payment_amount,

            "currency": stripe_data.get("currency"),

            "stripe_payment_id": stripe_payment_id
        }

    except Exception as e:

        frappe.db.rollback()

        frappe.log_error(
            frappe.get_traceback(),
            "Stripe Payment Entry Error"
        )

        return {
            "success": False,
            "error": str(e)
        }
