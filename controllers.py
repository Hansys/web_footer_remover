# -*- coding: utf-8 -*-
from openerp import http

# class WebFooterRemover(http.Controller):
#     @http.route('/web_footer_remover/web_footer_remover/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_footer_remover/web_footer_remover/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_footer_remover.listing', {
#             'root': '/web_footer_remover/web_footer_remover',
#             'objects': http.request.env['web_footer_remover.web_footer_remover'].search([]),
#         })

#     @http.route('/web_footer_remover/web_footer_remover/objects/<model("web_footer_remover.web_footer_remover"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_footer_remover.object', {
#             'object': obj
#         })