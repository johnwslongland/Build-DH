import frappe

@frappe.whitelist()
def get_template(template_name, build):

    template = frappe.get_doc("BDH Template", template_name)
    bdh_doc = frappe.get_doc("BDH", build)
    bdh_doc.check_items = []

    for parameter in template.bdh_parameters:
        bdh_doc.append("check_items", {
            "parameter": parameter.bdh_parameter,
            "checked": 0,
            "employee": "",
            "date": None
        })

    bdh_doc.save()
