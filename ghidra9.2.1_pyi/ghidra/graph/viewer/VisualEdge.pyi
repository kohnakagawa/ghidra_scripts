from typing import List
import ghidra.graph
import ghidra.graph.viewer
import java.awt.geom
import java.lang


class VisualEdge(ghidra.graph.GEdge, object):
    """
    An edge that contains properties and state related to a user interface.

     An edge can be selected, which means that it has been clicked by the user.  Also, an
     edge can be part of an active path.  This allows the UI to paint the edge differently if it
     is in the active path.   The active path concept applies to both hovered and focused vertices
     separately.  A hovered vertex is one that the user moves the mouse over; a focused vertex is
     one that is selected.


     Articulations - The start and end points are always part of the
     edge.  Any additional points on the edge are considered articulation points.  Thus, an edge
     without articulations will be drawn as a straight line.  An edge with articulations will
     be drawn as a series of straight lines from point-to-point, allowing the layout algorithm
     to add points to the edge to avoid line crossings; these points are used to make the
     drawing of the edge cleaner.

     equals() and hashCode() - The graph API allows for cloning of layouts.  For this
     to correctly copy layout locations, each edge must override equals and
     hashCode in order to properly find edges across graphs.
    """









    def cloneEdge(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: ghidra.graph.viewer.VisualVertex) -> ghidra.graph.viewer.VisualEdge: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlpha(self) -> float:
        """
        Get the alpha, which determines how much of the edge is visible/see through.  0 is
         completely transparent.  This attribute allows transitional for animations.
        @return the alpha value
        """
        ...

    def getArticulationPoints(self) -> List[java.awt.geom.Point2D]:
        """
        Returns the points (in {@link GraphViewerUtils} View Space) of the articulation

         <P><A HREF="#articulations">What are articulations?</A>
        @return the points (in View Space space) of the articulation.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEmphasis(self) -> float:
        """
        Returns the emphasis value of this edge.  0 if not emphasized.
        @return the emphasis value of this edge.
        """
        ...

    def getEnd(self) -> object: ...

    def getStart(self) -> object: ...

    def hashCode(self) -> int: ...

    def isInFocusedVertexPath(self) -> bool:
        """
        Returns true if this edge is part of an active path for a currently focused/selected
         vertex (this allows the edge to be differently rendered)
        @return true if this edge is part of the active path
        """
        ...

    def isInHoveredVertexPath(self) -> bool:
        """
        Returns true if this edge is part of an active path for a currently hovered
         vertex (this allows the edge to be differently rendered)
        @return true if this edge is part of the active path
        """
        ...

    def isSelected(self) -> bool:
        """
        Returns true if this edge is selected
        @return true if this edge is selected
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAlpha(self, alpha: float) -> None:
        """
        Set the alpha, which determines how much of the edge is visible/see through.  0 is
         completely transparent.  This attribute allows transitional for animations.
        @param alpha the alpha value
        """
        ...

    def setArticulationPoints(self, __a0: List[object]) -> None: ...

    def setEmphasis(self, emphasisLevel: float) -> None:
        """
        Sets the emphasis value for this edge.  A value of 0 indicates no emphasis.
        @param emphasisLevel the emphasis
        """
        ...

    def setInFocusedVertexPath(self, inPath: bool) -> None:
        """
        Sets this edge to be marked as in the active path of a currently focused/selected vertex
        @param inPath true to be marked as in the active path; false to be marked as not
                in the active path
        """
        ...

    def setInHoveredVertexPath(self, inPath: bool) -> None:
        """
        Sets this edge to be marked as in the active path of a currently hovered vertex
        @param inPath true to be marked as in the active path; false to be marked as not
                in the active path
        """
        ...

    def setSelected(self, selected: bool) -> None:
        """
        Sets this edge selected.  This is usually in response to the user selecting the edge.
        @param selected true to select this edge; false to de-select this vertex
        """
        ...

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
    def end(self) -> object: ...

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
    def start(self) -> object: ...
