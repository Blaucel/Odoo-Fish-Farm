# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pool(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'ejro21222.pool'
    _description = 'Installation pools'

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char()
    capacity = fields.Integer(help="Must be expressed in hectoliters (hl)")  # in hectoliters (hl)
    description = fields.Text()

    # Special
    water = fields.Selection(
        [('fresh', 'Fresh water'), ('salt', 'Salt water'), ('none', 'None')], string='Type of water', default='none')
    state = fields.Selection(
        [('ready', 'Ready for use'), ('farming', 'Farming'), ('maintenance', 'Maintenance')], string='Pool State',
        default='none')

    # Computed

    # ---------------------------------------- Compute methods ------------------------------------
