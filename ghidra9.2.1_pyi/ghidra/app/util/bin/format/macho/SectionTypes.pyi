import java.lang


class SectionTypes(object):
    SECTION_TYPE_MASK: int = 255
    S_16BYTE_LITERALS: int = 14
    S_4BYTE_LITERALS: int = 3
    S_8BYTE_LITERALS: int = 4
    S_COALESCED: int = 11
    S_CSTRING_LITERALS: int = 2
    S_DTRACE_DOF: int = 15
    S_GB_ZEROFILL: int = 12
    S_INTERPOSING: int = 13
    S_LAZY_DYLIB_SYMBOL_POINTERS: int = 16
    S_LAZY_SYMBOL_POINTERS: int = 7
    S_LITERAL_POINTERS: int = 5
    S_MOD_INIT_FUNC_POINTERS: int = 9
    S_MOD_TERM_FUNC_POINTERS: int = 10
    S_NON_LAZY_SYMBOL_POINTERS: int = 6
    S_REGULAR: int = 0
    S_SYMBOL_STUBS: int = 8
    S_THREAD_LOCAL_INIT_FUNCTION_POINTERS: int = 21
    S_THREAD_LOCAL_REGULAR: int = 17
    S_THREAD_LOCAL_VARIABLES: int = 19
    S_THREAD_LOCAL_VARIABLE_POINTERS: int = 20
    S_THREAD_LOCAL_ZEROFILL: int = 18
    S_ZEROFILL: int = 1



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getTypeName(type: int) -> unicode:
        """
        Returns the string name for the constant define of the section type.
        @param type the section type
        @return string name for the constant define of the section type
        """
        ...

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
