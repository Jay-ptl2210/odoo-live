from odoo import models, fields, api


class Measurement(models.Model):
    _name = 'yantra.measurement'
    _description = 'Measurement Master'
    _rec_name = 'value_mm'   

    measurement_type = fields.Selection([
        ('height', 'Height'),
        ('width', 'Width'),
        ('length', 'Length'),
        ('drill_dia', 'Drill Diameter'),
        ('plate_thickness', 'Plate Thickness'),
    ], required=True)

    value = fields.Integer(string="Value (mm)", required=True)

    # ✅ COMPUTED, NOT STORED (WORKS FOR OLD DATA)
    value_mm = fields.Char(
        string="Measurement",
        compute="_compute_value_mm"
    )

    _sql_constraints = [
        (
            'unique_measurement_value',
            'unique(measurement_type, value)',
            'This measurement value already exists!'
        )
    ]

    @api.depends('value')
    def _compute_value_mm(self):
        for rec in self:
            rec.value_mm = f"{rec.value} mm"

    @api.model
    def _create_default_measurements(self):
        predefined_data = {
            'height': [400, 500, 750, 1000],
            'width': [1000, 1500, 2000, 2500],
            'length': [1000, 1500, 2000, 2500],
            'drill_dia': [20, 32, 40, 50, 52, 65, 85],
            'plate_thickness': [80, 120, 250, 350],
        }

        for m_type, values in predefined_data.items():
            for val in values:
                if not self.search([
                    ('measurement_type', '=', m_type),
                    ('value', '=', val)
                ], limit=1):
                    self.create({
                        'measurement_type': m_type,
                        'value': val
                    })

    @api.model
    def init(self):
        self._create_default_measurements()
