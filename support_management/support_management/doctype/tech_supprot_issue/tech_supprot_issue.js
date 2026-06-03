// Copyright (c) 2026, Marwan Badr and contributors
// For license information, please see license.txt
frappe.ui.form.on("Tech Supprot Issue", {
    refresh(frm) {
        if (!frm.is_new()){
            frm.add_custom_button(__("Create Maintenance Visit"), function(){
                frappe.confirm(
                    __('Are you sure you want to create a Maintenance Visit?'),
                    function() {
                        frappe.call({
                            method: "support_management.utils.tech_logic.create_maintenance_visit",
                            args: {
                                customer: frm.doc.customer,
                                maint_time: frm.doc.dt,
                                visit_date: frm.doc.visit_date,
                                item_code: frm.doc.item_code,
                                serial_number: frm.doc.serial_number,
                                address: frm.doc.address,
                                report: frm.doc.report,
                                doc_name: frm.doc.name
                            },
                            callback: function(r) {
                                if (!r.exc) {
                                    frappe.msgprint(__('Maintenance has been created successfully!'));
                                }
                            }
                        });
                    },
                    function() {
                        return;
                    }
                );
            });    
        }
    },
});