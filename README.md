# My Ghidra scripts

This repository contains some Ghidra scripts to automate my reverse-engineering tasks.

## IDE setup

### Python Scripting

I think the Ghidra python scripting with PyCharm is the best way for developing.
Please follow [here](https://github.com/VDOO-Connected-Trust/ghidra-pyi-generator) for more details.
The [ghidra-pyi-generator](https://github.com/VDOO-Connected-Trust/ghidra-pyi-generator) does not provide the `.pyi` type stubs for Ghidra 9.2.
So, I have newly created the `.pyi` [type stubs for Ghidra 9.2](./ghidra9.2.1_pyi). If you use the Ghidra 9.2, please use these stubs.

### Java Scripting

I think it is better to use Eclipse with GhidraDev plugin when scripting Java.
Please follow the Ghidra official documentation.

## About scripts

### CalcCyclomaticForAllFunctions.py

This script calculates the Cyclomatic complexities for all functions of the current program.
It can be used for finding the complex functions that have potential vulnerabilities.

### SearchFunctionCallPattern.py

This script searches the function call pattern

## Author

Koh M. Nakagawa

## License

MIT License
