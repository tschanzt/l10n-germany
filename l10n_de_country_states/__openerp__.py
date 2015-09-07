# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2010-2013 OpenERP s.a. (<http://openerp.com>).
# Copyright (C) 2014 initOS GmbH & Co. KG (<http://www.initos.com>).
# Author Nikolina Todorova <nikolina.todorova@initos.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Country States',
    'version': '1.0',
    'category': '',
    'author': 'initOS GmbH & Co. KG, Odoo Community Association (OCA)',
    'description': """
States in Germany
======================
    """,
    'website': '',
    'depends': [
        'base',
    ],
    'init_xml': [
    ],
    'update_xml': [
        'data/res_country_states.xml'
    ],
    'test': [
    ],
    'demo_xml': [
    ],
    'installable': True,
    'active': False,
}
