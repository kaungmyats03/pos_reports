# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'
    _description = 'POS Config'

    show_logo = fields.Boolean(string="Show Logo in Receipt",
                               default=False)
    show_company_address = fields.Boolean(string="Show Company Address in Receipt",
                                          default=True)
    logo = fields.Binary(string="Logo")

