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

from setuptools import setup

import titus.version

### To run the tests:
# python setup.py test

### To install on a machine:
# sudo python setup.py install

### To install in a home directory (~/lib):
# python setup.py install --home=~

setup(name="titus",
      version=titus.version.__version__,
      author="Ankit Mahato",
      author_email="ankmahato@gmail.com",
      packages=["titus",
                "titus.producer",
                "titus.lib",
                "titus.lib.model",
                "titus.lib.prob",
                "titus.lib.stat",
                "titus.pmml",
                "titus.inspector"],
      scripts = ["scripts/pfainspector", "scripts/pfachain", "scripts/pfaexternalize", "scripts/pfarandom", "scripts/pfasize"],
      description="Python 3 implementation of Portable Format for Analytics (PFA): producer, converter, and consumer.",
      test_suite="test",
      install_requires=["avro-python3 >= 1.8.2", "ply >= 3.4", "pyyaml >= 3.10", "numpy >= 1.6.1", "pytz >= 2015.4"],
      tests_require=["avro-python3 >= 1.8.2", "ply >= 3.4", "pyyaml >= 3.10", "numpy >= 1.6.1", "pytz >= 2015.4"],
      )

### details of dependencies:
# 
# Tested in Python 3.4-3.8.
# Will not work in Python 2.x.
# 
# Avro is required; it is an integral part of PFA.
# PLY is required; it is used to parse PrettyPFA and Inspector commandlines.
# 
# PyYAML is an optional dependency; it is only used by the titus.reader.yamlToAst function.
# Numpy is an optional dependency; it is only used by the "interp", "la", "stat.test", and "model.reg" PFA libraries, as well as Titus producers.
# pytz is an optional dependency; it is only used by the "time" PFA library.
