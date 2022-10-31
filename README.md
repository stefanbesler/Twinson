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
- [ ] Performance improvments for accessing elements, use tree to store date instead of array

## Comparison to Tc3_Json

Twinson is lightweight alternative to Beckhoff's `Tc3_Json.FB_JsonDomParser`. When comparing Twinson with the Tc3_Json (TC 3.1.4024.25), is discovered some issues with Tc3_Json that might be addressed by Beckhoff in the future.

- Null is not parsed correctly
- Parsing nested arrays doesn't seem to work correctly
- Array access and even member access is cumbersome (maybe it's only personal taste though)

## Benchmark

Twinson includes a seperate PLC for benchmarking the library against Tc3_Json. The benchmark uses several examples with increasing JSON complexity. We measure the duration it takes for parsing a JSON document and assigning all members of the JSON document to TwinCAT variables with direct member access. Note that JsonDomParser offers an iterator-like approach for parsing, which may lead to better results.


- Example 1


