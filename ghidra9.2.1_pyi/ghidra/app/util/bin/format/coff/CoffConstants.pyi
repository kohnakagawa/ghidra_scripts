import java.lang


class CoffConstants(object):
    AUXILIARY_ARRAY_DIMENSION: int = 4
    FILE_NAME_LENGTH: int = 14
    SECTION_NAME_LENGTH: int = 8
    SYMBOL_NAME_LENGTH: int = 8
    SYMBOL_SIZEOF: int = 18



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
