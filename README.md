[![Build Status](https://travis-ci.org/animator/titus2.svg?branch=master)](https://travis-ci.org/animator/titus2)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/titus2)
[![PyPI version](https://badge.fury.io/py/titus2.svg)](https://badge.fury.io/py/titus2)
![Maintenance](https://img.shields.io/maintenance/yes/2019)
![GitHub](https://img.shields.io/github/license/animator/titus2)
![Twitter Follow](https://img.shields.io/twitter/follow/ankitmahato?label=Follow&style=social)

> **Data Scientist**: Why is my cutting edge model still not in production?
>
Scenario 1:
> **IT Team**: We are still implementing the scoring engine in Go/Java/C++.   

Scenario 2:
> **IT Team**: We are still figuring out how to read the model.pkl file you provided.   

. .

and the push to production pang continues ..

# New Features!

  - `PFAEngine.fromPmml(pmmlDocument)` support is now dropped begining v1.1.0 as its implementation was originally not matured in [titus](https://github.com/opendatagroup/hadrian). Only 2/40 examples listed in the DMG PMML website were compatible with `PFAEngine.fromPmml(pmmlDocument)` in the original titus package.   

### Changes in titus2 v1.1.0

View the complete changelog [here](https://github.com/animator/titus2/blob/master/CHANGELOG.md).

Titus 2 - Portable Format for Analytics (PFA) implementation for Python 3.4+ 
========


This is a subset-fork of the [original repository](https://github.com/opendatagroup/hadrian) which has been completely migrated to Python 3.

The [Portable Format for Analytics (PFA)](http://dmg.org/pfa) is a specification for scoring/inference engines: event-based processors that perform predictive or analytic calculations. It is a model interchange format which helps smoothen the transition from statistical model development to large-scale and/or online production. 

![PFA](http://dmg.org/pfa/docs/motivation/pfatoeverything.png)

**Titus** (Python 2) ([API](http://opendatagroup.github.io/hadrian/titus-0.8.3/titus.genpy.PFAEngine)) was originally Open Data's complete implementation of PFA for Python. It can be used for model development as well as to execute the scoring engine. Titus 2 is a fork of Titus which is being maintained actively. 

### Requirements

Titus 2 uses a number of open source projects to work properly:

* avro-python3 >= 1.8.2
* numpy >= 1.15.0
* pytz >= 2019.1
* pyyaml >= 5.1.2
* ply >= 3.11

The above packages are available via `pip` and are automatically installed during setup.

### Installation

Titus requires [Python 3.4+](https://www.python.org/download/) to run.
It can be installed via pip/pip3 as follows:
```sh
$ pip install titus2
```

or you can directly install the latest build from github repository via 
```sh
$ pip install git+https://github.com/animator/titus2.git
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
  - Unit testing status available [here](https://travis-ci.org/animator/titus2) [![Build Status](https://travis-ci.org/animator/titus2.svg?branch=master)](https://travis-ci.org/animator/titus2) 
  - Conformance testing status available [here](https://travis-ci.org/animator/pfa) [![Build Status](https://travis-ci.org/animator/pfa.svg?branch=master)](https://travis-ci.org/animator/pfa) 

### Issues, Questions and Feature Requests

Please raise an issue/question/request [here](https://github.com/animator/titus2/issues).

### Development

Want to contribute? Great!

Please raise an [issue](https://github.com/animator/titus2/issues) to discuss your ideas and send a [pull request](https://github.com/animator/titus2/pulls).

### Todos

 - Write MORE Tests for `scripts/*`.
 - Add `scikit-learn` model export to PFA tutorials.
