# -*- coding: utf-8 -*-

from odoo import models, fields, api

class optometry(models.Model):
    _name = 'optometry.order'
    # _inherit=['image_mixin']
    _description = 'optometry.order'

    customer_id = fields.Many2one('res.partner',string="客戶姓名")
    image_id = fields.Image(related='customer_id.image_1920',string="Image")
    optometrist_id = fields.Many2one('res.partner',string="驗光師")
    order_created = fields.Datetime(string='開單日期',default=lambda self: fields.Datetime.now())
    order_r_sph=fields.Float(string="SPH",default=0.)
    order_r_cyl=fields.Float(string="CYL",default=0.)
    order_r_axis=fields.Float(string="AXIS",default=0.)
    order_r_prsim=fields.Float(string="PRSIM",default=0.)
    order_r_bas=fields.Float(string="BAS",default=0.)
    order_l_sph=fields.Float(string="SPH",default=0.)
    order_l_cyl=fields.Float(string="CYL",default=0.)
    order_l_axis=fields.Float(string="AXIS",default=0.)
    order_l_prsim=fields.Float(string="PRSIM",default=0.)
    order_l_bas=fields.Float(string="BAS",default=0.)
    order_pd=fields.Float(string="PD",default=50.)
    order_notes = fields.Text(string='備註')

    def name_get(self):
        result = []
        for rec in self:
            name = rec.customer_id.name
            result.append((rec.id, name))
        return result
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
