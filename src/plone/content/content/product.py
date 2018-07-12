# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer


class IProduct(model.Schema):
    """ Marker interface for Product
    """


@implementer(IProduct)
class Product(Item):
    """
    """
