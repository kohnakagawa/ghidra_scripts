import java.lang


class CoffSymbolType(object):
    DT_ARY: int = 3
    DT_FCN: int = 2
    DT_NON: int = 0
    DT_PTR: int = 1
    T_CHAR: int = 2
    T_DOUBLE: int = 7
    T_ENUM: int = 10
    T_FLOAT: int = 6
    T_INT: int = 4
    T_LONG: int = 5
    T_LONG_DOUBLE: int = 16
    T_MOE: int = 11
    T_NULL: int = 0
    T_SHORT: int = 3
    T_STRUCT: int = 8
    T_UCHAR: int = 12
    T_UINT: int = 14
    T_ULONG: int = 15
    T_UNION: int = 9
    T_USHORT: int = 13
    T_VOID: int = 1



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getBaseType(symbolType: int) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDerivedType(symbolType: int) -> int: ...

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
