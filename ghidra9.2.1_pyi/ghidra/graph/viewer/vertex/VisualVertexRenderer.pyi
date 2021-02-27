import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.visualization
import ghidra.graph.viewer
import ghidra.graph.viewer.vertex
import java.awt
import java.lang


class VisualVertexRenderer(ghidra.graph.viewer.vertex.AbstractVisualVertexRenderer):
    """
    A renderer for the VisualGraph system.

     Rendering in the graph system is a bit different than other Java rendering systems.  For
     example, when a JTable renders itself, it uses a single renderer to stamp the data.  The
     table's renderer has no state and is updated for each cell's data that is to be rendered.
     The graph renderer system is different due to the possibility of complex vertex UIs.  Some
     vertices have sophisticated UI elements that have state.  For these vertices, it makes sense
     for the vertex to build and maintain that state; having that state repeatedly built by the
     renderer would be extremely inefficient and difficult to implement.  Considering that we
     expect the vertex to build and maintain its UI, this renderer is really just a tool to:

      Determine if the vertex needs to be painted (by clipping or filtering)

      Setup the geometry for the vertex (convert the model's location to the view location,
          accounting for panning and zooming)

      Paint any added effects (such as drop-shadows or highlighting)


    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFullShape(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualVertex) -> java.awt.Shape: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def paintVertex(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def paintVertex(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
