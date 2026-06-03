import frappe 

def get_series_number_from_invoice():
    sales_order = frappe.db.get_value("Sales Invoice", "ACC-SINV-2026-00006")
    print(sales_order) 