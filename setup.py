# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='hmc_8043',
      version = '0.2.0',
      description = '',
      long_description = '',
      author = 'Philipp Klaus',
      author_email = 'klaus@physik.uni-frankfurt.de',
      url = '',
      license = 'GPL',
      packages = ['hmc_8043'],
      scripts = ['scripts/hmc-8043-shell'],
      zip_safe = True,
      platforms = 'any',
      requires = ['python_vxi11'],
      keywords = 'R&D HMC 8043 power supply',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GPL License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Logging',
      ]
)


