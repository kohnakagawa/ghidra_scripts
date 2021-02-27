import java.lang


class DecmpfsStates(object):
    FILE_IS_COMPRESSED: int = 2
    FILE_IS_CONVERTING: int = 3
    FILE_IS_NOT_COMPRESSED: int = 1
    FILE_TYPE_UNKNOWN: int = 0



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
