import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.bytesearch
import ghidra.xml
import java.lang


class GenericMatchAction(ghidra.util.bytesearch.DummyMatchAction):
    """
    Template for generic match action attached to a match sequence.
     Used to store an associated value to the matching sequence.
     The associated value can be retrieved when the sequence is matched.
    """





    def __init__(self, matchValue: object):
        """
        Construct a match action used when a match occurs for some GenericByteSequece
        @param matchValue specialized object used when match occurs
        """
        ...



    def apply(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, match: ghidra.util.bytesearch.Match) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMatchValue(self) -> object:
        """
        @return the specialized object associated with this match action
        """
        ...

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

    @property
    def matchValue(self) -> object: ...
