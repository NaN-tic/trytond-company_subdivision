#This file is part company_subdivision module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import If, Eval
from trytond.transaction import Transaction

__all__ = ['Company', 'CompanySubdivision', 'CompanySubdivisionResUser']

STATES = {
    'readonly': ~Eval('active', True),
}
DEPENDS = ['active']


class Company:
    __metaclass__ = PoolMeta
    __name__ = 'company.company'
    subdivisions = fields.One2Many('company.subdivision', 'company',
        'Subdivisions')


class CompanySubdivision(ModelSQL, ModelView):
    'Company Subdivision'
    __name__ = "company.subdivision"
    name = fields.Char('Name', required=True, select=True,
        states=STATES, depends=DEPENDS)
    active = fields.Boolean('Active', select=True)
    address = fields.Many2One('party.address', 'Address', 
        states=STATES, depends=DEPENDS)
    company = fields.Many2One('company.company', 'Company', required=True,
        states=STATES, depends=DEPENDS, select=True,
        domain=[
            ('id', If(Eval('context', {}).contains('company'), '=', '!='),
                Eval('context', {}).get('company', -1)),
            ])

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_company():
        return Transaction().context.get('company')


class CompanySubdivisionResUser(ModelSQL):
    'Company Subdivision - Res User'
    __name__ = 'company.subdivision-res.user'
    _table = 'company_subdivision_res_user'
    subdivision = fields.Many2One('company.subdivision', 'Subdivision', ondelete='CASCADE',
        select=True, required=True)
    user = fields.Many2One('res.user', 'User', ondelete='RESTRICT',
        required=True)
