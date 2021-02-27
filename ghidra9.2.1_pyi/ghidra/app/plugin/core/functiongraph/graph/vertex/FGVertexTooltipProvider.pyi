import ghidra.app.plugin.core.functiongraph.graph
import ghidra.app.plugin.core.functiongraph.graph.vertex
import ghidra.graph.viewer.event.mouse
import java.awt.event
import java.lang
import javax.swing


class FGVertexTooltipProvider(object, ghidra.graph.viewer.event.mouse.VertexTooltipProvider):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getTooltip(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> javax.swing.JComponent: ...

    @overload
    def getTooltip(self, __a0: object) -> javax.swing.JComponent: ...

    @overload
    def getTooltip(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a1: ghidra.app.plugin.core.functiongraph.graph.FGEdge) -> javax.swing.JComponent: ...

    @overload
    def getTooltip(self, __a0: object, __a1: object) -> javax.swing.JComponent: ...

    @overload
    def getTooltipText(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a1: java.awt.event.MouseEvent) -> unicode: ...

    @overload
    def getTooltipText(self, __a0: object, __a1: java.awt.event.MouseEvent) -> unicode: ...

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
