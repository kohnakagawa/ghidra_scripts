# Search function call pattern
# @author Ko Nakagawa
# @category CodeAnalysis
# @keybinding
# @menupath
# @toolbar


import sys

try:
    from ghidra_builtins import *
except:
    pass


def search_function_call_pattern(func_name, argment):  # type: (str, str) -> None
    functions_found = getGlobalFunctions(func_name)
    if len(functions_found) != 1:
        if len(functions_found) == 0:
            sys.stderr.write(func_name + " is not found")
            return
        if len(functions_found) >= 2:
            sys.stderr.write("Multiple " + func_name + " are found")
            return

    target_function_addr = functions_found[0].getEntryPoint()
    refs_to_target = getReferencesTo(target_function_addr)
    for ref in refs_to_target:
        print(type(ref))


if __name__ == "__main__":
    func_name = askString(
        "Function call pattern?", "Type function call pattern (e.g., func(1, _, 3))"
    )
    search_function_call_pattern(func_name, None)
