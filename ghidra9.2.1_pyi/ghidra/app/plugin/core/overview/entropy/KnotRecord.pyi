import java.lang


class KnotRecord(object):
    color: java.awt.Color
    end: int
    name: unicode
    point: int
    start: int



    def __init__(self, __a0: unicode, __a1: java.awt.Color, __a2: int, __a3: int, __a4: int): ...



    def contains(self, __a0: int) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

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
