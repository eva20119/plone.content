# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from email.mime.text import MIMEText
import json
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from zope.globalrequest import getRequest
from plone.content.browser.basic_inform_configlet import IInform


class SubscribeMail(BrowserView):
    def __call__(self):
        request = self.request
        portal = api.portal.get()
        email = request.get('email')
        content = api.content.find(context=portal['subscribe'], portal_type="Document")[0]
        content.getObject().description += email + ','
        request.response.redirect(portal.absolute_url())


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


class SendMail(BrowserView):
    def __call__(self):
        request = self.request
        name = request.get('name')
        email = request.get('email')
        msg = request.get('msg')

        body_str = """Name:{}<br/>Email:{}<br/>Message:{}""".format(name, email, msg)
        mime_text = MIMEText(body_str, 'html', 'utf-8')
        api.portal.send_email(
            recipient="ah13441673@gmail.com",
            sender="henry@mingtak.com.tw",
            subject="Contact Us",
            body=mime_text.as_string(),
        )
        api.portal.show_message(message='發送成功!'.decode('utf-8'), request=request)

