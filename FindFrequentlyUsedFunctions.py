#TODO write a description for this script
#@author Ko Nakagawa
#@category CodeAnalysis
#@keybinding 
#@menupath 
#@toolbar 


from __main__ import *


def get_frequently_used_functions(num):
    functions = currentProgram.getFunctionManager().getFunctions(True)
    
    function_to_n_called = list()
    for function in functions:
        n_calling = len(function.getCalledFunctions(monitor))
        function_to_n_called.append({
            "n_called": n_calling,
            "function": function,
            "address": function.getEntryPoint()
        })
        
    
    function_to_n_called = sorted(function_to_n_called, key=lambda elem: elem["n_called"], reverse=True)
    return function_to_n_called[:num]


if __name__ == "__main__":
    print(get_frequently_used_functions(10))
