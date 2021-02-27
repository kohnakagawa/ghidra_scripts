import java.lang


class StatementProgramInstructions(object):
    DW_LNE_define_file: int = 3
    DW_LNE_end_sequence: int = 1
    DW_LNE_set_address: int = 2
    DW_LNS_advance_line: int = 3
    DW_LNS_advance_pc: int = 2
    DW_LNS_const_add_pc: int = 8
    DW_LNS_copy: int = 1
    DW_LNS_fixed_advanced_pc: int = 9
    DW_LNS_negate_statement: int = 6
    DW_LNS_set_basic_block: int = 7
    DW_LNS_set_column: int = 5
    DW_LNS_set_epilog_begin: int = 11
    DW_LNS_set_file: int = 4
    DW_LNS_set_isa: int = 12
    DW_LNS_set_prologue_end: int = 10



    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, machine: ghidra.app.util.bin.format.dwarf.line.StateMachine, prologue: ghidra.app.util.bin.format.dwarf.line.StatementProgramPrologue): ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self) -> None:
        """
        Read the next instruction and executes it
         on the given state machine.
        @throws IOException if an i/o error occurs
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
