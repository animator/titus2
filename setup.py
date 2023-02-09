#!/usr/bin/env python

# Copyright (C) 2014  Open Data ("Open Data" refers to
# one or more of the following companies: Open Data Partners LLC,
# Open Data Research LLC, or Open Data Capital LLC.)
# 
# This file is part of Hadrian.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from os import path, walk
from setuptools import setup

import titus.version

### To run the tests:
# python setup.py test

### To install on a machine:
# sudo python setup.py install

### To install in a home directory (~/lib):
# python setup.py install --home=~
LONG_DESCRIPTION = open(path.join(path.dirname(__file__), 'README.md')).read()

requires = ["numpy==1.14.0; python_version < '3.6'",
            "numpy>=1.15.0, <1.20; python_version >= '3.6'", 
            "avro-python3>=1.8.2", 
            "ply>=3.11", 
            "pyyaml>=5.1.2", 
            "pytz>=2019.1"]

setup(name="titus2",
      version=titus.version.__version__,
      author="Ankit Mahato",
      author_email="ankit@realworldpython.guide",
      keywords='pfa scoring inference pmml titus hadrian machine learning data mining',
      packages=["titus",
                "titus.producer",
                "titus.lib",
                "titus.lib.model",
                "titus.lib.prob",
                "titus.lib.stat",
                "titus.inspector"],
      scripts = ["scripts/pfainspector", "scripts/pfachain", "scripts/pfaexternalize", "scripts/pfarandom", "scripts/pfasize"],
      description="Python 3 implementation of Portable Format for Analytics (PFA): producer, converter, and consumer.",
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://realworldpython.guide/titus2/",
      project_urls={
            "Source Code": "https://github.com/animator/titus2",
            "Bug Tracker": "https://github.com/animator/titus2/issues",
            "Documentation": "https://realworldpython.guide/titus2/",
      },
      test_suite="test",
      install_requires=requires,
      tests_require=requires,
      python_requires='>=3.4,<3.10',
      classifiers=[  
            'Development Status :: 5 - Production/Stable', 
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Information Technology',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',            
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Natural Language :: English',
      ],      
      )

### details of dependencies:
# 
# Tested in Python 3.4-3.9.
# Will not work in Python 2.x.
# 
# avro-python3 is required; it is an integral part of PFA.
# ply is required; it is used to parse PrettyPFA and Inspector commandlines.
# 
# PyYAML is an optional dependency; it is only used by the titus.reader.yamlToAst function.
# Numpy is an optional dependency; it is only used by the "interp", "la", "stat.test", and "model.reg" PFA libraries, as well as Titus producers.
# pytz is an optional dependency; it is only used by the "time" PFA library.
