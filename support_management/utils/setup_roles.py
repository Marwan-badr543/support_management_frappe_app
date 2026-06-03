import frappe


def create_role_profile():
    if not frappe.db.exists("Role Profile", "Technician"):
            role_profile = frappe.get_doc({
                "doctype": "Role Profile",
                "role_profile": "Technician",
                "roles": [
                    {"role": "Maintenance User"},
                    {"role": "Technician"}
                    ]
                })
            role_profile.insert(ignore_permissions=True)

    if not frappe.db.exists("Role Profile", "Maintenance Technician"):
            role_profile = frappe.get_doc({
                "doctype": "Role Profile",
                "role_profile": "Maintenance Technician",
                "roles": [
                    {"role": "Maintenance Technician User"}
                    ]
                })
            role_profile.insert(ignore_permissions=True, ignore_links=True)
