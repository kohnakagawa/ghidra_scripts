from typing import List
import ghidra.graph.viewer
import java.lang


class PathHighlightMode(java.lang.Enum):
    ALLCYCLE: ghidra.graph.viewer.PathHighlightMode = ALLCYCLE
    CYCLE: ghidra.graph.viewer.PathHighlightMode = CYCLE
    IN: ghidra.graph.viewer.PathHighlightMode = IN
    INOUT: ghidra.graph.viewer.PathHighlightMode = INOUT
    OFF: ghidra.graph.viewer.PathHighlightMode = OFF
    OUT: ghidra.graph.viewer.PathHighlightMode = OUT
    PATH: ghidra.graph.viewer.PathHighlightMode = PATH
    SCOPED_FORWARD: ghidra.graph.viewer.PathHighlightMode = SCOPED_FORWARD
    SCOPED_REVERSE: ghidra.graph.viewer.PathHighlightMode = SCOPED_REVERSE







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.graph.viewer.PathHighlightMode: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.graph.viewer.PathHighlightMode]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
