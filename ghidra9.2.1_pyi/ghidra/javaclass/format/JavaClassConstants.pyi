import java.lang


class JavaClassConstants(object):
    MAGIC: int = -889275714
    MAGIC_BYTES: List[int] = array('b', [-54, -2, -70, -66])
    OPERAND_PLACEHOLDER: unicode = u'&&&'
    T_BOOLEAN: int = 4
    T_BYTE: int = 8
    T_CHAR: int = 5
    T_DOUBLE: int = 7
    T_FLOAT: int = 6
    T_INT: int = 10
    T_LONG: int = 11
    T_SHORT: int = 9



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
