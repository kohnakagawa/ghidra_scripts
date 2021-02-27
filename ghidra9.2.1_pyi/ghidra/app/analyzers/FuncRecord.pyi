import ghidra.app.analyzers
import ghidra.xml
import java.io
import java.lang
import java.util


class FuncRecord(object, java.lang.Comparable):
    calls: java.util.ArrayList
    children: java.util.ArrayList
    func: ghidra.program.model.listing.Function
    funcName: unicode
    hashValue: long



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Function): ...



    @overload
    def compareTo(self, __a0: ghidra.app.analyzers.FuncRecord) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser) -> java.util.ArrayList: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
