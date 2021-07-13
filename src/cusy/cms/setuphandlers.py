# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "cusy.cms:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide other products from site-creation and quickinstaller."""
        return [
            "collective.easyform",
            "cusy.exportimport",
            "cusy.restapi.easyform",
            "cusy.restapi.info",
            "cusy.restapi.patches",
            "plone.restapi",
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
