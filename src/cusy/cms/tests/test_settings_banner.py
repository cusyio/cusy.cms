# -*- coding: utf-8 -*-
"""Test banner settings."""

from cusy.cms import testing

import plone.api
import unittest


class TestBannerSettings(unittest.TestCase):
    """Validate banner settings."""

    layer = testing.INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer["portal"]

    def test_banner_scale(self):
        """Validate the 'banner_scale' setting."""
        setting = plone.api.portal.get_registry_record(
            "collective.behavior.banner.browser.controlpanel.IBannerSettingsSchema.banner_scale",
        )
        self.assertEqual(setting, "banner_md")
