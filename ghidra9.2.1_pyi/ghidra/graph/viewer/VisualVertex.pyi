import ghidra.graph
import java.awt
import java.awt.geom
import java.lang
import javax.swing


class VisualVertex(ghidra.graph.GVertex, object):
    """
    A vertex that contains properties and state related to a user interface.

     equals() and hashCode() - The graph API allows for cloning of layouts.  For this
     to correctly copy layout locations, each edge must override equals and
     hashCode in order to properly find edges across graphs.
    """









    def dispose(self) -> None:
        """
        A dispose method that should be called when a vertex is reclaimed, never again to be
         used in a graph or display
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAlpha(self) -> float:
        """
        Get the alpha, which determines how much of the vertex is visible/see through.  0 is
         completely transparent.  This attribute allows transitional for animations.
        @return the alpha value
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent:
        """
        Returns the component of this vertex.  This is used for rendering and interaction
         with the user.
        @return the component of this vertex
        """
        ...

    def getEmphasis(self) -> float:
        """
        Returns the emphasis value of this vertex.  0 if not emphasized.
        @return the emphasis value of this vertex.
        """
        ...

    def getLocation(self) -> java.awt.geom.Point2D:
        """
        Returns the location of this vertex in the view
        @return the location of this vertex in the view
        """
        ...

    def hashCode(self) -> int: ...

    def isFocused(self) -> bool:
        """
        Returns true if this vertex is focused (see {@link #setFocused(boolean)}
        @return true if focused
        """
        ...

    def isGrabbable(self, c: java.awt.Component) -> bool:
        """
        Returns true if the given component of this vertex is grabbable, which means that
         mouse drags on that component will move the vertex.

         <P>This is used to differentiate components within a vertex that should receive mouse
         events versus those components that will not be given mouse events.
        @param c the component
        @return true if the component is grabbable
        """
        ...

    def isHovered(self) -> bool:
        """
        Returns true if this vertex is being hovered by the mouse
        @return true if this vertex is being hovered by the mouse
        """
        ...

    def isSelected(self) -> bool:
        """
        Returns true if this vertex is selected
        @return true if this vertex is selected
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAlpha(self, alpha: float) -> None:
        """
        Set the alpha, which determines how much of the vertex is visible/see through.  0 is
         completely transparent.  This attribute allows transitional for animations.
        @param alpha the alpha value
        """
        ...

    def setEmphasis(self, emphasisLevel: float) -> None:
        """
        Sets the emphasis value for this vertex.  A value of 0 indicates no emphasis.
        @param emphasisLevel the emphasis
        """
        ...

    def setFocused(self, focused: bool) -> None:
        """
        Sets this vertex to be focused.   This differs from being selected in that multiple
         vertices in a graph can be selected, but only one can be the focused vertex.
        @param focused true to focus; false to be marked as not focused
        """
        ...

    def setHovered(self, hovered: bool) -> None:
        """
        Sets this vertex to be hovered
        @param hovered true to be marked as hovered; false to be marked as not hovered
        """
        ...

    def setLocation(self, p: java.awt.geom.Point2D) -> None:
        """
        Sets the location of this vertex in the view
        @param p the location of this vertex in the view
        """
        ...

    def setSelected(self, selected: bool) -> None:
        """
        Sets this vertex selected
        @param selected true to select this vertex; false to de-select this vertex
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
    def component(self) -> javax.swing.JComponent: ...

    @property
    def emphasis(self) -> float: ...

    @emphasis.setter
    def emphasis(self, value: float) -> None: ...

    @property
    def focused(self) -> bool: ...

    @focused.setter
    def focused(self, value: bool) -> None: ...

    @property
    def hovered(self) -> bool: ...

    @hovered.setter
    def hovered(self, value: bool) -> None: ...

    @property
    def location(self) -> java.awt.geom.Point2D: ...

    @location.setter
    def location(self, value: java.awt.geom.Point2D) -> None: ...

    @property
    def selected(self) -> bool: ...

    @selected.setter
    def selected(self, value: bool) -> None: ...
