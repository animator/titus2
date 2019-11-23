**v1.1.0:**

  * `PFAEngine.fromPmml(pmmlDocument)` support is now dropped begining v1.1.0 as its implementation was originally not matured in [titus](https://github.com/opendatagroup/hadrian). Only 2/40 examples listed in the DMG PMML website were compatible with `PFAEngine.fromPmml(pmmlDocument)` in the original titus package.

**v1.0.1:**

  * Package renamed as titus2

  * Now available in PyPI - `pip install titus2`

**v1.0.0:**

  * Continues development on Titus v0.8.4 which was maintained by Open Data Group.

  * Major version change as significant changes were made to the codebase in order to migrate to Python 3.

  *  Python's 2to3 tool was used to convert the python files post which other migration activity was undertaken.

  * Listify dict methods - keys(), values(), items().

  * Listify map() function

  * xrange() -> range()

  * unicode, basestring -> str 
  
  * long -> int 

  * raw_input() -> input()

  * unichr() -> chr()

  * .next() method replaced by next() in-built function.

  * urllib.urlopen() -> urllib.request.urlopen()

  * __init__.func_code  -> __init__.__code__

  * Provide the rich comparison methods for ordering in Python 3, which are __lt__, __gt__, __le__, __ge__, __eq__, and __ne__ (PEP 207 -- Rich Comparisons). __cmp__ is no longer used.

  * L postfix is no longer used to denote long datatype number.

  * isinstance(jsonInput, file) -> isinstance(jsonInput, io.IOBase)

  * avro.schema.make_avsc_object() -> avro.schema.SchemaFromJSONData()

  * avro.schema.ArraySchema() & avro.schema.MapSchema() no longer have avro.schema.Names() argument.

  * In Python 3, a new data type is introduced called bytes which is denoted by b'' prefix. As per the PFA specification bytes input and output data are in string form and without any b prefix. To comply with the specification bytesToString() and stringToBytes() are included in titus/utils.py. Also, all inputs to the engine.action() should not contain any string(bytes) prefixed by b'' as per the standard.

  * '/' operator yields a float when operated on integers. Replaced with '//'.

  * sorted( .. , lambda x, y: compare(...)) replaced by sorted(.., functools.cmp_to_key(...)) 

  * SchemaParseException -> avro.schema.AvroException

  * Post Python 3.3, the value for any Linux version (sys.platform) is linux instead of linux2.

  * Fixed avro-python3 'mappingproxy' is not JSON serializable issue by replacing json.dumps(self.schema.to_json()) with str(self.schema). More details [here](https://github.com/animator/python3-titus/commit/a82a981f245fac9a7363b9abbde1f0977dd612ff).

  * Fixed fullName property of AvroCompiled. More details [here](https://github.com/animator/python3-titus/commit/95befe35a5d1dc3050e3ec1c3824e61a7a7e1289).

  * Modified testcase to compare string representation of dictionaries using self.assertDictEqual(). More details [here](https://github.com/animator/python3-titus/commit/3be5bafed38db8baa33b5d4dd11ae0e298d25172) 

  * Fixed scripts/pfachain

  * Bug fixes.

 
**The CHANGELOG of titus maintained by Open Data ("Open Data" refers to one or more of the following companies: Open Data Partners LLC, Open Data Research LLC, or Open Data Capital LLC.) is provided [here](https://github.com/opendatagroup/hadrian/blob/master/CHANGELOG.md).**
