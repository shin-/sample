#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'six >= 1.4.0',
]

extras_require = {}

version = "1.0.0"


long_description = 'This is a sample app'

setup(
    name="sample",
    version=version,
    description="This is a sample app.",
    long_description=long_description,
    url='https://github.com/shin-/sample',
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=requirements,
    extras_require=extras_require,
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
    maintainer='Joffrey F',
    maintainer_email='joffrey@docker.com',
)
