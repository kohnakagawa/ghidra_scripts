import ghidra.program.model.listing
import ghidra.xml
import java.io
import java.lang
import java.util


class FuncDB(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def query(self, __a0: ghidra.program.model.listing.Function) -> java.util.ArrayList: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser) -> None: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
