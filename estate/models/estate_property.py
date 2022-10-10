from unicodedata import decimal
from odoo import fields, models
from datetime import timedelta, date

class RealEstate(models.Model):

    _name = "estate.property"
    _description = "Contains the fields of the real estate properties"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=date.today() + timedelta(days=90))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = "Orientation",
        selection = [("north","North"), ("south","South"), ("west","West"), ("east","East")],
        help = "Select the orientation you want to see the garden"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string = "State",
        selection = [("new","New"), ("offer_received","Offer Received"), 
                        ("offer_accepted","Offer Accepted"), ("sold","sold"), ("canceled","Canceled")],
        help = "Select state for the property",
        copy = False,
        default="new",
        required=True)
    property_type_id = fields.Many2one("estate.property.type")
    


