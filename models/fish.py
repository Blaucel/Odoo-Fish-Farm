# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fish(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'ejro21222.fish'
    _description = 'Fishes species'

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    specie = fields.Char(string='Fish specie')
    comname = fields.Char(string='Common name')
    fishimg = fields.Image()
    weight = fields.Integer(string='Average weight (g)', help="Must be expressed in g")  # in grams (g)
    eggtime = fields.Integer(string='Egg period (d)', help="Must be expressed in days (d)")  # in days (d)
    larvaetime = fields.Integer(string='Larvae period (d)', help="Must be expressed in days (d)")  # in days (d)
    juventime = fields.Integer(string='Juvenile period (d)', help="Must be expressed in days (d)")  # in days (d)
    adultime = fields.Integer(string='Adult period (d)', help="Must be expressed in days (d)")  # in days (d)
    description = fields.Text()

    # Special
    feeding = fields.Selection(
        [('omnivorous', 'Omnivorous'), ('carnivorous', 'Carnivorous'), ('herbivorous', 'Herbivorous')],
        string='Type of feeding', default='none')

    # Computed
    lifecycle = fields.Integer(string='Full life cycle (d)', compute="_life_cycle", store=True)  # in days (d)

    # ---------------------------------------- Compute methods ------------------------------------

    @api.depends('eggtime', 'larvaetime', 'juventime', 'adultime')
    def _life_cycle(self):
        for record in self:
            record.lifecycle = record.eggtime + record.larvaetime + record.juventime + record.adultime
