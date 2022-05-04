# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta


class Fish(models.Model):
    _name = 'ejro2122.fish'
    _description = 'Fish species'

    specie = fields.Char(string='Fish specie')
    comname = fields.Char(string='Common name')
    fishimg = fields.Image()
    feeding = fields.Selection(
        [('omnivorous', 'Omnivorous'), ('carnivorous', 'Carnivorous'), ('herbivorous', 'Herbivorous')], string='Type of feeding', default='none')
    weight = fields.Integer(string='Average weight (g)', help="Must be expressed in g")  # in grams (g)
    eggtime = fields.Integer(string='Egg period (d)', help="Must be expressed in days (d)") # in days (d)
    larvaetime = fields.Integer(string='Larvae period (d)', help="Must be expressed in days (d)")  # in days (d)
    juventime = fields.Integer(string='Juvenile period (d)', help="Must be expressed in days (d)")  # in days (d)
    adultime = fields.Integer(string='Adult period (d)', help="Must be expressed in days (d)")  # in days (d)
    lifecycle = fields.Integer(string='Full life cycle (d)', compute="_life_cycle", store=True)  # in days (d)
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


class Farm(models.Model):
    _name = 'ejro2122.farm'

    pool = fields.Char()
    specie = fields.Char()
    feeding = fields.Char()
    lifecycle = fields.Char()
    transferdate = fields.Char()
    fishingdate = fields.Char()
#     oncharge = fields.Many2many('hr.employee', string='Employee')

#
#
    # pool = fields.One2many('ejro2122.pool', 'name', string='name')  # referencia a una piscina
    # specie = fields.Many2one('ejro2122.fish', 'specie', string='specie')  # referencia a un pez
    # feeding = fields.Many2one('ejro2122.fish', 'feeding', string='feeding')  # debe sacar la info del pez
    # lifecycle = fields.Many2one('ejro2122.fish', 'lifecycle', string='lifecycle')  # debe sacar la info del pez
    # transferdate = fields.Datetime('Datetime', default=fields.datetime.now())
    # fishingdate = fields.Datetime('Datetime', default=fields.datetime.now())  # Hacer el calculo
    # oncharge = fields.Many2many('hr.employee', string='Employee')

    # @api.depends('lifecycle', 'transferdate')
    # def _fishing_date(self):
    #     for record in self:
    #         record.fishingdate = record.transferdate + timedelta(days=record.lifecycle)
