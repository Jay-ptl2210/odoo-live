from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # ---------------- MEASUREMENTS ----------------
    height_id = fields.Many2one(
        'yantra.measurement',
        related='product_tmpl_id.height_id',
        store=True,
        readonly=False
    )

    width_id = fields.Many2one(
        'yantra.measurement',
        related='product_tmpl_id.width_id',
        store=True,
        readonly=False
    )

    length_id = fields.Many2one(
        'yantra.measurement',
        related='product_tmpl_id.length_id',
        store=True,
        readonly=False
    )

    drill_dia_id = fields.Many2one(
        'yantra.measurement',
        related='product_tmpl_id.drill_dia_id',
        store=True,
        readonly=False
    )

    plate_thickness_id = fields.Many2one(
        'yantra.measurement',
        related='product_tmpl_id.plate_thickness_id',
        store=True,
        readonly=False
    )

    # ---------------- SPINDLE ----------------
    spindle_type_id = fields.Many2one(
        'yantra.spindle.type',
        related='product_tmpl_id.spindle_type_id',
        store=True,
        readonly=False
    )

    spindle_motor_power_id = fields.Many2one(
        'yantra.spindle.motor.power',
        related='product_tmpl_id.spindle_motor_power_id',
        store=True,
        readonly=False
    )

    spindle_rpm_id = fields.Many2one(
        'yantra.spindle.rpm',
        related='product_tmpl_id.spindle_rpm_id',
        store=True,
        readonly=False
    )

    # ---------------- MACHINE ----------------
    machine_structure_id = fields.Many2one(
        'yantra.machine.structure',
        related='product_tmpl_id.machine_structure_id',
        store=True,
        readonly=False
    )

    prefered_operation_id = fields.Many2one(
        'yantra.prefered.operation',
        related='product_tmpl_id.prefered_operation_id',
        store=True,
        readonly=False
    )

    # ---------------- OTHER SPECIFICATIONS (MANUAL ENTRY) ----------------
    cnc_controller = fields.Char(
        related='product_tmpl_id.cnc_controller',
        store=True,
        readonly=False
    )

    positional_accuracy = fields.Char(
        related='product_tmpl_id.positional_accuracy',
        store=True,
        readonly=False
    )

    spindle_motor = fields.Char(
        related='product_tmpl_id.spindle_motor',
        store=True,
        readonly=False
    )

    driving_motor = fields.Char(
        related='product_tmpl_id.driving_motor',
        store=True,
        readonly=False
    )

    machine_category = fields.Char(
        related='product_tmpl_id.machine_category',
        store=True,
        readonly=False
    )
