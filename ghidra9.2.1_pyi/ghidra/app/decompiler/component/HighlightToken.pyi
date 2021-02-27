import ghidra.app.decompiler
import java.awt
import java.lang


class HighlightToken(object):
    """
    A class to used to track a Decompiler token along with its highlight color
    """





    def __init__(self, token: ghidra.app.decompiler.ClangToken, color: java.awt.Color): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self) -> java.awt.Color: ...

    def getToken(self) -> ghidra.app.decompiler.ClangToken: ...

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
    def color(self) -> java.awt.Color: ...

    @property
    def token(self) -> ghidra.app.decompiler.ClangToken: ...
