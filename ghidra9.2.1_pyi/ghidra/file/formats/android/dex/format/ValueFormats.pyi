import java.lang


class ValueFormats(object):
    VALUE_ANNOTATION: int = 29
    VALUE_ARRAY: int = 28
    VALUE_BOOLEAN: int = 31
    VALUE_BYTE: int = 0
    VALUE_CHAR: int = 3
    VALUE_DOUBLE: int = 17
    VALUE_ENUM: int = 27
    VALUE_FIELD: int = 25
    VALUE_FLOAT: int = 16
    VALUE_INT: int = 4
    VALUE_LONG: int = 6
    VALUE_METHOD: int = 26
    VALUE_NULL: int = 30
    VALUE_SHORT: int = 2
    VALUE_STRING: int = 23
    VALUE_TYPE: int = 24



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(__a0: int) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
