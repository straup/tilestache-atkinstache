#!/usr/bin/env python

from distutils.core import setup

version = open('VERSION', 'r').read().strip()

setup(name='atkinstache',
      version=version,
      description='dot dot dot dot dot dot (and so on)',
      author='Aaron Straup Cope',
      author_email='straup@gmail.com',
      url='https://github.com/straup/tilestache-atkinstache',
      requires=['TileStache','ModestMaps', 'PIL'],
      packages=['atkinstache',
                'atkinstache.dithering'],
      scripts=[],
      data_files=[],
      download_url='',
      license='BSD')
