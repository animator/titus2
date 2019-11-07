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

import time
import unittest

from titus.genpy import PFAEngine
from titus.errors import *
    
class TestSpeed(unittest.TestCase):
    def testTree(self):
        pfa_file = open("test/hipparcos_numerical_10.pfa")
        pfa = pfa_file.read()
        pfa_file.close()
        engine, = PFAEngine.fromJson(pfa)

        data = []
        data_file = open("test/hipparcos_numerical.csv")
        lines = data_file.readlines()
        data_file.close()
        for line in lines:
            ra, dec, dist, mag, absmag, x, y, z, vx, vy, vz, spectrum = line.split(",")
            data.append({"ra": float(ra), "dec": float(dec), "dist": float(dist), "mag": float(mag), "absmag": float(absmag), 
                         "x": float(x), "y": float(y), "z": float(z), "vx": float(vx), "vy": float(vy), "vz": float(vz)})

        i = 0
        startTime = time.time()
        for datum in data:
            engine.action(datum)
            i += 1
            if i % 5000 == 0:
                print("{0}, {1}".format(time.time() - startTime, i))

if __name__ == "__main__":
    unittest.main()
