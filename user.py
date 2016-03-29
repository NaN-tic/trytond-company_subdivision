# This file is part company_subdivision module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['User']


class User:
    __metaclass__ = PoolMeta
    __name__ = "res.user"
    subdivisions = fields.Many2Many('company.subdivision-res.user',
            'user', 'subdivision', 'Subdivisions')
    subdivision = fields.Many2One('company.subdivision', 'Subdivision', domain=[
            ('id', 'in', Eval('subdivisions', [])),
            ], depends=['subdivisions'])

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._preferences_fields.extend([
                'subdivision',
                'subdivisions',
                ])
        cls._context_fields.insert(0, 'subdivision')
        cls._context_fields.insert(0, 'subdivisions')

    def get_status_bar(self, name):
        status = super(User, self).get_status_bar(name)
        if self.subdivision:
            status += ' - %s' % (self.subdivision.rec_name)
        return status
