import ghidra.graph.viewer
import ghidra.graph.viewer.edge
import java.lang


class VisualGraphPathHighlighter(object):
    """
    A class that calculates flow between vertices and then triggers that flow to be painted
     in the UI.

     Threading Policy:  Some operations use algorithms that slow down, depending
     upon the graph size.  Further, some of these algorithms may not even complete.  To keep the
     graph responsive, this class will perform its work in the future.   The work we
     wish to do is further complicated by these requirements:

     	Some data should be calculated only as needed, to avoid excessive work
     	Many tasks depend on data to be calculated before they can perform their algorithm
     	Results must be cached for speed, but may cleared as the graph is mutated
      Algorithms must not block the UI thread
      Related actions (i.e., hover vs. selection) should cancel any pending action, but not
          unrelated actions (e.g., a new hover request should cancel a pending hover update)


     Based on these requirements, we need to use multi-threading.  Further complicating the need
     for multi-threading is that some operations depending on lazy-loaded data.  Finally, we
     have different types of actions, hovering vs. selecting a vertex, which should override
     previous related requests.   To accomplish this we use:

     	CompletableFuture - to lazy-load and cache required algorithm data
     	RunManagers - to queue requests so that new requests cancel old ones.  A
          different Run Manager is used for each type of request.


     Naming Conventions:  There are many methods in this class, called from
     different threads.   For simplicity, we use the following conventions:

     	fooAsync - methods ending in Async indicate that they are to be
                                  called from a background thread.
      fooSwing - methods ending in Swing indicate that they are to be
                                  called from the Swing thread.
     	*All public methods are assumed to be called on the Swing thread

    """





    def __init__(self, graph: ghidra.graph.VisualGraph, listener: ghidra.graph.viewer.edge.PathHighlightListener): ...



    def clearEdgeCache(self) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getVertexFocusPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def getVertexHoverPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setFocusedVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    def setHoveredVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    def setVertexFocusMode(self, mode: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    def setVertexHoverMode(self, mode: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    def setWorkPauser(self, pauser: ghidra.graph.viewer.edge.PathHighlighterWorkPauser) -> None:
        """
        Sets the callback that signals when this path highlighter should not be performing any
         work
        @param pauser the callback that returns a boolean of true when this class should pause
                its work.
        """
        ...

    def stop(self) -> None:
        """
        Signals to this path highlighter that it should stop all background jobs
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
    def busy(self) -> bool: ...

    @property
    def focusedVertex(self) -> None: ...  # No getter available.

    @focusedVertex.setter
    def focusedVertex(self, value: ghidra.graph.viewer.VisualVertex) -> None: ...

    @property
    def hoveredVertex(self) -> None: ...  # No getter available.

    @hoveredVertex.setter
    def hoveredVertex(self, value: ghidra.graph.viewer.VisualVertex) -> None: ...

    @property
    def vertexFocusMode(self) -> None: ...  # No getter available.

    @vertexFocusMode.setter
    def vertexFocusMode(self, value: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    @property
    def vertexFocusPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    @property
    def vertexHoverMode(self) -> None: ...  # No getter available.

    @vertexHoverMode.setter
    def vertexHoverMode(self, value: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    @property
    def vertexHoverPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    @property
    def workPauser(self) -> None: ...  # No getter available.

    @workPauser.setter
    def workPauser(self, value: ghidra.graph.viewer.edge.PathHighlighterWorkPauser) -> None: ...
