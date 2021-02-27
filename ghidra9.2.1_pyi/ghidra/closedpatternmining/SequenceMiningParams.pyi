import java.lang


class SequenceMiningParams(object):




    def __init__(self, __a0: float, __a1: int, __a2: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMinPercentage(self) -> float: ...

    def getRequiredBitsOfCheck(self) -> int: ...

    def getUseBinary(self) -> bool: ...

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
    def minPercentage(self) -> float: ...

    @property
    def requiredBitsOfCheck(self) -> int: ...

    @property
    def useBinary(self) -> bool: ...
