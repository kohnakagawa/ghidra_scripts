import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.visualization
import ghidra.graph.viewer
import ghidra.graph.viewer.vertex
import java.awt
import java.lang


class FGVertexRenderer(ghidra.graph.viewer.vertex.VisualVertexRenderer):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFullShape(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualVertex) -> java.awt.Shape: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def paintVertex(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def paintVertex(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
