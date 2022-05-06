# -*- coding: utf-8 -*-

from odoo import models, fields, api


class farm(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'ejro21222.farm'
    _description = 'Farming Processes'

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    selpools = fields.Char()
    selspecie = fields.Char()
    selfeeding = fields.Char()
    sellifecycle = fields.Char()
    seltransferdate = fields.Char()
    selfishingdate = fields.Char()

    # Relational
    oncharge = fields.Many2many('hr.employee', string='Employee')

    # Special

    # Computed


    # ---------------------------------------- Compute methods ------------------------------------

