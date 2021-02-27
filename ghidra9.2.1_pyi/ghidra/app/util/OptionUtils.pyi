from typing import List
import java.lang


class OptionUtils(object):
    """
    Utility class for providing convenience methods for working with Option's.
    """





    def __init__(self): ...



    @staticmethod
    def containsOption(__a0: unicode, __a1: List[object]) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getBooleanOptionValue(__a0: unicode, __a1: List[object], __a2: bool) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getOption(__a0: unicode, __a1: List[object], __a2: object) -> object: ...

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
