#!/usr/bin/env python

from distutils.core import setup

setup(name='Tw00ny',
      version='0.1',
      description='port of web2py libs to pyramid (includes copy of modules from the web2py framework)',
      author='Jefta Harlingen',
      author_email='jefta.harlingen@gmail.com',
      license='lgpl',
      url='https://github.com/twister077/twoony',
      packages=['gluon'],
      package_dir={'gluon': 'gluon'},
      )

