import frappe


def get_permission_query_conditions(user):
    if "System Manager" in frappe.get_roles(user):
        return "1=1"

    if "Technician" in frappe.get_roles(user): 
        user_escaped = frappe.db.escape(user) 
        return f"`tabTech Supprot Issue`.technician = {user_escaped}" 

    return "1=1" 

def get_permission_query_conditions_maint(user):
    if "System Manager" in frappe.get_roles(user):
        return "1=1"

    if "Maintenance Technician User" in frappe.get_roles(user): 
        user_escaped = frappe.db.escape(user) 
        return f"`tabMaint Tech Supprot Issue`.maint_tech = {user_escaped}" 

    return "1=1" 
 

def has_permission(doc, user):
    if "Technician" in frappe.get_roles(user):
        return doc.technician == user
    return True    


def has_permission_maint(doc, user):
    if "Maintenance Technician User" in frappe.get_roles(user):
        return doc.maint_tech == user
    return True    