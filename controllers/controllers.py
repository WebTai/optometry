# -*- coding: utf-8 -*-
# from odoo import http


# class Optometry(http.Controller):
#     @http.route('/optometry/optometry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/optometry/optometry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('optometry.listing', {
#             'root': '/optometry/optometry',
#             'objects': http.request.env['optometry.optometry'].search([]),
#         })

#     @http.route('/optometry/optometry/objects/<model("optometry.optometry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('optometry.object', {
#             'object': obj
#         })
