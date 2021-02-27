from typing import List
import ghidra.app.plugin.core.functiongraph
import ghidra.graph.viewer
import java.lang


class EdgeDisplayType(java.lang.Enum):
    AllCycles: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = AllCycles
    Cycles: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = Cycles
    Off: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = Off
    PathsFromToVertex: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = PathsFromToVertex
    PathsFromVertex: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = PathsFromVertex
    PathsFromVertexToVertex: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = PathsFromVertexToVertex
    PathsToVertex: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = PathsToVertex
    ScopedFlowsFromVertex: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = ScopedFlowsFromVertex
    ScopedFlowsToVertex: ghidra.app.plugin.core.functiongraph.EdgeDisplayType = ScopedFlowsToVertex







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAsPathHighlightHoverMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

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
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.functiongraph.EdgeDisplayType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.functiongraph.EdgeDisplayType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def asPathHighlightHoverMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...
