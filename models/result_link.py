from odoo import fields, models, api, _
import base64


class ResultLinkWizard(models.TransientModel):
    _name = 'result.link.wizard'
    _description = 'Result Link Wizard'

    batch_id = fields.Many2one('logic.base.batch', string='Batch')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)

    @api.depends('batch_id')
    def _compute_link(self):
        for rec in self:
            if rec.batch_id:
                batch_name = rec.batch_id.id
                batch = batch_name.to_bytes((batch_name.bit_length() + 7) // 8, byteorder='big')
                batch_id = base64.b64encode(batch).decode('utf-8')

                value = self.env.user.id
                user = value.to_bytes((value.bit_length() + 7) // 8, byteorder='big')
                user_id = base64.b64encode(user).decode('utf-8')
                rec.link = rec.company_id.website + "/" + 'exam_results' + '/' + str(batch_id) + "/" + str(user_id)
            else:
                rec.link = ''

    link = fields.Char(string='Link', compute='_compute_link', store=True, readonly=False)

    def action_copy_link(self):
        print('hi')
