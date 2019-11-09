#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
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

import unittest
import math
import struct
import base64

from titus.genpy import PFAEngine
from titus.lib.core import INT_MIN_VALUE, INT_MAX_VALUE, LONG_MIN_VALUE, LONG_MAX_VALUE
from titus.errors import *

class TestLib1Rand(unittest.TestCase):
    def testInt(self):
        engine1, = PFAEngine.fromYaml('''
input: "null"
output: int
randseed: 12345
action: {rand.int: []}
''')
        self.assertTrue(INT_MIN_VALUE <= engine1.action(None) <= INT_MAX_VALUE)
        self.assertTrue(INT_MIN_VALUE <= engine1.action(None) <= INT_MAX_VALUE)
        self.assertTrue(INT_MIN_VALUE <= engine1.action(None) <= INT_MAX_VALUE)

        engine2, = PFAEngine.fromYaml('''
input: "null"
output: int
randseed: 12345
action: {rand.int: [5, 10]}
''')
        self.assertTrue(5 <= engine2.action(None) <= 10)
        self.assertTrue(5 <= engine2.action(None) <= 10)
        self.assertTrue(5 <= engine2.action(None) <= 10)

    def testLong(self):
        engine1, = PFAEngine.fromYaml('''
input: "null"
output: long
randseed: 12345
action: {rand.long: []}
''')
        self.assertTrue(LONG_MIN_VALUE <= engine1.action(None) <= LONG_MAX_VALUE)
        self.assertTrue(LONG_MIN_VALUE <= engine1.action(None) <= LONG_MAX_VALUE)
        self.assertTrue(LONG_MIN_VALUE <= engine1.action(None) <= LONG_MAX_VALUE)

        engine2, = PFAEngine.fromYaml('''
input: "null"
output: long
randseed: 12345
action: {rand.long: [5, 10]}
''')
        self.assertTrue(5 <= engine2.action(None) <= 10)
        self.assertTrue(5 <= engine2.action(None) <= 10)
        self.assertTrue(5 <= engine2.action(None) <= 10)

    def testFloat(self):
        engine, = PFAEngine.fromYaml('''
input: "null"
output: float
randseed: 12345
action: {rand.float: [5, 10]}
''')
        self.assertAlmostEqual(engine.action(None), 7.08309936273, places=5)
        self.assertAlmostEqual(engine.action(None), 5.05084584729, places=5)
        self.assertAlmostEqual(engine.action(None), 9.12603254627, places=5)

    def testDouble(self):
        engine, = PFAEngine.fromYaml('''
input: "null"
output: double
randseed: 12345
action: {rand.double: [5, 10]}
''')
        self.assertAlmostEqual(engine.action(None), 7.08309936273, places=5)
        self.assertAlmostEqual(engine.action(None), 5.05084584729, places=5)
        self.assertAlmostEqual(engine.action(None), 9.12603254627, places=5)

    def testChoice(self):
        engine, = PFAEngine.fromYaml('''
input:
  type: array
  items: string
output: string
randseed: 12345
action: {rand.choice: input}
''')
        self.assertTrue(engine.action(["one", "two", "three", "four", "five"]) in ["one", "two", "three", "four", "five"])
        self.assertTrue(engine.action(["one", "two", "three", "four", "five"]) in ["one", "two", "three", "four", "five"])
        self.assertTrue(engine.action(["one", "two", "three", "four", "five"]) in ["one", "two", "three", "four", "five"])
        self.assertTrue(engine.action(["one", "two", "three", "four", "five"]) in ["one", "two", "three", "four", "five"])
        self.assertTrue(engine.action(["one", "two", "three", "four", "five"]) in ["one", "two", "three", "four", "five"])

    def testChoicesWithReplacement(self):
        engine, = PFAEngine.fromYaml('''
input:
  type: array
  items: string
output:
  type: array
  items: string
randseed: 12345
action: {rand.choices: [3, input]}
''')
        self.assertTrue(set(engine.action(["one", "two", "three", "four", "five"])).issubset({"one", "two", "three", "four", "five"}))
        self.assertTrue(set(engine.action(["one", "two", "three", "four", "five"])).issubset({"one", "two", "three", "four", "five"}))
        self.assertTrue(set(engine.action(["one", "two", "three", "four", "five"])).issubset({"one", "two", "three", "four", "five"}))
        self.assertTrue(set(engine.action(["one", "two", "three", "four", "five"])).issubset({"one", "two", "three", "four", "five"}))
        self.assertTrue(set(engine.action(["one", "two", "three", "four", "five"])).issubset({"one", "two", "three", "four", "five"}))

    def testSampleWithoutReplacement(self):
        engine, = PFAEngine.fromYaml('''
input:
  type: array
  items: string
output:
  type: array
  items: string
randseed: 12345
action: {rand.sample: [3, input]}
''')
        x = engine.action(["one", "two", "three", "four", "five"])
        self.assertTrue(set(x).issubset({"one", "two", "three", "four", "five"}) and len(set(x))==3)
        x = engine.action(["one", "two", "three", "four", "five"])
        self.assertTrue(set(x).issubset({"one", "two", "three", "four", "five"}) and len(set(x))==3)
        x = engine.action(["one", "two", "three", "four", "five"])
        self.assertTrue(set(x).issubset({"one", "two", "three", "four", "five"}) and len(set(x))==3)
        x = engine.action(["one", "two", "three", "four", "five"])
        self.assertTrue(set(x).issubset({"one", "two", "three", "four", "five"}) and len(set(x))==3)
        x = engine.action(["one", "two", "three", "four", "five"])
        self.assertTrue(set(x).issubset({"one", "two", "three", "four", "five"}) and len(set(x))==3)

    def testHistogram(self):
        engine, = PFAEngine.fromYaml('''
input: "null"
output: int
randseed: 12345
action: {rand.histogram: {value: [3.3, 2.2, 5.5, 0.0, 1.1, 8.8], type: {type: array, items: double}}}
''')
        results = [engine.action(None) for i in range(0, 10000)]
        self.assertAlmostEqual(results.count(0) / 10000.0, 0.15789473684210525, places=2)
        self.assertAlmostEqual(results.count(1) / 10000.0, 0.10526315789473686, places=2)
        self.assertAlmostEqual(results.count(2) / 10000.0, 0.26315789473684215, places=2)
        self.assertAlmostEqual(results.count(3) / 10000.0, 0.0, places=2)
        self.assertAlmostEqual(results.count(4) / 10000.0, 0.05263157894736843, places=2)
        self.assertAlmostEqual(results.count(5) / 10000.0, 0.42105263157894746, places=2)
        self.assertAlmostEqual(results.count(6) / 10000.0, 0.0, places=2)

    def testHistogram2(self):
        engine, = PFAEngine.fromYaml('''
input: "null"
output: HistogramItem
randseed: 12345
cells:
  hist:
    type:
      type: array
      items:
        type: record
        name: HistogramItem
        fields:
          - {name: label, type: string}
          - {name: prob, type: double}
    init:
      - {label: A, prob: 3.3}
      - {label: B, prob: 2.2}
      - {label: C, prob: 5.5}
      - {label: D, prob: 0.0}
      - {label: E, prob: 1.1}
      - {label: F, prob: 8.8}
action: {rand.histogram: {cell: hist}}
''')
        results = [engine.action(None) for i in range(0, 10000)]
        self.assertAlmostEqual(sum(1 for x in results if x["label"] == "A") / 10000.0, 0.15789473684210525, places=2)
        self.assertAlmostEqual(sum(1 for x in results if x["label"] == "B") / 10000.0, 0.10526315789473686, places=2)
        self.assertAlmostEqual(sum(1 for x in results if x["label"] == "C") / 10000.0, 0.26315789473684215, places=2)
        self.assertAlmostEqual(sum(1 for x in results if x["label"] == "D") / 10000.0, 0.0, places=2)
        self.assertAlmostEqual(sum(1 for x in results if x["label"] == "E") / 10000.0, 0.05263157894736843, places=2)
        self.assertAlmostEqual(sum(1 for x in results if x["label"] == "F") / 10000.0, 0.42105263157894746, places=2)
        self.assertAlmostEqual(sum(1 for x in results if x["label"] == "G") / 10000.0, 0.0, places=2)

    def testString(self):
        engine1, = PFAEngine.fromYaml('''
input: "null"
output: string
randseed: 12345
action: {rand.string: [10]}
''')
        self.assertEqual(len(engine1.action(None)), 10)
        self.assertEqual(len(engine1.action(None)), 10)
        self.assertEqual(len(engine1.action(None)), 10)

        engine2, = PFAEngine.fromYaml('''
input: "null"
output: string
randseed: 12345
action: {rand.string: [10, {string: "abcdefghijklmnopqrstuvwxyz0123456789"}]}
''')
        x = engine2.action(None)
        self.assertTrue(set(list(x)).issubset(set(list("abcdefghijklmnopqrstuvwxyz0123456789"))) and len(x)==10)
        x = engine2.action(None)
        self.assertTrue(set(list(x)).issubset(set(list("abcdefghijklmnopqrstuvwxyz0123456789"))) and len(x)==10)
        x = engine2.action(None)
        self.assertTrue(set(list(x)).issubset(set(list("abcdefghijklmnopqrstuvwxyz0123456789"))) and len(x)==10)

        engine3, = PFAEngine.fromYaml('''
input: "null"
output: string
randseed: 12345
action: {rand.string: [10, 33, 127]}
''')
        x = engine3.action(None)
        self.assertTrue(len(x)==10 and min(list(map(ord, x)))>=33 and max(list(map(ord, x)))<=127)
        x = engine3.action(None)
        self.assertTrue(len(x)==10 and min(list(map(ord, x)))>=33 and max(list(map(ord, x)))<=127)
        x = engine3.action(None)
        self.assertTrue(len(x)==10 and min(list(map(ord, x)))>=33 and max(list(map(ord, x)))<=127)

    def testBytes(self):
        engine1, = PFAEngine.fromYaml('''
input: "null"
output: bytes
randseed: 12345
action: {rand.bytes: [10]}
''')
        self.assertEqual(len(engine1.action(None)), 10)
        self.assertEqual(len(engine1.action(None)), 10)
        self.assertEqual(len(engine1.action(None)), 10)

        engine2, = PFAEngine.fromYaml('''
input: "null"
output: bytes
randseed: 12345
action: {rand.bytes: [10, {base64: "YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5"}]}
''')
        x = engine2.action(None)
        self.assertTrue(set(list(x)).issubset(set(list('abcdefghijklmnopqrstuvwxyz0123456789'))) and len(x)==10)
        x = engine2.action(None)
        self.assertTrue(set(list(x)).issubset(set(list('abcdefghijklmnopqrstuvwxyz0123456789'))) and len(x)==10)
        x = engine2.action(None)
        self.assertTrue(set(list(x)).issubset(set(list('abcdefghijklmnopqrstuvwxyz0123456789'))) and len(x)==10)

        engine3, = PFAEngine.fromYaml('''
input: "null"
output: bytes
randseed: 12345
action: {rand.bytes: [10, 33, 127]}
''')
        x = engine3.action(None)
        self.assertTrue(len(x)==10 and min(list(map(ord, x)))>=33 and max(list(map(ord, x)))<=127)
        x = engine3.action(None)
        self.assertTrue(len(x)==10 and min(list(map(ord, x)))>=33 and max(list(map(ord, x)))<=127)
        x = engine3.action(None)
        self.assertTrue(len(x)==10 and min(list(map(ord, x)))>=33 and max(list(map(ord, x)))<=127)

    def testUUID(self):
        engine1, = PFAEngine.fromYaml('''
input: "null"
output: string
randseed: 12345
action: {rand.uuid4: []}
''')
        self.assertEqual(engine1.action(None), "6aa79987-bb91-4029-8d1f-cd8778e7d340bbcd")
        self.assertEqual(engine1.action(None), "4c73a942-daea-45e5-8ee8-452ec40a3193ca54")
        self.assertEqual(engine1.action(None), "90e5e945-6fac-4296-85f8-dfc9e3b11fcff454")

        engine2, = PFAEngine.fromYaml('''
input: "null"
output: string
action: {s.substr: [{rand.uuid4: []}, 14, 15]}
''')
        for i in range(1000):
            self.assertEqual(engine2.action(None), "4")

        engine3, = PFAEngine.fromYaml('''
input: "null"
output: string
action: {s.substr: [{rand.uuid4: []}, 19, 20]}
''')
        for i in range(1000):
            self.assertEqual(engine3.action(None), "8")

    def testGaussian(self):
        engine, = PFAEngine.fromYaml('''
input: "null"
output: double
randseed: 12345
action: {rand.gaussian: [10, 2]}
''')
        self.assertAlmostEqual(engine.action(None), 9.75239840882, places=5)
        self.assertAlmostEqual(engine.action(None), 10.143049927, places=5)
        self.assertAlmostEqual(engine.action(None), 10.7667383886, places=5)

if __name__ == "__main__":
    unittest.main()
