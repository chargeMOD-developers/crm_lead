import frappe


def execute():
	for source in ("Instagram", "WhatsApp"):
		if not frappe.db.exists("CRM Lead Source", source):
			doc = frappe.new_doc("CRM Lead Source")
			doc.source_name = source
			doc.insert(ignore_permissions=True)
