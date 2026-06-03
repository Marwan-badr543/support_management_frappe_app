// Copyright (c) 2026, Marwan Badr and contributors
// For license information, please see license.txt

frappe.ui.form.on("CS Support Issue", {
	refresh(frm) {
        frm.add_custom_button("Close", () => {
            frm.set_value("status", "Closed");
            frm.save()
        },"Actions");
        
        frm.add_custom_button("Move to Tech", () => {
            // frm.set_value("status", "Reopened");
            // frm.save()
        },"Actions");
	},
});
