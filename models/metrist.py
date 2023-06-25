# -*- coding: utf-8 -*-

from odoo import models, fields, api

class optometrist(models.Model):
    _name = 'optometry.optometrist'
    _description = 'optometry.optometrist'

    image_id = fields.Image(related='optometrist_id.image_1920',string="Image")
    optometrist_id = fields.Many2one('res.partner',string="驗光師")
    email = fields.Char(related='optometrist_id.email',string="Email")
    mobile = fields.Char(related='optometrist_id.mobile',string="行動電話")
    lience_id = fields.Char(string="證照號碼")
    lic = fields.Binary(string="證書")
    pic = fields.Binary(string="執業執照")

    def name_get(self):
        result = []
        for rec in self:
            name = rec.optometrist_id.name
            result.append((rec.id, name))
        return result
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
