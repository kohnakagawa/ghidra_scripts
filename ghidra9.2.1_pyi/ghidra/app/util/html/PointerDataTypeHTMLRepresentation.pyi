from typing import List
import ghidra.app.util.html
import java.lang


class PointerDataTypeHTMLRepresentation(ghidra.app.util.html.HTMLDataTypeRepresentation):




    def __init__(self, pointer: ghidra.program.model.data.Pointer): ...



    def diff(self, otherRepresentation: ghidra.app.util.html.HTMLDataTypeRepresentation) -> List[ghidra.app.util.html.HTMLDataTypeRepresentation]: ...

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
