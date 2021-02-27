# Search function call pattern
# @author Ko Nakagawa
# @category CodeAnalysis
# @keybinding
# @menupath
# @toolbar


import re
import sys
from typing import Any, List, Optional, Tuple, Union

from ghidra.app.decompiler import (
    DecompileOptions,
    DecompileResults,
    DecompInterface,
)
from ghidra.program.model.address import Address
from ghidra.program.model.pcode import PcodeOpAST
from ghidra.program.model.symbol import Reference, RefType

try:
    from ghidra_builtins import *
except Exception as e:
    pass


def is_target_ref(ref):  # type: (Reference) -> bool
    return ref.getReferenceType() == RefType.UNCONDITIONAL_CALL


# NOTE: float is not supported
def parse_args(args):  # type: (str) -> List[Tuple[int, Union[str, int]]]
    args_parsed = list()
    for i, arg in enumerate(args.split(",")):
        if arg.isdigit():
            args_parsed.append((i, int(arg)))
        elif arg != "_":
            args_parsed.append((i, arg))
    return args_parsed


def get_decompile_interface():  # type: () -> DecompInterface
    interface = DecompInterface()
    options = DecompileOptions()
    interface.setOptions(options)
    interface.openProgram(currentProgram)
    interface.setSimplificationStyle("decompile")
    return interface


def decompile_at(
    interface, address
):  # type: (DecompInterface, Address) -> Optional[DecompileResults]
    function = getFunctionContaining(address)
    if function is None:
        sys.stderr.write("Function is not defined at " + str(address) + "\n")
        return None
    return interface.decompileFunction(function, 30, monitor)


def check_function_argments(
    pcode_op_ast, parsed_args
):  # type: (PcodeOpAST, List[Tuple[int, Union[str, int]]]) -> None
    pcode_op_ast.getNumInputs()


def search_function_call_pattern(
    func_name, args
):  # type: (str, str) -> Optional[List[Any]]
    functions_found = getGlobalFunctions(func_name)
    if len(functions_found) != 1:
        if len(functions_found) == 0:
            sys.stderr.write(func_name + " is not found\n")
            return None
        if len(functions_found) >= 2:
            sys.stderr.write("Multiple " + func_name + " are found\n")
            return None

    decompile_ifc = get_decompile_interface()
    parsed_args = parse_args(args)

    target_function_addr = functions_found[0].getEntryPoint()
    refs_to_target = getReferencesTo(target_function_addr)
    for ref in refs_to_target:  # type: Reference
        if not is_target_ref(ref):
            continue

        decompile_results = decompile_at(decompile_ifc, ref.getFromAddress())
        high_function = decompile_results.getHighFunction()
        if high_function is None:
            sys.stderr.write("Cannot get high function")
            continue

        high_function.getPcodeOps(ref.getFromAddress())


def split_function_name_and_argment(
    func_call_pattern,
):  # type: (str) -> Optional[Tuple[str, str]]
    # NOTE: assuming that parenthesis are not included in function parameters
    # For example, func(a, hoge(b, c)) is not supported now.
    # This feature will be supported future.
    matched_obj = re.match(r"(.*)\((.*)\)", func_call_pattern)
    if matched_obj is None or len(matched_obj.groups()) != 2:
        sys.stderr.write(
            "Specified function call patter " + func_call_pattern + " is invalid"
        )
        return None
    return matched_obj.groups()[0], matched_obj.groups()[1]


def _main():  # type: () -> None
    func_name = askString(
        "Function call pattern?", "Type function call pattern (e.g., func(1, _, 3))"
    )
    func_name_and_args = split_function_name_and_argment(str(func_name).strip())
    if func_name_and_args is None:
        return

    search_function_call_pattern(*func_name_and_args)


if __name__ == "__main__":
    _main()
