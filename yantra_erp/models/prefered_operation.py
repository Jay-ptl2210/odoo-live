from odoo import models, fields, api


class PreferedOperation(models.Model):
    _name = 'yantra.prefered.operation'
    _description = 'Prefered Operation'
    _rec_name = 'value'

    # ONLY ONE FIELD
    value = fields.Char(
        string="Prefered Operation",
        required=True
    )
    
    _sql_constraints = [
        (
            'unique_prefered_operation',
            'unique(value)',
            'This prefered operation is already exists!'
        )
    ]

    # AUTO CREATE DEFAULT VALUES
    @api.model
    def _create_default_prefered_operation(self):
        values = ['Drilling',"Milling","Turning"]
        for val in values:
            if not self.search([('value', '=', val)], limit=1):
                self.create({'value': val})

    # RUN ON INSTALL / UPGRADE
    @api.model
    def init(self):
        self._create_default_prefered_operation()
    
    
