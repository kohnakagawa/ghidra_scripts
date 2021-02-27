import java.lang


class SpaceQuality(object):
    isdefault: bool
    name: unicode
    size: int
    type: ghidra.pcodeCPort.slgh_compile.space_class
    wordsize: int



    def __init__(self, __a0: unicode): ...



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
