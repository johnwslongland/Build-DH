# Copyright (c) 2023, J Longland and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BDH(Document):

    @frappe.whitelist()
    def populate_check_items(self):
        parameters = frappe.get_doc("BDH Parameter Template", self.bdh_template)
        self.check_items = []

        for parameter in parameters.parameters:
            self.append("check_items", {
                "parameter": parameter.parameter,
                "checked": 0,
                "employee": "",
                "date": None
            })

        self.save()

