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
        title=_(u'Subject'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        required=False
    )

    fieldset(_('Set Image'), fields=['cover1', 'cover2', 'innerCover1', 'innerCover2', 'innerCover3', 'innerCover4', 'innerCover5', 'innerCover6'])
    cover1 = namedfile.NamedBlobImage(
        title=_(u'Cover1 Image'),
        required=True,
    )
    cover2 = namedfile.NamedBlobImage(
        title=_(u'Cover2 Image'),
        required=False,
    )
    innerCover1 = namedfile.NamedBlobImage(
        title=_(u'innerCover1 Image'),
        required=False,
    )
    innerCover2 = namedfile.NamedBlobImage(
        title=_(u'innerCover2 Image'),
        required=False,
    )
    innerCover3 = namedfile.NamedBlobImage(
        title=_(u'innerCover3 Image'),
        required=False,
    )
    innerCover4 = namedfile.NamedBlobImage(
        title=_(u'innerCover4 Image'),
        required=False,
    )
    innerCover5 = namedfile.NamedBlobImage(
        title=_(u'innerCover5 Image'),
        required=False,
    )
    innerCover6 = namedfile.NamedBlobImage(
        title=_(u'innerCover6 Image'),
        required=False,
    )



@implementer(IProduct)
class Product(Item):
    """
    """
