from core import *


def test_Property_init_():

    p = Property('small cabin', 5, 100, 150)

    assert p.name == 'small cabin'
    assert p.stock == 5
    assert p.rent == 100
    assert p.replacement == 150


def test_Property_rent():

    p = Property('small cabin', 5, 100, 150)

    assert p.rent == 100


def test_Property_matches_name():

    p = Property('small cabin', 5, 100, 150)

    assert p.name == 'small cabin'


def test_Property_str():

    p = Property('small cabin', 5, 100, 150)

    assert p.__str__() == 'small cabin: $100 per month'


def test_inventory_init_():
    properties = [
        Property('small cabin', 5, 100, 150),
        Property('medium cabin', 6, 150, 200),
        Property('large cabin', 3, 300, 400),
        Property('studio apartment', 4, 150, 200),
        Property('medium apartment', 3, 200, 300),
        Property('penthouse', 1, 400, 800)
    ]

    inv = Inventory(properties)

    assert inv.properties == properties


def test_inventory_str():

    properties = [
        Property('small cabin', 5, 100, 150),
        Property('medium cabin', 6, 150, 200),
        Property('large cabin', 3, 300, 400),
        Property('studio apartment', 4, 150, 200),
        Property('medium apartment', 3, 200, 300),
        Property('penthouse', 1, 400, 800)
    ]

    inv = Inventory(properties)

    assert inv.__str__(
    ) == 'Properties:\nsmall cabin: $100 per month\nmedium cabin: $150 per month\nlarge cabin: $300 per month\nstudio apartment: $150 per month\nmedium apartment: $200 per month\npenthouse: $400 per month'


def test_rental_init():

    R = Rental('timothy', ['small cabin'], '3', 'rent')

    assert R.name == 'timothy'
    assert R.items == ['small cabin']
    assert R.length == '3'
    assert R.type == 'rent'


def test_rental_str():

    R = Rental('timothy', [Property('small cabin', 5, 100, 150)], '3', 'R')

    assert R.__str__(
    ) == '-----------------\nType: R\nCustomer: timothy\nDeposit: 15.0\nTotal: $336.00 for 3 months\nProperty: \nsmall cabin: $100 per month\n-----------------'
