In Development - Please do not use until release
=======


Python 3 port of the Portable Format for Analytics (PFA) implementation Titus
========

Fork of a subset of [Hadrian: implementations of the PFA specification](https://github.com/opendatagroup/hadrian).


**As of version 0.8.4, Titus is available with the Apache License v2.0**

**Version v.0.8.4**

The [Portable Format for Analytics (PFA)](http://dmg.org/pfa) is a specification for scoring engines: event-based processors that perform predictive or analytic calculations. It is a common language to help smooth the transition from statistical model development to large-scale and/or online production. For a model expressed as PFA to be run against data, an application is required.

**Titus** ([API](http://opendatagroup.github.io/hadrian/titus-0.8.3/titus.genpy.PFAEngine)) is Open Data's complete implementation of PFA for Python. Hadrian and Titus both execute the same scoring engines, but while Hadrian's focus is speed and portability, Titus's focus is on model development. Included with Titus are standard model producers, a [PrettyPFA](https://github.com/opendatagroup/hadrian/wiki/PrettyPFA) parser for easier editing, a [PFA-Inspector](https://github.com/opendatagroup/hadrian/wiki/PFA-Inspector) commandline for interactive analysis of a PFA document, and many other tools and scripts.

See the [Hadrian wiki](https://github.com/opendatagroup/hadrian/wiki) for more information, including [installation instructions](https://github.com/opendatagroup/hadrian/wiki/Installation) and tutorials.
