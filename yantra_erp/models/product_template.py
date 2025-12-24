from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # ---------------- MEASUREMENTS ----------------
    height_id = fields.Many2one(
        'yantra.measurement',
        string="Height",
        domain="[('measurement_type','=','height')]"
    )

    width_id = fields.Many2one(
        'yantra.measurement',
        string="Width",
        domain="[('measurement_type','=','width')]"
    )

    length_id = fields.Many2one(
        'yantra.measurement',
        string="Length",
        domain="[('measurement_type','=','length')]"
    )

    drill_dia_id = fields.Many2one(
        'yantra.measurement',
        string="Drill Diameter",
        domain="[('measurement_type','=','drill_dia')]"
    )

    plate_thickness_id = fields.Many2one(
        'yantra.measurement',
        string="Plate Thickness",
        domain="[('measurement_type','=','plate_thickness')]"
    )

    # ---------------- SPINDLE ----------------
    spindle_type_id = fields.Many2one(
        'yantra.spindle.type',
        string="Spindle Type"
    )

    spindle_motor_power_id = fields.Many2one(
        'yantra.spindle.motor.power',
        string="Spindle Motor Power"
    )

    spindle_rpm_id = fields.Many2one(
        'yantra.spindle.rpm',
        string="Spindle RPM"
    )

    # ---------------- MACHINE STRUCTURE ----------------
    machine_structure_id = fields.Many2one(
        'yantra.machine.structure',
        string="Machine Structure"
    )

    # ---------------- PREFERED OPERATION ----------------
    prefered_operation_id = fields.Many2one(
        'yantra.prefered.operation',
        string="Prefered Operation"
    )

    # ---------------- OTHER SPECIFICATIONS (MANUAL ENTRY) ----------------
    cnc_controller = fields.Char(
        string="CNC Controller"
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
