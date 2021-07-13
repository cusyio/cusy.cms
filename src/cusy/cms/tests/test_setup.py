# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from cusy.cms.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Validate that `cusy.cms` is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Validate that `cusy.cms` is installed."""
        self.assertTrue(self.installer.isProductInstalled("cusy.cms"))

    def test_browserlayer(self):
        """Validate that the browser layer is registered."""
        from cusy.cms.interfaces import ICusyCmsLayer
        from plone.browserlayer import utils

        self.assertIn(ICusyCmsLayer, utils.registered_layers())

    def test_collective_easyform_installed(self):
        """Validate that `collective.easyform` is installed."""
        self.assertTrue(self.installer.isProductInstalled("collective.easyform"))

    def test_cusy_exportimport_installed(self):
        """Validate that `cusy.exportimport` is installed."""
        self.assertTrue(self.installer.isProductInstalled("cusy.exportimport"))

    def test_cusy_restapi_easyform_installed(self):
        """Validate that `cusy.restapi.easyform` is installed."""
        self.assertTrue(self.installer.isProductInstalled("cusy.restapi.easyform"))

    def test_cusy_restapi_info_installed(self):
        """Validate that `cusy.restapi.info` is installed."""
        self.assertTrue(self.installer.isProductInstalled("cusy.restapi.info"))

    def test_cusy_restapi_patches_installed(self):
        """Validate that `cusy.restapi` is installed."""
        self.assertTrue(self.installer.isProductInstalled("cusy.restapi.patches"))

    def test_plone_restapi_installed(self):
        """Validate that `plone.restapi` is installed."""
        self.assertTrue(self.installer.isProductInstalled("plone.restapi"))


class TestUninstall(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["cusy.cms"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Validate that `cusy.cms` is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("cusy.cms"))

    def test_browserlayer_removed(self):
        """Validate that the browser layer is removed."""
        from cusy.cms.interfaces import ICusyCmsLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICusyCmsLayer, utils.registered_layers())
