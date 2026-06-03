# Copyright (c) 2026, Marwan Badr and contributors
# For license information, please see license.txt

from os import link
import frappe
from frappe.model.document import Document


class CSSupportIssue(Document):
	def before_save(self):
		self._status_validation()

	def _status_validation(self):
		if self.report:
			if self.status == "Open":
				self.status = "Replied"
			
	def before_insert(self):
		link = frappe.get_value("Dynamic Link",
			{"parenttype":"Contact",
			"link_doctype":"Customer",
			"link_name":self.customer
			},"parent")
		
		if link:
			phone = frappe.get_value("Contact Phone",{"parent":link},"phone")
			
			if phone:
				self.customer_phone = phone

			
