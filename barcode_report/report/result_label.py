# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.report import report_sxw
from odoo import models
import odoo


class ResultLabel(report_sxw.rml_parse):

    def __init__(self):
        super(ResultLabel, self).__init__()
        self.localcontext.update({'get_student_info': self.get_student_info})

    def get_student_info(self, standard_id, division_id, medium_id, year_id):
        env = odoo.api.Environment(self.cr, self.uid, {})
        student_obj = env['student.student']
        student_ids = student_obj.search([('standard_id', '=', standard_id),
                                          ('division_id', '=', division_id),
                                          ('medium_id', '=', medium_id),
                                          ('year', '=', year_id)])
        result = []
        for student in student_ids:
            result.append(student.pid)
        return result


class ReportLabel(models.AbstractModel):

    _name = 'report.barcode_report.result_label'
    _inherit = 'report.abstract_report'
    _template = 'barcode_report.result_label'
    _wrapped_report_class = ResultLabel
