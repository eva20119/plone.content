# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from plone import api
from plone.content.browser.basic_inform_configlet import IInform


class CoverBanner(base.ViewletBase):
    def update(self):
        portal = api.portal.get()
        bannerList = portal['banner'].getChildNodes()
        self.bannerList = bannerList


class CoverNews(base.ViewletBase):
    def update(self):
	portal = api.portal.get()
        newsBrain = api.content.find(context=portal['news'], portal_type='News Item', sort_limit=5)
        self.newsBrain = newsBrain


class CoverNewProduct(base.ViewletBase):
    def update(self):
        portal = api.portal.get()
        productBrain = api.content.find(context=portal['products'], portal_type='Product', sort_limit=5)
        self.productBrain = productBrain


class CoverAd(base.ViewletBase):
    def update(self):
        """"""


class CoverTriple(base.ViewletBase):
    def update(self):
        """"""

class NewFooter(base.ViewletBase):
    def update(self):
        self.email = api.portal.get_registry_record('email', interface=IInform, default=u'')
        self.cellphone = api.portal.get_registry_record('cellphone', interface=IInform, default=u'')
        self.address = api.portal.get_registry_record('address', interface=IInform, default=u'')
        self.fax = api.portal.get_registry_record('fax', interface=IInform, default=u'')
        self.company = api.portal.get_registry_record('company', interface=IInform, default=u'')


