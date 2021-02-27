import ghidra.app.plugin.core.functiongraph.action
import ghidra.graph.viewer
import ghidra.graph.viewer.actions
import java.lang
import java.util


class FunctionGraphVertexLocationContextIf(ghidra.app.plugin.core.functiongraph.action.FunctionGraphValidGraphActionContextIf, ghidra.graph.viewer.actions.VisualGraphVertexActionContext, object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSelectedVertices(self) -> java.util.Set: ...

    def getVertex(self) -> ghidra.graph.viewer.VisualVertex: ...

    def getVertexInfo(self) -> ghidra.app.plugin.core.functiongraph.action.VertexActionContextInfo: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shouldShowSatelliteActions(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def selectedVertices(self) -> java.util.Set: ...

    @property
    def vertex(self) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    @property
    def vertexInfo(self) -> ghidra.app.plugin.core.functiongraph.action.VertexActionContextInfo: ...
