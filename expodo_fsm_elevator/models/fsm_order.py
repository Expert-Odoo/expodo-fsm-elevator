from odoo import models, fields


class FsmOrder(models.Model):
    _inherit = "expodo.fsm.order"

    # Equipment
    lift_type = fields.Selection(
        [
            ("traction", "Traction (geared / gearless)"),
            ("hydraulic", "Hydraulic"),
            ("mrl", "Machine-room-less (MRL)"),
            ("goods", "Goods / freight lift"),
            ("platform", "Platform / accessibility lift"),
            ("escalator", "Escalator"),
            ("moving_walk", "Moving walkway"),
            ("dumbwaiter", "Dumbwaiter"),
            ("other", "Other"),
        ],
        string="Equipment Type",
    )
    lift_brand = fields.Char(string="Brand")
    lift_model = fields.Char(string="Model Reference")
    serial_number = fields.Char(string="Serial / Unit No.", index=True)
    building = fields.Char(string="Building / Site")
    machine_location = fields.Char(
        string="Machine Room Location", help="Where the machinery is installed"
    )

    # Specifications
    capacity_kg = fields.Integer(string="Capacity (kg)")
    capacity_persons = fields.Integer(string="Capacity (persons)")
    floors_served = fields.Integer(string="Floors Served")
    travel_height_m = fields.Float(string="Travel Height (m)")
    install_date = fields.Date(string="Install Date")

    # Regulatory inspection
    last_inspection_date = fields.Date(string="Last Inspection")
    next_inspection_date = fields.Date(
        string="Next Inspection Due", help="Date the next periodic inspection is due"
    )
    inspection_body = fields.Char(
        string="Inspection Body", help="Notified body or inspector in charge"
    )
    compliance_ref = fields.Char(string="Compliance Certificate Ref")

    # Safety checks
    brake_test_done = fields.Boolean(string="Brake Test Passed")
    governor_test_done = fields.Boolean(string="Overspeed Governor Tested")
    door_interlock_ok = fields.Boolean(string="Door Interlocks OK")
    emergency_phone_ok = fields.Boolean(string="Emergency Phone / Alarm OK")
    leveling_ok = fields.Boolean(string="Levelling OK")
