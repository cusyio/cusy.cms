.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/cusyio/cusy.cms/workflows/ci/badge.svg
    :target: https://github.com/cusyio/cusy.cms/actions
    :alt: CI Status

.. image:: https://codecov.io/gh/cusyio/cusy.cms/branch/main/graph/badge.svg?token=KL4QL32DJR
    :target: https://codecov.io/gh/cusyio/cusy.cms
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/v/cusy.cms.svg
    :target: https://pypi.python.org/pypi/cusy.cms/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/cusy.cms.svg
    :target: https://pypi.python.org/pypi/cusy.cms
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/cusy.cms.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/cusy.cms.svg
    :target: https://pypi.python.org/pypi/cusy.cms/
    :alt: License


========
cusy.cms
========

The main policy package to install the Cusy CMS.


Features
--------

Dependencies
------------

``cusy.cms`` depends on and installs the following add-ons:

- `collective.behavior.banner <https://github.com/collective/collective.behavior.banner>`_:
  Add banners and create slider/carousel from banners.
- `collective.easyform <https://github.com/collective/collective.easyform>`_:
  Form Builder for Plone.
- `cusy.exportimport <https://github.com/cusyio/cusy.exportimport>`_:
  Extensions and patches for collective.exportimport.
- `cusy.restapi.easyform <https://github.com/cusyio/cusy.restapi.easyform>`_:
  EasyForm integration for plone.restapi.
- `cusy.restapi.info <https://github.com/cusyio/cusy.restapi.info>`_:
  Site and content info for plone.restapi.
- `cusy.restapi.patches <https://github.com/cusyio/cusy.restapi.patches>`_:
  Patches and fixes for plone.restapi which are not yet released.
- `plone.restapi <https://github.com/plone/plone.restapi>`_:
  RESTful hypermedia API for Plone.


``cusy.cms`` also depends on the following add-ons, but does not install them by default:

- `collective.lineage <https://github.com/collective/collective.lineage>`_:
  Turns subfolders of a Plone site to appear as autonomous Plone sites.


Installation
------------

Install ``cusy.cms`` by adding it to your buildout::

    [buildout]

    ...

    eggs =
        cusy.cms


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/cusyio/cusy.cms/issues
- Source Code: https://github.com/cusyio/cusy.cms


Support
-------

If you are having issues, please let us know by adding a new ticket.


License
-------

The project is licensed under the GPLv2.
