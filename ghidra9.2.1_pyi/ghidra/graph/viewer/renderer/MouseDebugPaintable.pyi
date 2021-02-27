import edu.uci.ics.jung.visualization
import ghidra.graph.viewer
import ghidra.graph.viewer.renderer
import java.awt
import java.lang


class MouseDebugPaintable(object, edu.uci.ics.jung.visualization.VisualizationServer.Paintable):




    def __init__(self): ...



    def addShape(self, shape: ghidra.graph.viewer.renderer.PaintableShape, graphViewer: ghidra.graph.viewer.GraphViewer) -> None: ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paint(self, g: java.awt.Graphics) -> None: ...

    def toString(self) -> unicode: ...

    def useTransform(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
