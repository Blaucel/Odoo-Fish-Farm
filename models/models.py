# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta


class Fish(models.Model):
    _name = 'ejro2122.fish'
    _description = 'Fish species'

    specie = fields.Char()
    comname = fields.Char()
    feeding = fields.Char()
    weight = fields.Integer(help="Must be expressed in g")  # in grams (g)
    eggtime = fields.Integer(help="Must be expressed in days (d)") # in days (d)
    larvaetime = fields.Integer(help="Must be expressed in days (d)")  # in days (d)
    juventime = fields.Integer(help="Must be expressed in days (d)")  # in days (d)
    adultime = fields.Integer(help="Must be expressed in days (d)")  # in days (d)
    lifecycle = fields.Integer(compute="_life_cycle", store=True)  # in days (d)
    description = fields.Text()

    @api.depends('eggtime', 'larvaetime', 'juventime', 'adultime')
    def _life_cycle(self):
        for record in self:
            record.lifecycle = record.eggtime + record.larvaetime + record.juventime + record.adultime


class Pool(models.Model):
    _name = 'ejro2122.pool'
    _description = 'Installation pools'

    name = fields.Char()
    capacity = fields.Integer(help="Must be expressed in hectoliters (hl)")  # in hectoliters (hl)
    water = fields.Selection(
        [('fresh', 'Fresh water'), ('salt', 'Salt water'), ('none', 'None')], string='Type of water', default='none')
    state = fields.Selection(
        [('ready', 'Ready for use'), ('farming', 'Farming'), ('maintenance', 'Maintenance')], string='Pool State', default='none')
    description = fields.Text()


# class Farming(models.Model):
#     _name = 'ejro2122.farm'
#     _description = 'Farming process'
#
#     pool = fields.Char()  # referencia a una piscina
#     specie = fields.Char()  # referencia a un pez
#     feeding = fields.Char()  # debe sacar la info del pez
#     lifecycle = fields.Integer()  # debe sacar la info del pez
#     transferdate = fields.Datetime('Datetime', default=fields.datetime.now())
#     fishingdate = fields.Datetime('Datetime', default=fields.datetime.now())  # Hacer el calculo
#     oncharge = fields.Many2many('hr.employee', string='Employee')
#
#     @api.depends('transferdate')
#     def _fishing_date(self):
#         for record in self:
#             record.fishingdate = record.transferdate + timedelta(days=record.lifecycle)
