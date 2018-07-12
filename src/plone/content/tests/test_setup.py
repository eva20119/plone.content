# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.content.testing import PLONE_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone.content is properly installed."""

    layer = PLONE_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.content'))

    def test_browserlayer(self):
        """Test that IPloneContentLayer is registered."""
        from plone.content.interfaces import (
            IPloneContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plone.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.content'))

    def test_browserlayer_removed(self):
        """Test that IPloneContentLayer is removed."""
        from plone.content.interfaces import \
            IPloneContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneContentLayer,
            utils.registered_layers())
