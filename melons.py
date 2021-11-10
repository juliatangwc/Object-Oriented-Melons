from random import randint
from datetime import datetime
from datetime import date
from pytz import timezone

"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    tax = None

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_base_price(self):
        base_price = randint(5,9)
        zone = datetime.now(timezone('EST'))
        ship_day = date.isoweekday(zone)
        ship_hour = zone.hour

        if ship_day == range(1,6) and ship_hour == range(8,11):
            base_price += 4

        return base_price


    



    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        flat_fee = 0

        if self.species == "Christmas":
            base_price = base_price*1.5

        if self.qty < 10 and self.order_type == 'international':
            flat_fee = 3



        total = (1 + self.tax) * self.qty * base_price + flat_fee

        return round(total, 2)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    # order_type = "domestic"
    # tax = 0.08

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    # order_type = "international"
    # tax = 0.17

    def __init__(self, species, qty, country_code):
        """International orders need country_code"""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    passed_inspection = False

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.0)

    def mark_passed(self):
        """Record if passes inspection."""

        self.passed_inspection = True

