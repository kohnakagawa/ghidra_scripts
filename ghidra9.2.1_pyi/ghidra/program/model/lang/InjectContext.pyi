import ghidra.program.model.address
import java.lang
import javax.xml.parsers


class InjectContext(object):
    baseAddr: ghidra.program.model.address.Address
    callAddr: ghidra.program.model.address.Address
    inputlist: java.util.ArrayList
    language: ghidra.app.plugin.processors.sleigh.SleighLanguage
    nextAddr: ghidra.program.model.address.Address
    output: java.util.ArrayList
    refAddr: ghidra.program.model.address.Address



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: javax.xml.parsers.SAXParser, xml: unicode, addrFactory: ghidra.program.model.address.AddressFactory) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
