# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe


def create_lead_from_whatsapp_message(doc):
	"""Create a CRM Lead from an incoming WhatsApp message if no existing lead/deal exists."""
	if doc.type != "Incoming":
		return

	phone_number = doc.get("from")
	if not phone_number:
		return

	# Check if WhatsApp lead sync is enabled
	if not frappe.db.exists("Lead Sync Source", {"type": "WhatsApp", "enabled": 1}):
		return

	# If reference is already set to a CRM Lead or CRM Deal, skip
	if doc.reference_doctype in ("CRM Lead", "CRM Deal") and doc.reference_name:
		return

	# Check if a lead or deal already exists for this phone number
	from crm.integrations.api import get_contact_lead_or_deal_from_number

	try:
		name, doctype = get_contact_lead_or_deal_from_number(phone_number)
		if name and doctype:
			return
	except Exception:
		pass

	# Check for existing lead with this mobile number
	if frappe.db.exists("CRM Lead", {"mobile_no": phone_number}):
		return

	# Create a new CRM Lead
	lead = frappe.get_doc(
		{
			"doctype": "CRM Lead",
			"mobile_no": phone_number,
			"source": "WhatsApp",
			"first_name": phone_number,
		}
	)
	lead.insert(ignore_permissions=True)

	# Update the WhatsApp message reference to point to the new lead
	doc.reference_doctype = "CRM Lead"
	doc.reference_name = lead.name
