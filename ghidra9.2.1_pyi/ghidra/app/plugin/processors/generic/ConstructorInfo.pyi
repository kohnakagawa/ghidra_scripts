import java.lang


class ConstructorInfo(object):
    """
    Structure for collecting cached information about an instruction
    """

    BRANCH_INDIRECT: int = 4
    BRANCH_TO_END: int = 64
    CALL: int = 8
    CALL_INDIRECT: int = 2
    JUMPOUT: int = 16
    NO_FALLTHRU: int = 32
    RETURN: int = 1



    def __init__(self, ln: int, fl: int): ...



    def addLength(self, l: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlowFlags(self) -> int: ...

    def getLength(self) -> int: ...

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

    @property
    def flowFlags(self) -> int: ...

    @property
    def length(self) -> int: ...
