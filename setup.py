#!/usr/bin/env python
import os.path
import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages

setup(
    name='webhook',
    maintainer="Rick van den Hof",
    maintainer_email='r.vandenhof@exonet.nl',
    url='https://github.com/exonet/ansible-tower-webhook',
    description='Launch jobs in Ansible Tower when pull requests are merged.',
    long_description='foo',
    license='MIT',
    keywords='ansible tower github webhook template job',
    install_requires=[
        'Flask>=0.10.1',
    ],
    classifiers=[
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta'
    ],
    provides=[
        'webhook',
    ],
    package_dir={
        '': 'lib',
    },
    packages=['webhook'],
    setup_requires=['setuptools_scm', 'pytest-flask'],
    tests_require=['tox'],
    entry_points={'console_scripts': ['webhook = webhook:main']},
)
