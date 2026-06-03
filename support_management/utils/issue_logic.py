import frappe
from datetime import datetime

def handle_workflow_action(doc, method):
    old_doc = doc.get_doc_before_save()
    if old_doc:
        if old_doc.workflow_state == "Draft" and doc.workflow_state == "Customer Service":
            _validate_reply_process(doc)
            doc.first_responded_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if old_doc.workflow_state == "Customer Service" and doc.workflow_state == "Technician":
            _validate_move_to_tech_process(doc)

        if old_doc.workflow_state == "Technician" and doc.workflow_state == "Maint Tech":
            if not getattr(doc.flags,"is_system_update", False):
                doc.workflow_state == "Technician"
                frappe.throw("Issue can't be assigned to Mait Tech here.")       
                

def validate_status(doc, method):
    _sync_status(doc)
    _validate_close_issue(doc)
    _validate_open_issue(doc)


def _sync_status(doc):
    old_doc = doc.get_doc_before_save()
    # frappe.throw(f"old doc is {old_doc}")
    if old_doc:
        old_status = old_doc.workflow_state
        
        if doc.workflow_state != old_status:
            doc.custom_hidden_status = doc.workflow_state

    else:
        doc.custom_hidden_status = doc.workflow_state            


def _validate_close_issue(doc):
    if doc.status and doc.status.lower() == "closed":
        doc.workflow_state = "Closed"


def _validate_open_issue(doc):
    old_doc = doc.get_doc_before_save()
    if old_doc:
        old_status = old_doc.status

        if doc.status and old_status and doc.status.lower() == "open" and old_status.lower() == "closed":
            doc.workflow_state = doc.custom_hidden_status



def _validate_reply_process(doc):
    if doc.workflow_state.lower() == "customer service":    
        if not doc.custom_report:
            frappe.throw("Please Fill Your Report.")

    # if doc.custom_report and doc.workflow_state.lower() == "draft":
    #     doc.workflow_state = "Customer Service"


def _validate_move_to_tech_process(doc):    
    if doc.workflow_state.lower() == "technician":
        if not doc.custom_item_code:
            frappe.throw("PLease determite item code.")
        if not doc.custom_serial_number:
            frappe.throw("PLease determite serial number.")
        if not doc.custom_technician:
            frappe.throw("Please Assign A Technician Before Moving To Technician Status")
        if not doc.custom_visit_time:
            frappe.throw("PLease determite visit time.")    
        if not doc.custom_visit_date:
            frappe.throw("PLease determite visit date.")    
        if not doc.custom_address:
            frappe.throw("PLease set customer address.")    

        doc.workflow_state = "Technician"
        return True

    
def create_tech_doc(doc, method):
    old_doc = doc.get_doc_before_save()
    if old_doc:
        if old_doc.workflow_state == "Customer Service" and doc.workflow_state == "Technician":
            issue_name = doc.name
            tech = doc.custom_technician
            visit_date = doc.custom_visit_date
            visit_time = doc.custom_visit_time
            address = doc.custom_address
            description = doc.description

            new_tech_doc = frappe.get_doc({
                "doctype": "Tech Supprot Issue",
                "issue": issue_name,
                "technician": tech,
                "visit_date": visit_date,
                "dt": visit_time,
                "address": address,
                "description": description,
                "item_code": doc.custom_item_code,
                "serial_number": doc.custom_serial_number,
                "customer": doc.customer
            })

            new_tech_doc.insert()
            