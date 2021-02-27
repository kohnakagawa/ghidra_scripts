import ghidra.pcodeCPort.slgh_compile
import java.lang


class Token(ghidra.pcodeCPort.slgh_compile.Yylval):
    beginColumn: int
    beginLine: int
    endColumn: int
    endLine: int
    image: unicode
    kind: int
    next: ghidra.pcodeCPort.slgh_compile.Token
    specialToken: ghidra.pcodeCPort.slgh_compile.Token



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def newToken(__a0: int) -> ghidra.pcodeCPort.slgh_compile.Token: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
