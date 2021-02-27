import ghidra.app.plugin.core.functiongraph.action
import ghidra.app.plugin.core.functiongraph.graph.vertex
import ghidra.program.model.address
import java.lang
import java.util


class FullScreenModeVertexActionContextInfo(ghidra.app.plugin.core.functiongraph.action.VertexActionContextInfo):




    def __init__(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex): ...



    def equals(self, __a0: object) -> bool: ...

    def getActiveVertex(self) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    def getClass(self) -> java.lang.Class: ...

    def getHoveredVertexAddresses(self) -> ghidra.program.model.address.AddressSet: ...

    def getSelectedVertexAddresses(self) -> ghidra.program.model.address.AddressSet: ...

    def getSelectedVertices(self) -> java.util.Set: ...

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
