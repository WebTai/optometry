from odoo import models, fields, api

class optometrist(models.Model):
    _name = 'optometry.store'
    _description = 'optometry.store'

    # image_id = fields.Image(related='store_id.image_1920',string="Image")
    store_id = fields.Many2one('res.company',string="店名")
    lience_id = fields.Char(string="執照號碼")
    pic = fields.Binary(string="執業執照")

    def name_get(self):
        result = []
        for rec in self:
            name = rec.store_id.name
            result.append((rec.id, name))
        return result
    