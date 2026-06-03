import frappe 

def handle_tech_wrokflow(doc, method):
    if _validate_move_to_mait_tech(doc):
        create_maint_tech_doc(doc)
        _update_issue_state(doc)

def _validate_move_to_mait_tech(doc):
    old_doc = doc.get_doc_before_save()
    if old_doc and old_doc.workflow_state == "Technician" and doc.workflow_state == "Maint Tech":
        if not doc.description:
            frappe.throw("Please set your Description.")
        if not doc.report:
            frappe.throw("Please set your Report.")
        if not doc.maintenance_technician:
            frappe.throw("Please determine Maintenance Technician.")
        if not doc.pickup_date:
            frappe.throw("Please determine Pickup Date.")
        if not doc.pickup_time:
            frappe.throw("Please determine Pickup Time.")
        return True


def create_maint_tech_doc(doc):
    issue = doc.issue
    description = doc.description
    maintenance_technician = doc.maintenance_technician
    pickup_date = doc.pickup_date
    pickup_time = doc.pickup_time

    new_maint_tech_doc = frappe.get_doc({
        "doctype": "Maint Tech Supprot Issue",
        "issue": issue,
        "description": description,
        "maintenance_technician": maintenance_technician,
        "pickup_date": pickup_date,
        "pickup_time": pickup_time,
        "maint_tech": doc.maintenance_technician,
        "item_code": doc.item_code,
        "serial_number": doc.serial_number
    })
    new_maint_tech_doc.insert()


def _update_issue_state(doc):
    issue_doc = frappe.get_doc("Issue", doc.issue)
    if issue_doc:
        issue_doc.workflow_state = "Maint Tech"
        issue_doc.flags.is_system_update = True
        issue_doc.save()


@frappe.whitelist()
def create_maintenance_visit(customer, maint_time, visit_date, item_code, serial_number, address, report, doc_name):
    new_visit = frappe.get_doc({
        "doctype": "Maintenance Visit",
        "customer": customer,
        "custom_tech_issue": doc_name,
        "mntc_time": maint_time,
        "mntc_date": visit_date,
        "purposes": [
            {
            "item_code": item_code,
            "serial_no": serial_number,
            "service_person": "Sales Team",
            "work_done": report
            }],
        "completion_status": "Fully Completed",
        "maintenance_type": "Breakdown",
    })
    
    new_visit.insert()
    
    return {"status": "success"}