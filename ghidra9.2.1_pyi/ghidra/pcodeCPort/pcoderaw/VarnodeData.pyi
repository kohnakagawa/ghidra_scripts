import ghidra.pcodeCPort.address
import ghidra.pcodeCPort.pcoderaw
import ghidra.pcodeCPort.translate
import java.lang
import org.jdom


class VarnodeData(object):
    offset: long
    size: int
    space: ghidra.pcodeCPort.space.AddrSpace



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: ghidra.pcodeCPort.space.AddrSpace, __a1: long, __a2: int): ...



    def compareTo(self, __a0: ghidra.pcodeCPort.pcoderaw.VarnodeData) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.pcodeCPort.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: org.jdom.Element, __a1: ghidra.pcodeCPort.translate.Translate) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.pcodeCPort.address.Address: ...
