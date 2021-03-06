# -*- coding: utf-8 -*-
"""Installer for the cusy.cms package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="cusy.cms",
    version="1.0.0.dev0",
    description="Cusy CMS Policy",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Thomas Massmann",
    author_email="thomas.massmann@it-spir.it",
    url="https://github.com/cusyio/cusy.cms",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/cusy.cms",
        "Source": "https://github.com/cusyio/cusy.cms",
        "Tracker": "https://github.com/cusyio/cusy.cms/issues",
        # 'Documentation': 'https://cusy.cms.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["cusy"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        "setuptools",
        "collective.behavior.banner",
        "collective.easyform",
        "collective.lineage",
        "cusy.exportimport",
        "cusy.patches.cmfplone",
        "cusy.restapi.easyform",
        "cusy.restapi.info",
        "cusy.restapi.patches",
        "lineage.controlpanels",
        "lineage.registry",
        "lineage.themeselection",
        "plone.restapi",
        "z3c.jbot",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
