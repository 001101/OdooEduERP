# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Evaluation Management',
    'version': "10.0.1.0.0",
    'author': '''Serpent Consulting Services Pvt. Ltd.,
                 Odoo Community Association (OCA)''',
    'website': 'http://www.almisnadtechnology.com',
    'category': 'School Management',
    'license': "AGPL-3",
    'complexity': 'easy',
    'summary': 'A Module For Evaluation Management In School',
    'depends': ['hr', 'school'],
    'data': ['views/student_evaluation_view.xml',
             'security/ir.model.access.csv'],
    'demo': ['demo/student_evaluation_demo.xml'],
    'installable': True,
    'application': True
}
