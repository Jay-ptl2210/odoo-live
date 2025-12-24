from odoo import models, fields


class YantraOtherSpecification(models.Model):
    _name = 'yantra.other.specification'
    _description = 'Other Machine Specification'

    cnc_controller = fields.Char(
        string="CNC Controller",
        required=True
    )

    positional_accuracy = fields.Char(
        string="Positional Accuracy"
    )

    spindle_motor = fields.Char(
        string="Spindle Motor"
    )

    driving_motor = fields.Char(
        string="Driving Motor"
    )

    machine_category = fields.Char(
        string="Machine Category"
    )
