# -*- coding: utf-8 -*-
from plone.content import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form


class IInform(Form.Schema):

    email = schema.TextLine(
        title=_(u'email'),
	default=u'',
        required=False,
    )
    cellphone = schema.TextLine(
        title=_(u'cellphone'),
        default=u'',
        required=False,
    )
    address = schema.TextLine(
        title=_(u'address'),
        default=u'',
        required=False
    )
    fax = schema.TextLine(
        title=_(u'fax'),
        default=u'',
        required=False
    )
    company = schema.TextLine(
        title=_(u'company'),
        default=u'',
        required=False
    )

class BasicInformControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IInform

CustomControlPanelView = layout.wrap_form(BasicInformControlPanelForm, ControlPanelFormWrapper)
CustomControlPanelView.label = _(u"Basic Inform")


