# Ghidra scripts

This repository contains some Ghidra scripts to automate my reverse-engineering tasks.

## About scripts in this repo

### [CalcCyclomaticForAllFunctions.py](./CalcCyclomaticForAllFunctions.py)

This script calculates the Cyclomatic complexities for all functions of the current program.
It can be used for finding the complex functions.

### [FindFrequentlyUsedFunctions.py](./FindFrequentlyUsedFunctions.py)

This script shows the frequently-called functions.

### [SearchFunctionCallPattern.py](./SearchFunctionCallPattern.py)

This script ...

### [TestSymbolicPropagator.py](./TestSymbolicPropagator.py)

This script ...

## IDE setup

### Python Scripting

I think the best way to develop a Ghidra Python script is to use PyCharm because all type completions work fine.
Please follow [here](https://github.com/VDOO-Connected-Trust/ghidra-pyi-generator) for more details.

Since the [ghidra-pyi-generator](https://github.com/VDOO-Connected-Trust/ghidra-pyi-generator) does not provide the `.pyi` type stubs for Ghidra 9.2, I have newly created the [`.pyi` type stubs for Ghidra 9.2](./ghidra9.2.1_pyi).
If you use the Ghidra 9.2, please use these stubs.

### Java Scripting

I think it is better to use Eclipse with GhidraDev plugin when using Java.
Please follow the Ghidra official documentation.

## Author

Koh M. Nakagawa

## License

MIT License
