# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-skeleton',
    version="0.1.0",
    author='wongxinjie',
    author_email='wongxinjierun@gmail.com',
    description='django project skeleton creator',
    packages=find_packages(exclude=["tests", "etc"]),
    license='MIT',
    scripts=['bin/django-skeleton'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
