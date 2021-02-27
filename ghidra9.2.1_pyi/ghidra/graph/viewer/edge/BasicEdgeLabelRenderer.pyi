import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.visualization
import edu.uci.ics.jung.visualization.renderers
import ghidra.graph.viewer
import java.awt
import java.lang


class BasicEdgeLabelRenderer(edu.uci.ics.jung.visualization.renderers.BasicEdgeLabelRenderer):
    """
    A class to override the default edge label placement.   This class is called a renderer because
     the parent class is.  However, it is not a renderer in the sense that it's job is to paint
     the contents, like in Java when you provide a cell rendering component, but rather, it uses
     such a component.  Further, the job of this class is to position said component and then to
     have it paint its contents.

     Normally we would just set our custom renderer on the RenderContext at construction
     time, like we do with the other rendering classes, but not such method is provided.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    def labelEdge(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualEdge, __a3: unicode) -> None: ...

    @overload
    def labelEdge(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: object, __a3: unicode) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def prepareRenderer(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.visualization.renderers.EdgeLabelRenderer, __a2: object, __a3: bool, __a4: object) -> java.awt.Component: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
