# -*- coding: utf-8 -*-
# (c) 2014 Serv. Tec. Avanzados - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from . import models

from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    # Create QC triggers
    env = api.Environment(cr, SUPERUSER_ID, {})
    picking_types = env['stock.picking.type'].search([])
    for picking_type in picking_types:
        picking_type._create_qc_trigger()
