# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.vocabularies.catalog import CatalogSource
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from z3c.form import validator
from plone.directives import form
import zope.component
import zope.interface
from zope.interface import Invalid
from zope.interface import invariant
from zope import schema
from zope.interface import implementer
from plone.content import _
import datetime


class IProduct(model.Schema):
    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )
    price = schema.Int(
        title=_(u'Price'),
        description=_(u'Enter USD$'),
        required=True,
    )

    salePrice = schema.Int(
        title=_(u'Sale Price'),
        description=_(u'Enter USD$'),
        required=False
    )
    @invariant
    def price_invariant(data):
        if data.price < data.salePrice:
            raise Invalid(_(u'The sale price is bigger than price!'))
    cover = namedfile.NamedBlobImage(
        title=_(u'Cover Image'),
        required=True,
    )
    brand = schema.TextLine(
        title=_(u'Brand'),
        required=True
    )

    availability = schema.Bool(
        title=(u'Availability'),
        default=True,
        required=False
    )
    category = schema.TextLine(
        title=_(u'Category'),
        required=True
    )

    subcategory = schema.TextLine(
        title=_(u'Subcategory'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        required=False
    )




@implementer(IProduct)
class Product(Item):
    """
    """
