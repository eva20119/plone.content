# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from plone import api


class CoverBanner(base.ViewletBase):
    def update(self):
        portal = api.portal.get()
        bannerList = portal['banner'].getChildNodes()
        self.bannerList = bannerList
