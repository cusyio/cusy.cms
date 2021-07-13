# -*- coding: utf-8 -*-
"""Content type tests for File."""

from cusy.cms import testing
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.registration import lookup_behavior_registration
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import queryUtility

import unittest


class FileIntegrationTest(unittest.TestCase):
    """Validate the File content type."""

    layer = testing.INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer["portal"]
        self.fti = queryUtility(
            IDexterityFTI,
            name="File",
        )
        self.request = self.layer["request"]
        self.request["ACTUAL_URL"] = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])

    def tearDown(self):
        """Additional test cleanup."""
        if "file" in self.portal.objectIds():
            self.portal.manage_delObjects(ids="file")  # noqa: P001
        if "file-1" in self.portal.objectIds():
            self.portal.manage_delObjects(ids="file-1")  # noqa: P001

    def test_allow_discussion(self):
        """Validate `allow_discussion` setting."""
        self.assertTrue(self.fti.allow_discussion)

    def test_global_allow(self):
        """Validate `global_allow` setting."""
        self.assertTrue(self.fti.global_allow)

    def test_behaviors(self):
        """Validate `behaviors` setting."""
        behaviors = [
            "collective.behavior.banner",
            "plone.leadimage",
        ]
        for item in behaviors:
            self.assertIn(item, self.fti.behaviors)
        self.assertTrue(len(self.fti.behaviors) >= 2)

        missing_behaviors = []
        for item in missing_behaviors:
            self.assertNotIn(item, self.fti.behaviors)

    def test_behavior_names_used(self):
        """Validate that the content types uses behavior names."""
        for behavior in self.fti.behaviors:
            behavior_registration = lookup_behavior_registration(behavior)
            self.assertEqual(behavior_registration.name, behavior)

    def test_view_methods(self):
        """Validate `view_methods` setting."""
        for item in ["file_view"]:
            self.assertIn(item, self.fti.view_methods)
        for item in []:
            self.assertNotIn(item, self.fti.view_methods)

    def test_default_view(self):
        """Validate `default_view` setting."""
        self.assertEqual("file_view", self.fti.default_view)

    def test_default_view_fallback(self):
        """Validate `default_view_fallback` setting."""
        self.assertTrue(self.fti.default_view_fallback)
