# -*- coding: utf-8 -*-
# from odoo import http


# class Ejro2122(http.Controller):
#     @http.route('/ejro2122/ejro2122', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejro2122/ejro2122/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejro2122.listing', {
#             'root': '/ejro2122/ejro2122',
#             'objects': http.request.env['ejro2122.ejro2122'].search([]),
#         })

#     @http.route('/ejro2122/ejro2122/objects/<model("ejro2122.ejro2122"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejro2122.object', {
#             'object': obj
#         })
