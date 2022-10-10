from unicodedata import decimal
from odoo import fields, models

class RealEstate(models.Model):

    name = "estate.property"
    description = "Contains the fields of the real estate properties"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = "Orientation",
        selection = [("north","North"), ("south","South"), ("west","West"), ("east","East")],
        help = "Select the orientation you want to see the garden"
    )


