from odoo import models, fields, api


class SpindleType(models.Model):
    _name = 'yantra.spindle.type'
    _description = 'Spindle Type'
    _rec_name = 'value'

    # ONLY ONE FIELD
    value = fields.Char(
        string="Spindle Type",
        required=True
    )
    
    _sql_constraints = [
        (
            'unique_spindle_type',
            'unique(value)',
            'This spindle type already exists!'
        )
    ]

    # AUTO CREATE DEFAULT VALUES
    @api.model
    def _create_default_spindle_types(self):
        values = ['BT-40', 'BT-50']
        for val in values:
            if not self.search([('value', '=', val)], limit=1):
                self.create({'value': val})

    # RUN ON INSTALL / UPGRADE
    @api.model
    def init(self):
        self._create_default_spindle_types() 

        


