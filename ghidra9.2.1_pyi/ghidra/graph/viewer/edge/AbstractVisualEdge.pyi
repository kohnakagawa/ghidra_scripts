from typing import List
import ghidra.graph.viewer
import java.awt.geom
import java.lang


class AbstractVisualEdge(object, ghidra.graph.viewer.VisualEdge):
    """
    An implementation of VisualEdge that implements the base interface so subclasses
     do not have to.
    """





    def __init__(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: ghidra.graph.viewer.VisualVertex): ...



    def cloneEdge(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: ghidra.graph.viewer.VisualVertex) -> ghidra.graph.viewer.VisualEdge: ...

    def equals(self, obj: object) -> bool: ...

    def getAlpha(self) -> float: ...

    def getArticulationPoints(self) -> List[java.awt.geom.Point2D]: ...

    def getClass(self) -> java.lang.Class: ...

    def getEmphasis(self) -> float: ...

    def getEnd(self) -> V: ...

    def getStart(self) -> V: ...

    def hashCode(self) -> int: ...

    def isInFocusedVertexPath(self) -> bool: ...

    def isInHoveredVertexPath(self) -> bool: ...

    def isSelected(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAlpha(self, alpha: float) -> None: ...

    def setArticulationPoints(self, __a0: List[object]) -> None: ...

    def setEmphasis(self, emphasisLevel: float) -> None: ...

    def setInFocusedVertexPath(self, inPath: bool) -> None: ...

    def setInHoveredVertexPath(self, inPath: bool) -> None: ...

    def setSelected(self, selected: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def alpha(self) -> float: ...

    @alpha.setter
    def alpha(self, value: float) -> None: ...

    @property
    def articulationPoints(self) -> List[object]: ...

    @articulationPoints.setter
    def articulationPoints(self, value: List[object]) -> None: ...

    @property
    def emphasis(self) -> float: ...

    @emphasis.setter
    def emphasis(self, value: float) -> None: ...

    @property
    def end(self) -> ghidra.graph.viewer.VisualVertex: ...

    @property
    def inFocusedVertexPath(self) -> bool: ...

    @inFocusedVertexPath.setter
    def inFocusedVertexPath(self, value: bool) -> None: ...

    @property
    def inHoveredVertexPath(self) -> bool: ...

    @inHoveredVertexPath.setter
    def inHoveredVertexPath(self, value: bool) -> None: ...

    @property
    def selected(self) -> bool: ...

    @selected.setter
    def selected(self, value: bool) -> None: ...

    @property
    def start(self) -> ghidra.graph.viewer.VisualVertex: ...