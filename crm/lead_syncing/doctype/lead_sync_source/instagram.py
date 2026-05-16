# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from crm.lead_syncing.doctype.lead_sync_source.facebook import FacebookSyncSource


class InstagramSyncSource(FacebookSyncSource):
	"""Instagram Lead Ads sync source.

	Instagram Lead Ads use the same Meta Graph API as Facebook since leads
	flow through Facebook Pages connected to Instagram accounts. The only
	difference is that the CRM Lead source is set to "Instagram".
	"""

	def sync_single_lead(self, lead, raise_exception=False):
		import frappe
		from crm.lead_syncing.doctype.lead_sync_source.facebook import DuplicateLeadError

		question_to_field_map = self.get_form_questions_mapping()
		lead_data = {item["name"]: item["values"][0] for item in lead["field_data"]}
		crm_lead_data = {
			question_to_field_map.get(k): v for k, v in lead_data.items() if k in question_to_field_map
		}
		crm_lead_data["source"] = "Instagram"
		crm_lead_data["facebook_lead_id"] = lead["id"]
		crm_lead_data["facebook_form_id"] = self.form_id

		try:
			self.validate_duplicate_lead(crm_lead_data, question_to_field_map)
			return frappe.get_doc(
				{
					"doctype": "CRM Lead",
					**crm_lead_data,
				}
			).insert(ignore_permissions=True)
		except (frappe.UniqueValidationError, DuplicateLeadError):
			self.create_failure_log(lead, "Duplicate")
			if raise_exception:
				raise
		except Exception:
			self.create_failure_log(lead, traceback=frappe.get_traceback(with_context=True))
			if raise_exception:
				raise
