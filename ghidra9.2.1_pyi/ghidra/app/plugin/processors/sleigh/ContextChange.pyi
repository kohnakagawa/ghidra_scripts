import ghidra.app.plugin.processors.sleigh
import ghidra.xml
import java.lang


class ContextChange(object):








    def apply(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker, debug: ghidra.app.plugin.processors.sleigh.SleighDebugLogger) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
