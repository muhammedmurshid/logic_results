from odoo import api, fields, models, _


class ExamResults(models.Model):
    _name = 'logic.exam.results'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Exam Result'

    name = fields.Char(string='Name')
    updated_photo = fields.Binary(string='Updated Photo')
    phone_number = fields.Char(string='Phone Number')
    batch_id = fields.Many2one('logic.base.batch', string='Batch')
    campus_name = fields.Char(string='Campus Name')
    class_teacher_id = fields.Many2one('res.users', string='Class Teacher')
    group = fields.Selection([('group_one', 'Group 1'), ('group_two', 'Group 2'), ('both', 'Both')], string='Group')
    mode_of_study = fields.Selection([('online', 'Online'), ('offline', 'Offline')], string='Mode of Study')
    qualification_status = fields.Selection(
        [('semi_qualified', 'Semi Qualified'), ('fully_qualified', 'Fully Qualified'),
         ('both_qualified_in_single_window', 'Both Qualified in Single Window')], string='Qualification Status')
    result_screenshot = fields.Binary(string='Result Screenshot')
