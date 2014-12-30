#This file is part company_subdivision module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .company import *
from .user import *

def register():
    Pool.register(
        Company,
        CompanySubdivision,
        CompanySubdivisionResUser,
        User,
        module='company_subdivision', type_='model')
