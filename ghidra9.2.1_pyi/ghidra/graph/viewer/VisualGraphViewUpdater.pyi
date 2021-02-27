import edu.uci.ics.jung.visualization
import ghidra.graph.job
import ghidra.graph.viewer
import ghidra.util.task
import java.awt
import java.awt.geom
import java.lang
import java.util
import utility.function


class VisualGraphViewUpdater(object):
    """
    This is the class through which operations travel that manipulate the view and graph while
     plugged-in to the UI.   (Setup and tear down operations performed before the view
     or graph are visible need not pass through this class.)  This class is responsible for
     controlling how to display view and graph changes, including whether to animate.

     The animations are categorized into those that mutate the graph and those that are just
     display animations (like hover animations).
    """





    def __init__(self, primaryViewer: ghidra.graph.viewer.GraphViewer, graph: ghidra.graph.VisualGraph): ...



    def addJobScheduledListener(self, c: utility.function.Callback) -> None:
        """
        Add a listener to be notified when a job is started.  Jobs often, but not always, mutate
         the underlying graph.  For this reason, other tasks that use the graph may want to not
         do their work while a job is running.
        @param c the listener
        """
        ...

    def animateEdgeHover(self) -> None: ...

    def centerLayoutSpacePointWithoutAnimation(self, point: java.awt.Point) -> None: ...

    def centerViewSpacePointWithAnimation(self, point: java.awt.Point) -> None: ...

    def centerViewSpacePointWithoutAnimation(self, point: java.awt.Point) -> None: ...

    def dispose(self) -> None: ...

    def ensureVertexAreaVisible(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.Rectangle, __a2: ghidra.util.task.BusyListener) -> None: ...

    def ensureVertexVisible(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.Rectangle) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fitAllGraphsToViewsNow(self) -> None:
        """
        Fits the graph into both the primary and satellite views
        """
        ...

    @overload
    def fitGraphToViewerLater(self) -> None:
        """
        Will schedule the fitting work to happen now if now work is being done, or later otherwis
        """
        ...

    @overload
    def fitGraphToViewerLater(self, theViewer: edu.uci.ics.jung.visualization.VisualizationServer) -> None: ...

    @overload
    def fitGraphToViewerNow(self) -> None: ...

    @overload
    def fitGraphToViewerNow(self, theViewer: edu.uci.ics.jung.visualization.VisualizationServer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isAnimationEnabled(self) -> bool: ...

    def isBusy(self) -> bool:
        """
        Returns true if this updater is performing any animations or running any jobs that can
         mutate the graph or view
        @return true if busy
        """
        ...

    def isMutatingGraph(self) -> bool:
        """
        Returns true if this updater is running any jobs that can mutate the graph or view
        @return true if busy
        """
        ...

    @overload
    def moveVertexToCenterTopWithAnimation(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def moveVertexToCenterTopWithAnimation(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: ghidra.util.task.BusyListener) -> None: ...

    def moveVertexToCenterTopWithoutAnimation(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def moveVertexToCenterWithAnimation(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def moveVertexToCenterWithAnimation(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: ghidra.util.task.BusyListener) -> None: ...

    def moveVertexToCenterWithoutAnimation(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    def moveViewerLocationWithoutAnimation(self, translation: java.awt.Point) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def scheduleViewChangeJob(self, job: ghidra.graph.job.GraphJob) -> None: ...

    def setGraphPerspective(self, graphInfo: ghidra.graph.viewer.GraphPerspectiveInfo) -> None: ...

    def setGraphScale(self, scale: float) -> None: ...

    def setLayoutSpacePointWithAnimation(self, point: java.awt.Point) -> None: ...

    def setLayoutSpacePointWithoutAnimation(self, point: java.awt.geom.Point2D) -> None: ...

    def stopAllAnimation(self) -> None: ...

    def stopEdgeHoverAnimation(self) -> None: ...

    def toString(self) -> unicode: ...

    def twinkeVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    def updateEdgeShapes(self, edges: java.util.Collection) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    def zoomInCompletely(self) -> None: ...

    @overload
    def zoomInCompletely(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    @property
    def animationEnabled(self) -> bool: ...

    @property
    def busy(self) -> bool: ...

    @property
    def graphPerspective(self) -> None: ...  # No getter available.

    @graphPerspective.setter
    def graphPerspective(self, value: ghidra.graph.viewer.GraphPerspectiveInfo) -> None: ...

    @property
    def graphScale(self) -> None: ...  # No getter available.

    @graphScale.setter
    def graphScale(self, value: float) -> None: ...

    @property
    def layoutSpacePointWithAnimation(self) -> None: ...  # No getter available.

    @layoutSpacePointWithAnimation.setter
    def layoutSpacePointWithAnimation(self, value: java.awt.Point) -> None: ...

    @property
    def layoutSpacePointWithoutAnimation(self) -> None: ...  # No getter available.

    @layoutSpacePointWithoutAnimation.setter
    def layoutSpacePointWithoutAnimation(self, value: java.awt.geom.Point2D) -> None: ...

    @property
    def mutatingGraph(self) -> bool: ...
