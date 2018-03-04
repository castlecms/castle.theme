from setuptools import setup, find_packages
import os

version = '1.0.2'

setup(name='castle.theme',
      version=version,
      description="CastleCMS Theme Package",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Wildcard Corp.',
      author_email='info@wildcardcorp.com',
      url='https://github.com/castlecms/castle.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['castle'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'z3c.jbot'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
