#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import sys

# Can't just import bdc, because dependencies have to be satisfied
# first. So, we'll "grep" for the VERSION.

source = "bdc/bdc.py"

version = None
version_re = re.compile(r'''^\s*VERSION\s*=\s*['"]?([\d.]+)["']?.*$''')
with open(source) as f:
    for line in f:
        m = version_re.match(line)
        if m:
            version = m.group(1)
            break

if not version:
    sys.stderr.write("Can't find version in {0}\n".format(source))
    sys.exit(1)

setup(
    name='bdc',
    packages=['bdc'],
    version=version,
    description='Build Databricks Course (curriculum build tool)',
    install_requires=['docopt >= 0.6.2',
                      'future >= 0.15.2',
                      'markdown2 >= 2.3.1',
                      'backports.tempfile >= 1.0rc1',
                      'grizzled-python >= 1.1.0',
                      'PyYAML >= 3.11'],
    author='Databricks Education Team',
    author_email='training-logins@databricks.com',
    entry_points={
        'console_scripts': [
            'bdc=bdc:main'
        ]
    },
    classifiers=[],
)
