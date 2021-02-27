from typing import List
import ghidra.app.util.html
import java.lang


class DataTypeDiffInput(object):
    """
    An interface that provides lines that are to be used in a diff and can also create
     specialized placeholder lines upon request.
    """









    def createPlaceHolder(self, oppositeLine: ghidra.app.util.html.ValidatableLine) -> ghidra.app.util.html.PlaceHolderLine: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLines(self) -> List[ghidra.app.util.html.ValidatableLine]: ...

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
    def lines(self) -> List[object]: ...
