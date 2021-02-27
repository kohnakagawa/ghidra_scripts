from typing import List
import java.io
import java.lang


class SimpleCharStream(object):
    bufpos: int
    staticFlag: bool = False



    @overload
    def __init__(self, __a0: java.io.InputStream): ...

    @overload
    def __init__(self, __a0: java.io.Reader): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: unicode): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: int, __a2: int): ...

    @overload
    def __init__(self, __a0: java.io.Reader, __a1: int, __a2: int): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: int, __a2: int, __a3: int): ...

    @overload
    def __init__(self, __a0: java.io.Reader, __a1: int, __a2: int, __a3: int): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: unicode, __a2: int, __a3: int): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: unicode, __a2: int, __a3: int, __a4: int): ...



    def BeginToken(self) -> int: ...

    def Done(self) -> None: ...

    def GetImage(self) -> unicode: ...

    def GetSuffix(self, __a0: int) -> List[int]: ...

    @overload
    def ReInit(self, __a0: java.io.InputStream) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.Reader) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.InputStream, __a1: unicode) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.InputStream, __a1: int, __a2: int) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.Reader, __a1: int, __a2: int) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.InputStream, __a1: int, __a2: int, __a3: int) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.Reader, __a1: int, __a2: int, __a3: int) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.InputStream, __a1: unicode, __a2: int, __a3: int) -> None: ...

    @overload
    def ReInit(self, __a0: java.io.InputStream, __a1: unicode, __a2: int, __a3: int, __a4: int) -> None: ...

    def adjustBeginLineColumn(self, __a0: int, __a1: int) -> None: ...

    def backup(self, __a0: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBeginColumn(self) -> int: ...

    def getBeginLine(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self) -> int: ...

    def getEndColumn(self) -> int: ...

    def getEndLine(self) -> int: ...

    def getLine(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readChar(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def beginColumn(self) -> int: ...

    @property
    def beginLine(self) -> int: ...

    @property
    def column(self) -> int: ...

    @property
    def endColumn(self) -> int: ...

    @property
    def endLine(self) -> int: ...

    @property
    def line(self) -> int: ...
