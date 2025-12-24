from odoo import models, fields, api


class SpindleRpm(models.Model):
    _name = 'yantra.spindle.rpm'
    _description = 'Spindle rpm'
    _rec_name = 'value'

    # ONLY ONE FIELD
    value = fields.Char(
        string="Spindle Rpm",
        required=True
    )
    
    _sql_constraints = [
        (
            'unique_spindle_rpm',
            'unique(value)',
            'This spindle type already exists!'
        )
    ]

    # AUTO CREATE DEFAULT VALUES
    @api.model
    def _create_default_spindle_rpm(self):
        values = [300, 4500, 6000, 8000]
        for val in values:
            if not self.search([('value', '=', val)], limit=1):
                self.create({'value': val})

    # RUN ON INSTALL / UPGRADE
    @api.model
    def init(self):
        self._create_default_spindle_rpm()
