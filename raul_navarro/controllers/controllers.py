# -*- coding: utf-8 -*-
# from odoo import http


# class RaulNavarro(http.Controller):
#     @http.route('/raul_navarro/raul_navarro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/raul_navarro/raul_navarro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('raul_navarro.listing', {
#             'root': '/raul_navarro/raul_navarro',
#             'objects': http.request.env['raul_navarro.raul_navarro'].search([]),
#         })

#     @http.route('/raul_navarro/raul_navarro/objects/<model("raul_navarro.raul_navarro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('raul_navarro.object', {
#             'object': obj
#         })
