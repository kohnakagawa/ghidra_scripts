from typing import List
import java.awt
import java.lang


class TokenHighlightColors(object):
    """
    A class to create and store colors related to token names
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self, text: unicode) -> java.awt.Color: ...

    def getRecentColors(self) -> List[java.awt.Color]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setColor(self, text: unicode, color: java.awt.Color) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def recentColors(self) -> List[object]: ...
