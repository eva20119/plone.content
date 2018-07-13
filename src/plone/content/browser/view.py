# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from email.mime.text import MIMEText
from plone.content.browser.basic_inform_configlet import IInform
import json
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from zope.globalrequest import getRequest
from plone.content.browser.basic_inform_configlet import IInform


class CoverView(BrowserView):
    template = ViewPageTemplateFile('template/cover_view.pt')
    def __call__(self):
        return self.template()


class NewsDetail(BrowserView):
    template = ViewPageTemplateFile('template/news_detail.pt')
    def __call__(self):
        return self.template()


class ContactUs(BrowserView):
    template = ViewPageTemplateFile('template/contact_us.pt')
    def __call__(self):
        self.email = api.portal.get_registry_record('email', interface=IInform, default=u'')
        self.address = api.portal.get_registry_record('address', interface=IInform, default=u'')
        self.cellphone = api.portal.get_registry_record('cellphone', interface=IInform, default=u'')
        self.fax = api.portal.get_registry_record('fax', interface=IInform, default=u'')
        return self.template()


class ProductDetail(BrowserView):
    template = ViewPageTemplateFile('template/product_detail.pt')
    def __call__(self):
        return self.template()



class AboutUs(BrowserView):
    template = ViewPageTemplateFile('template/about_us.pt')
    def __call__(self):
        return self.template()

