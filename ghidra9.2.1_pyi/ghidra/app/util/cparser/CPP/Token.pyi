import ghidra.app.util.cparser.CPP
import java.io
import java.lang


class Token(object, java.io.Serializable):
    beginColumn: int
    beginLine: int
    endColumn: int
    endLine: int
    image: unicode
    kind: int
    next: ghidra.app.util.cparser.CPP.Token
    specialToken: ghidra.app.util.cparser.CPP.Token



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: int): ...

    @overload
    def __init__(self, __a0: int, __a1: unicode): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getValue(self) -> object: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def newToken(__a0: int) -> ghidra.app.util.cparser.CPP.Token: ...

    @overload
    @staticmethod
    def newToken(__a0: int, __a1: unicode) -> ghidra.app.util.cparser.CPP.Token: ...

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
    def value(self) -> object: ...
