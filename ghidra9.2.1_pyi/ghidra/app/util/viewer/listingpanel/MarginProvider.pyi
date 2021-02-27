import ghidra.app.util.viewer.listingpanel
import ghidra.program.util
import java.lang
import javax.swing


class MarginProvider(object):
    """
    Interface for objects that want to add a component to the listings left margin.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent:
        """
        Get the component to show the margin markers.
        """
        ...

    def getMarkerLocation(self, x: int, y: int) -> ghidra.program.util.MarkerLocation:
        """
        Get the marker location for the given x, y point.
        @param x the horizontal coordinate.
        @param y the vertical coordinate.
        """
        ...

    def hashCode(self) -> int: ...

    def isResizeable(self) -> bool:
        """
        Return whether the component can be resized.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setPixelMap(self, pixmap: ghidra.app.util.viewer.listingpanel.VerticalPixelAddressMap) -> None:
        """
        Set the vertical pixel layout map.
        @param pixmap the vertical pixel map to use.
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
    def component(self) -> javax.swing.JComponent: ...

    @property
    def pixelMap(self) -> None: ...  # No getter available.

    @pixelMap.setter
    def pixelMap(self, value: ghidra.app.util.viewer.listingpanel.VerticalPixelAddressMap) -> None: ...

    @property
    def resizeable(self) -> bool: ...
