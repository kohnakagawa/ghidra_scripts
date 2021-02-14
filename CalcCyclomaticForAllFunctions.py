#Calculate cyclomatic complexities for all functions defined in the current program
#@author 
#@category CodeAnalysis
#@keybinding 
#@menupath 
#@toolbar 


from __main__ import *
from ghidra.program.util import CyclomaticComplexity


def get_complex_functions_list(num):
    functions = currentProgram.getFunctionManager().getFunctions(True)

    func_to_complexity = list()
    cc = CyclomaticComplexity()
    for function in functions:
        complexity = cc.calculateCyclomaticComplexity(function, monitor)
        func_to_complexity.append({
            "function": str(function),
            "address": function.getEntryPoint(),
            "complexity": complexity
        })

    func_to_complexity_sorted = sorted(func_to_complexity, key=lambda elem: elem["complexity"], reverse=True)
    return func_to_complexity_sorted[:num]



if __name__ == "__main__":
    print(get_complex_functions_list(10))