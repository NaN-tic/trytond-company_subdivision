# This file is part of the company_subdivision module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class CompanySubdivisionTestCase(ModuleTestCase):
    'Test Company Subdivision module'
    module = 'company_subdivision'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CompanySubdivisionTestCase))
    return suite