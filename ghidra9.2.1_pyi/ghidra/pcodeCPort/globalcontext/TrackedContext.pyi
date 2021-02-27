import ghidra.pcodeCPort.translate
import java.io
import java.lang
import org.jdom


class TrackedContext(object):
    loc: ghidra.pcodeCPort.pcoderaw.VarnodeData
    val: long



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: org.jdom.Element, __a1: ghidra.pcodeCPort.translate.Translate) -> None: ...

    def saveXml(self, __a0: java.io.PrintStream) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
