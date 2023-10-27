from odoo import http
from odoo.http import request
import base64


class WebsiteForm(http.Controller):
    @http.route(['/exam_results/<string:batch_id>/<string:user_id>'], type='http', auth="public", website=True)
    def appointment(self, batch_id, user_id):
        decoded_bytes = base64.b64decode(user_id)
        user_id = int.from_bytes(decoded_bytes, byteorder='big')

        decoded_batch = base64.b64decode(batch_id)
        batch_id = int.from_bytes(decoded_batch, byteorder='big')

        print(user_id, 'user')
        batch_name = request.env['logic.base.batch'].sudo().search([('id', '=', batch_id)])
        current_user = request.env['res.users'].sudo().search([('id', '=', int(user_id))])
        #
        print(batch_name.name, 'batch', current_user.id, 'c_user')
        # current_user = request.env['res.users'].sudo().browse(user)

        values = {
            'batch_id': batch_id,
            'batch_name': batch_name.name,
            'user': current_user.name,
            'u_id': current_user.id

        }
        return request.render("logic_results.logic_exams_result_template", values)

    @http.route(['/exam_results/submit'], type='http', auth="user", website=True)
    def action_get_data(self, **kw):
        print(kw, 'poo')
        updated_image = base64.b64encode(kw.get('student_photo').read())
        result_sc = base64.b64encode(kw.get('result_screenshot').read())
        request.env['logic.exam.results'].sudo().create({
            'name': kw.get('student_name'),
            'phone_number': kw.get('phone'),
            'batch_id': kw.get('batch_id'),
            'campus_name': kw.get('campus_name'),
            'class_teacher_id': kw.get('class_teacher_name'),
            'group': kw.get('group'),
            'mode_of_study': kw.get('mode_of_study'),
            'qualification_status': kw.get('qualification_status'),
            'updated_photo': updated_image,
            'result_screenshot': result_sc,

        })
        return request.render("logic_results.tmp_logic_exam_results")