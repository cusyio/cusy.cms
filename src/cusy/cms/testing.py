# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import cusy.cms


class CusyCmsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=cusy.cms)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cusy.cms:default')


CUSY_CMS_FIXTURE = CusyCmsLayer()


CUSY_CMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CUSY_CMS_FIXTURE,),
    name='CusyCmsLayer:IntegrationTesting',
)


CUSY_CMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CUSY_CMS_FIXTURE,),
    name='CusyCmsLayer:FunctionalTesting',
)


CUSY_CMS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CUSY_CMS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CusyCmsLayer:AcceptanceTesting',
)
