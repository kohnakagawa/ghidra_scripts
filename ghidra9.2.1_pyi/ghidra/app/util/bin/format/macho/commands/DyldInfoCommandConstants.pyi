import java.lang


class DyldInfoCommandConstants(object):
    BIND_IMMEDIATE_MASK: int = 15
    BIND_OPCODE_ADD_ADDR_ULEB: int = 128
    BIND_OPCODE_DONE: int = 0
    BIND_OPCODE_DO_BIND: int = 144
    BIND_OPCODE_DO_BIND_ADD_ADDR_IMM_SCALED: int = 176
    BIND_OPCODE_DO_BIND_ADD_ADDR_ULEB: int = 160
    BIND_OPCODE_DO_BIND_ULEB_TIMES_SKIPPING_ULEB: int = 192
    BIND_OPCODE_MASK: int = 240
    BIND_OPCODE_SET_ADDEND_SLEB: int = 96
    BIND_OPCODE_SET_DYLIB_ORDINAL_IMM: int = 16
    BIND_OPCODE_SET_DYLIB_ORDINAL_ULEB: int = 32
    BIND_OPCODE_SET_DYLIB_SPECIAL_IMM: int = 48
    BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB: int = 112
    BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM: int = 64
    BIND_OPCODE_SET_TYPE_IMM: int = 80
    BIND_OPCODE_THREADED: int = 208
    BIND_SPECIAL_DYLIB_FLAT_LOOKUP: int = -2
    BIND_SPECIAL_DYLIB_MAIN_EXECUTABLE: int = -1
    BIND_SPECIAL_DYLIB_SELF: int = 0
    BIND_SYMBOL_FLAGS_NON_WEAK_DEFINITION: int = 8
    BIND_SYMBOL_FLAGS_WEAK_IMPORT: int = 1
    BIND_TYPE_POINTER: int = 1
    BIND_TYPE_TEXT_ABSOLUTE32: int = 2
    BIND_TYPE_TEXT_PCREL32: int = 3
    EXPORT_SYMBOL_FLAGS_HAS_SPECIALIZATIONS: int = 16
    EXPORT_SYMBOL_FLAGS_INDIRECT_DEFINITION: int = 8
    EXPORT_SYMBOL_FLAGS_KIND_MASK: int = 3
    EXPORT_SYMBOL_FLAGS_KIND_REGULAR: int = 0
    EXPORT_SYMBOL_FLAGS_KIND_THREAD_LOCAL: int = 1
    EXPORT_SYMBOL_FLAGS_WEAK_DEFINITION: int = 4
    REBASE_IMMEDIATE_MASK: int = 15
    REBASE_OPCODE_ADD_ADDR_IMM_SCALED: int = 64
    REBASE_OPCODE_ADD_ADDR_ULEB: int = 48
    REBASE_OPCODE_DONE: int = 0
    REBASE_OPCODE_DO_REBASE_ADD_ADDR_ULEB: int = 112
    REBASE_OPCODE_DO_REBASE_IMM_TIMES: int = 80
    REBASE_OPCODE_DO_REBASE_ULEB_TIMES: int = 96
    REBASE_OPCODE_DO_REBASE_ULEB_TIMES_SKIPPING_ULEB: int = 128
    REBASE_OPCODE_MASK: int = 240
    REBASE_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB: int = 32
    REBASE_OPCODE_SET_TYPE_IMM: int = 16
    REBASE_TYPE_POINTER: int = 1
    REBASE_TYPE_TEXT_ABSOLUTE32: int = 2
    REBASE_TYPE_TEXT_PCREL32: int = 3



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

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
