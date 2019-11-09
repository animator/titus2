[![Build Status](https://travis-ci.org/animator/python3-titus.svg?branch=master)](https://travis-ci.org/animator/python3-titus)
[![](https://img.shields.io/badge/python-3.4%20|%203.5%20|%203.6%20|%203.7%20|%203.8-blue.svg)](https://www.python.org/download/)
![Maintenance](https://img.shields.io/maintenance/yes/2019)
![GitHub](https://img.shields.io/github/license/animator/python3-titus)
![Twitter Follow](https://img.shields.io/twitter/follow/ankitmahato?label=Follow&style=social)

> **Data Scientist**: Why is my cutting edge model still not in production?
>
Scenario 1:
> **IT Team**: We are still implementing the scoring engine in Go/Java/C++.   

Scenario 2:
> **IT Team**: We are still figuring out how to read the model.pkl file you provided in Java.   

. .

and the push to production pang continues ..

# New Features!

  - Supports Python 3.4+
  - `scripts/pfachain` can combine 2 or more PFA documents

Titus for Python 3.4+ - Portable Format for Analytics (PFA) implementation 
========


This is a subset-fork of the [original repository](https://github.com/opendatagroup/hadrian) which has been completely migrated to Python 3.

The [Portable Format for Analytics (PFA)](http://dmg.org/pfa) is a specification for scoring/inference engines: event-based processors that perform predictive or analytic calculations. It is a model interchange format which helps smoothen the transition from statistical model development to large-scale and/or online production. 

![PFA](http://dmg.org/pfa/docs/motivation/pfatoeverything.png)

**Titus** (Python 2) ([API](http://opendatagroup.github.io/hadrian/titus-0.8.3/titus.genpy.PFAEngine)) was originally Open Data's complete implementation of PFA for Python. It can be used for model development as well as to execute the scoring engine. 

### Requirements

Titus uses a number of open source projects to work properly:

* avro-python3
* numpy
* pytz
* pyyaml
* ply

The above packages are available via `pip` and are automatically installed during setup.

### Installation

Titus requires [Python 3.4+](https://www.python.org/download/) to run.
It can be installed via pip/pip3 as follows:
```sh
$ pip install git+https://github.com/animator/python3-titus.git
```

After installation please run the following elementary example in python

```python
from titus.genpy import PFAEngine

pfa = {"input": "double",
 "output": "double",
 "action": [
   {"+": ["input", 100]}
 ]}
engine, = PFAEngine.fromJson(pfa)

l = [1.0, 2.0, 3.0, 4.0, 5.0]

for num in l:
    print(num, engine.action(num))
```

### User Guide and Tutorials

See the [Hadrian wiki](https://github.com/opendatagroup/hadrian/wiki) for user guide and tutorials.

### Current Testing Framework
  - Unit testing status available [here](https://travis-ci.org/animator/python3-titus) [![Build Status](https://travis-ci.org/animator/python3-titus.svg?branch=master)](https://travis-ci.org/animator/python3-titus) 
  - Conformance testing status available [here](https://travis-ci.org/animator/pfa) [![Build Status](https://travis-ci.org/animator/pfa.svg?branch=master)](https://travis-ci.org/animator/pfa) 

### Issues and Feature Requests

Please raise an issue [here](https://github.com/animator/python3-titus/issues).

### Development

Want to contribute? Great!

Please raise an [issue](https://github.com/animator/python3-titus/issues) and send a [pull request](https://github.com/animator/python3-titus/pulls).

### Todos

 - Write MORE Tests for `scripts/*`.
 - Add `scikit-learn` model export to PFA tutorials.
