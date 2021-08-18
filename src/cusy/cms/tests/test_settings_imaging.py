# -*- coding: utf-8 -*-
"""Test imaging settings."""

from cusy.cms import testing

import plone.api
import unittest


class TestImagingSettings(unittest.TestCase):
    """Validate imaging settings."""

    layer = testing.INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer["portal"]

    def test_allowed_sizes(self):
        """Validate the 'allowed_sizes' setting."""
        setting = plone.api.portal.get_registry_record(
            "plone.allowed_sizes",
        )
        expected = [
            "banner 1280:720",
        ]
        for item in expected:
            self.assertIn(item, setting)
        self.assertTrue(len(setting) >= len(expected))
