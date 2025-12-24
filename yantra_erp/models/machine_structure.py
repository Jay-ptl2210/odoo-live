from odoo import models, fields, api


class MachineStructure(models.Model):
    _name = 'yantra.machine.structure'
    _description = 'Spindle Machine Structure'
    _rec_name = 'value'

    value = fields.Char(
        string="Spindle Machine Structure",
        required=True
    )

    _sql_constraints = [
        (
            'unique_machine_structure',
            'unique(value)',
            'This machine structure already exists!'
        )
    ]

    @api.model
    def _normalize_and_cleanup(self):
        # Map ALL wrong variations to ONE correct value
        normalize_map = {
            "heavy duty steel structure": "Heavy Duty Steel Structure",
            "heavy duty steel Structure": "Heavy Duty Steel Structure",
            "Heavy duty steel structure": "Heavy Duty Steel Structure",

            "semi-casted": "Semi Casted",
            "semi casted": "Semi Casted",

            "graded casting": "Graded Casting",
            " graded casting": "Graded Casting",
        }

        for rec in self.search([]):
            key = rec.value.strip().lower()
            if key in normalize_map:
                correct_value = normalize_map[key]

                # Check if correct record already exists
                existing = self.search([
                    ('value', '=', correct_value)
                ], limit=1)

                if existing and existing.id != rec.id:
                    # 🔥 DELETE DUPLICATE
                    rec.unlink()
                else:
                    # 🔥 NORMALIZE VALUE
                    rec.value = correct_value

    @api.model
    def _ensure_defaults(self):
        defaults = [
            "Heavy Duty Steel Structure",
            "Semi Casted",
            "Graded Casting",
        ]

        for val in defaults:
            if not self.search([('value', '=', val)], limit=1):
                self.create({'value': val})

    @api.model
    def init(self):
        self._normalize_and_cleanup()
        self._ensure_defaults()
