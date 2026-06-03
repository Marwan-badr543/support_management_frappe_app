frappe.ui.form.on('Issue', {
    refresh: function(frm) {
        setup_serial_filter(frm);
    },
    custom_item_code: function(frm) {
        setup_serial_filter(frm);
    }
});

function setup_serial_filter(frm) {
    frm.set_query('custom_serial_number', function() {
        return {
            filters: {
                'item_code': frm.doc.custom_item_code,
                'status': "Delivered",
            }
        };
    });
}