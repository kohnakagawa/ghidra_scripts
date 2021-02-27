import edu.uci.ics.jung.visualization.control
import java.awt
import java.awt.event
import java.lang


class JungPickingGraphMousePlugin(edu.uci.ics.jung.visualization.control.AbstractGraphMousePlugin, java.awt.event.MouseListener, java.awt.event.MouseMotionListener):
    """
    PickingGraphMousePlugin supports the picking of graph elements
     with the mouse. MouseButtonOne picks a single vertex
     or edge, and MouseButtonTwo adds to the set of selected Vertices
     or EdgeType. If a Vertex is selected and the mouse is dragged while
     on the selected Vertex, then that Vertex will be repositioned to
     follow the mouse until the button is released.
    """





    @overload
    def __init__(self):
        """
        create an instance with default settings
        """
        ...

    @overload
    def __init__(self, selectionModifiers: int, addToSelectionModifiers: int):
        """
        create an instance with overrides
        @param selectionModifiers for primary selection
        @param addToSelectionModifiers for additional selection
        """
        ...



    def checkModifiers(self, __a0: java.awt.event.MouseEvent) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCursor(self) -> java.awt.Cursor: ...

    def getLensColor(self) -> java.awt.Color:
        """
        @return Returns the lensColor.
        """
        ...

    def getModifiers(self) -> int: ...

    def hashCode(self) -> int: ...

    def isLocked(self) -> bool:
        """
        @return Returns the locked.
        """
        ...

    def mouseClicked(self, e: java.awt.event.MouseEvent) -> None: ...

    def mouseDragged(self, e: java.awt.event.MouseEvent) -> None:
        """
        If the mouse is over a picked vertex, drag all picked
         vertices with the mouse.
         If the mouse is not over a Vertex, draw the rectangle
         to select multiple Vertices
        """
        ...

    def mouseEntered(self, e: java.awt.event.MouseEvent) -> None: ...

    def mouseExited(self, e: java.awt.event.MouseEvent) -> None: ...

    def mouseMoved(self, e: java.awt.event.MouseEvent) -> None: ...

    def mousePressed(self, e: java.awt.event.MouseEvent) -> None:
        """
        For primary modifiers (default, MouseButton1):
         pick a single Vertex or Edge that
         is under the mouse pointer. If no Vertex or edge is under
         the pointer, unselect all picked Vertices and edges, and
         set up to draw a rectangle for multiple selection
         of contained Vertices.
         For additional selection (default Shift+MouseButton1):
         Add to the selection, a single Vertex or Edge that is
         under the mouse pointer. If a previously picked Vertex
         or Edge is under the pointer, it is un-picked.
         If no vertex or Edge is under the pointer, set up
         to draw a multiple selection rectangle (as above)
         but do not unpick previously picked elements.
        @param e the event
        """
        ...

    def mouseReleased(self, e: java.awt.event.MouseEvent) -> None:
        """
        If the mouse is dragging a rectangle, pick the
         Vertices contained in that rectangle

         clean up settings from mousePressed
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCursor(self, __a0: java.awt.Cursor) -> None: ...

    def setLensColor(self, lensColor: java.awt.Color) -> None:
        """
        @param lensColor The lensColor to set.
        """
        ...

    def setLocked(self, locked: bool) -> None:
        """
        @param locked The locked to set.
        """
        ...

    def setModifiers(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def lensColor(self) -> java.awt.Color: ...

    @lensColor.setter
    def lensColor(self, value: java.awt.Color) -> None: ...

    @property
    def locked(self) -> bool: ...

    @locked.setter
    def locked(self, value: bool) -> None: ...
