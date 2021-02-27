import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.bytesearch
import ghidra.xml
import java.lang


class DummyMatchAction(object, ghidra.util.bytesearch.MatchAction):
    """
    Dummy action attached to a match sequence.  Action is not restored from XML
    """





    def __init__(self): ...



    def apply(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, match: ghidra.util.bytesearch.Match) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
