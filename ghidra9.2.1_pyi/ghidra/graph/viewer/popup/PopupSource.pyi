import ghidra.graph.viewer.popup
import java.awt
import java.awt.event
import java.lang


class PopupSource(object):
    """
    An interface that provides graph and component information to the PopupRegulator
    """









    def addMouseMotionListener(self, l: java.awt.event.MouseMotionListener) -> None:
        """
        Adds the given mouse motion listener to the graph component.  This allows the popup
         regulator to decided when to show and hide popups.
        @param l the listener
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdge(self, event: java.awt.event.MouseEvent) -> E:
        """
        Returns an edge for the given event
        @param event the event
        @return the edge or null
        """
        ...

    def getPopupParent(self) -> java.awt.Window:
        """
        Returns a suitable window parent for the popup window
        @return the window parent
        """
        ...

    def getToolTipInfo(self, event: java.awt.event.MouseEvent) -> ghidra.graph.viewer.popup.ToolTipInfo:
        """
        Returns the tool tip info object for the given mouse event.  Implementations will use the
         event to determine whether a popup should be created for a vertex, edge, the graph or
         not at all.
        @param event the event
        @return the info; null for no popup
        """
        ...

    def getVertex(self, event: java.awt.event.MouseEvent) -> V:
        """
        Returns a vertex for the given event
        @param event the event
        @return the vertex or null
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def repaint(self) -> None:
        """
        Signals that the graph needs to repaint
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
    def popupParent(self) -> java.awt.Window: ...
