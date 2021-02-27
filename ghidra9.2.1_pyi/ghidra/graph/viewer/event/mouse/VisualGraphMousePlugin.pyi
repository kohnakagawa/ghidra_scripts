import edu.uci.ics.jung.visualization
import ghidra.graph.viewer
import java.awt.event
import java.lang


class VisualGraphMousePlugin(object):
    """
    An interface to provide a common set of methods for classes that could not otherwise
     extend an abstract class.  This interface signals that the implementer is a VisualGraph
     mouse plugin.

     Note: The implementors of this interface still use the deprecated
     MouseEvent#getModifiers() method, since many of those classes extends from
     3rd-party classes that still use them, such as PickingGraphMousePlugin.   We will need
     to update the library (if/when possible), or rewrite our code so that it does not use the
     old 3rd-party algorithms.
    """









    def dispose(self) -> None:
        """
        Signals to perform any cleanup when this plugin is going away
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getGraphViewer(self, e: java.awt.event.MouseEvent) -> ghidra.graph.viewer.GraphViewer:
        """
        Returns the <b>primary/master</b> graph viewer.
        @param e the mouse event from which to get the viewer
        @return the viewer
        """
        ...

    def getSatelliteGraphViewer(self, e: java.awt.event.MouseEvent) -> ghidra.graph.viewer.SatelliteGraphViewer:
        """
        Returns the satellite graph viewer.  This assumes that the mouse event originated from
         the satellite viewer.
        @param e the mouse event from which to get the viewer
        @return the viewer
        """
        ...

    @overload
    def getViewUpdater(self, viewer: ghidra.graph.viewer.GraphViewer) -> ghidra.graph.viewer.VisualGraphViewUpdater:
        """
        Returns the updater that is used to modify the primary graph viewer.
        @param viewer the viewer
        @return the updater
        """
        ...

    @overload
    def getViewUpdater(self, e: java.awt.event.MouseEvent) -> ghidra.graph.viewer.VisualGraphViewUpdater:
        """
        Returns the updater that is used to modify the primary graph viewer.
        @param e the mouse event from which to get the viewer
        @return the updater
        """
        ...

    def getViewer(self, e: java.awt.event.MouseEvent) -> edu.uci.ics.jung.visualization.VisualizationViewer: ...

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
