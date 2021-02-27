import edu.uci.ics.jung.visualization
import edu.uci.ics.jung.visualization.control
import ghidra.graph.viewer
import ghidra.graph.viewer.event.mouse
import java.awt
import java.awt.event
import java.lang


class VisualGraphAnimatedPickingGraphMousePlugin(edu.uci.ics.jung.visualization.control.AnimatedPickingGraphMousePlugin, ghidra.graph.viewer.event.mouse.VisualGraphMousePlugin):
    """
    A mouse handler to center a vertex when the header is double-clicked
    """





    def __init__(self): ...



    def checkModifiers(self, __a0: java.awt.event.MouseEvent) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCursor(self) -> java.awt.Cursor: ...

    def getGraphViewer(self, __a0: java.awt.event.MouseEvent) -> ghidra.graph.viewer.GraphViewer: ...

    def getModifiers(self) -> int: ...

    def getSatelliteGraphViewer(self, __a0: java.awt.event.MouseEvent) -> ghidra.graph.viewer.SatelliteGraphViewer: ...

    @overload
    def getViewUpdater(self, __a0: ghidra.graph.viewer.GraphViewer) -> ghidra.graph.viewer.VisualGraphViewUpdater: ...

    @overload
    def getViewUpdater(self, __a0: java.awt.event.MouseEvent) -> ghidra.graph.viewer.VisualGraphViewUpdater: ...

    def getViewer(self, __a0: java.awt.event.MouseEvent) -> edu.uci.ics.jung.visualization.VisualizationViewer: ...

    def hashCode(self) -> int: ...

    def mouseClicked(self, e: java.awt.event.MouseEvent) -> None: ...

    def mouseDragged(self, e: java.awt.event.MouseEvent) -> None: ...

    def mouseEntered(self, __a0: java.awt.event.MouseEvent) -> None: ...

    def mouseExited(self, __a0: java.awt.event.MouseEvent) -> None: ...

    def mouseMoved(self, e: java.awt.event.MouseEvent) -> None: ...

    def mousePressed(self, e: java.awt.event.MouseEvent) -> None: ...

    def mouseReleased(self, e: java.awt.event.MouseEvent) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCursor(self, __a0: java.awt.Cursor) -> None: ...

    def setModifiers(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
