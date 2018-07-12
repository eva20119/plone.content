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


class AboutUs(BrowserView):
    template = ViewPageTemplateFile('template/about_us.pt')
    def __call__(self):
        return self.template()
