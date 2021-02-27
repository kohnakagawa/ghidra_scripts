import ghidra.util.bytesearch
import ghidra.xml
import java.lang


class PostRule(object):
    """
    Inteface for post match rules that are checked after a match is idenfied
    """









    def apply(self, pat: ghidra.util.bytesearch.Pattern, matchoffset: long) -> bool:
        """
        Apply a post rule given the matching pattern and offset into the byte stream.
        @param pat pattern that matched
        @param matchoffset offset of the match
        @return true if the PostRule is satisfied
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None:
        """
        Can restore state of instance PostRule from XML
        @param parser XML pull parser
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
