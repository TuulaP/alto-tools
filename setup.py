#!/usr/bin/env python

import codecs

from setuptools import setup

setup(
   name='alto-tools',
   version='0.0.1',
   description='Simple methods to perform operations on ALTO xml files',
   long_description=codecs.open('README.md', encoding='utf-8').read(),
   long_description_content_type='text/markdown',
   license='Apache License 2.0',
   url='https://github.com/cneud/alto-tools',
   author='Clemens Neudecker',
   author_email='cneud@tuta.io',
   packages=['alto-tools'],
   install_requires=['lxml'],
   # scripts=[
   #          'scripts/alto_ocr_text',
   #          'scripts/alto_ocr_confidence',
   #          'scripts/alto_ocr_metadata'
   #         ]
)