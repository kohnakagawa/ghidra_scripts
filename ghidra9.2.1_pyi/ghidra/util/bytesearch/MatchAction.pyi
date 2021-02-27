import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.bytesearch
import ghidra.xml
import java.lang


class MatchAction(object):
    """
    Interface for a match action to be taken for the Program@Address for a ditted bit seqence pattern
    """









    def apply(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, match: ghidra.util.bytesearch.Match) -> None:
        """
        Apply the match action to the program at the address.
        @param program program in which the match occurred
        @param addr where the match occured
        @param match information about the match that occurred
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None:
        """
        Action can be constructed from XML
        @param parser XML pull parser to restore action from XML
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
