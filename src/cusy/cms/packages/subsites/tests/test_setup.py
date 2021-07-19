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
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.installProducts(["cusy.cms.packages.subsites"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_installed(self):
        """Validate that `cusy.cms.packages.subsites` is installed."""
        self.assertTrue(self.installer.isProductInstalled("cusy.cms.packages.subsites"))

    def test_browserlayer(self):
        """Validate that the browser layer is registered."""
        from cusy.cms.packages.subsites.interfaces import ICusyCmsSubsitesLayer
        from plone.browserlayer import utils

        self.assertIn(ICusyCmsSubsitesLayer, utils.registered_layers())

    def test_collective_lineage_installed(self):
        """Validate that `collective.lineage` is installed."""
        self.assertTrue(
            self.installer.isProductInstalled("collective.lineage"),
        )

    def test_lineage_controlpanels_installed(self):
        """Validate that `lineage.controlpanels` is installed."""
        self.assertTrue(self.installer.isProductInstalled("lineage.controlpanels"))

    def test_lineage_registry_installed(self):
        """Validate that `lineage.registry` is installed."""
        self.assertTrue(self.installer.isProductInstalled("lineage.registry"))

    def test_lineage_themeselection_installed(self):
        """Validate that `lineage.themeselection` is installed."""
        self.assertTrue(self.installer.isProductInstalled("lineage.themeselection"))


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
        self.installer.installProducts(["cusy.cms.packages.subsites"])
        self.installer.uninstallProducts(["cusy.cms.packages.subsites"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Validate that `cusy.cms.packages.subsites` is cleanly uninstalled."""
        self.assertFalse(
            self.installer.isProductInstalled("cusy.cms.packages.subsites")
        )

    def test_browserlayer_removed(self):
        """Validate that the browser layer is removed."""
        from cusy.cms.packages.subsites.interfaces import ICusyCmsSubsitesLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICusyCmsSubsitesLayer, utils.registered_layers())
