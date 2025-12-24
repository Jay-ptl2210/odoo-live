from odoo import models, fields, api


class SpindleMotorPower(models.Model):
    _name = 'yantra.spindle.motor.power'
    _description = 'Spindle Motor Power'
    _rec_name = 'value'

    # ONLY ONE FIELD
    value = fields.Char(
        string="Spindle Motor Power",
        required=True
    )
    
    _sql_constraints = [
        (
            'unique_spindle_motor_power',
            'unique(value)',
            'This spindle type already exists!'
        )
    ]

    # AUTO CREATE DEFAULT VALUES
    @api.model
    def _create_default_spindle_motor_powers(self):
        values = ['5.5/7.5 KW', '7.5/11 KW', '11/15 KW','15/18 KW','18/22 KW','22/26 KW','26/30 KW','30/37 KW']
        for val in values:
            if not self.search([('value', '=', val)], limit=1):
                self.create({'value': val})

    # RUN ON INSTALL / UPGRADE
    @api.model
    def init(self):
        self._create_default_spindle_motor_powers()
