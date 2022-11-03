# Twinson
Simple and lightweight JSON decoder for TwinCAT and CODESYS.

## State of the implementation

- [x] Continuous integration
- [x] Parser
  - [x] Strings
  - [x] Numbers
  - [x] Boolean
  - [x] Null
  - [x] Objects (including nested objects)
  - [x] Arrays (including mixed array and nested arrays)
- [x] Basic element access
- [ ] Monadic element access
- [ ] Unittests
- [x] Performance improvements for accessing elements, use tree to store data instead of array

## Comparison to Tc3_Json

Twinson is lightweight alternative to Beckhoff's `Tc3_Json.FB_JsonDomParser`. When comparing Twinson with the Tc3_Json (TC 3.1.4024.25), I discovered issues with Tc3_Json that might be addressed by Beckhoff in the future.

- `null`, as specified by the JSON format, is not parsed correctly.
- Parsing nested arrays is cumbersome, because there is no way (at least I didn't find any documented) to access an array element directly.

## Benchmark

Twinson includes a seperate PLC for benchmarking the library against Tc3_Json. The benchmark uses several examples with increasing JSON complexity. We measure the duration it takes for parsing a JSON document and assigning all members of the JSON document to TwinCAT variables with direct element access.


