from unicodedata import decimal
from odoo import fields, models
from datetime import timedelta, date

class RealEstate(models.Model):

    _name = "estate.property.type"
    _description = "Contains the festate property types"

    name = fields.Char(required=True)



