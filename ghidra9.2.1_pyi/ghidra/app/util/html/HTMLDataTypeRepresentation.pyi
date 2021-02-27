from typing import List
import ghidra.app.util.html
import java.lang


class HTMLDataTypeRepresentation(object):








    def diff(self, otherRepresentation: ghidra.app.util.html.HTMLDataTypeRepresentation) -> List[ghidra.app.util.html.HTMLDataTypeRepresentation]:
        """
        Compares this representation and the given representation creates a diff string for both
         representations.
        @param otherRepresentation the other representation to diff against.
        @return An array of two strings: the first is this object's diff value, the second is the
                 given objects diff value.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHTMLContentString(self) -> unicode:
        """
        This is like {@link #getHTMLString()}, but does not put HTML tags around the data.
        """
        ...

    def getHTMLString(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def HTMLContentString(self) -> unicode: ...

    @property
    def HTMLString(self) -> unicode: ...
