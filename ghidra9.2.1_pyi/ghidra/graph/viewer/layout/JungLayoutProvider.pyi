import ghidra.graph
import ghidra.graph.graphs
import ghidra.graph.viewer.layout
import ghidra.util.task
import java.lang
import javax.swing


class JungLayoutProvider(ghidra.graph.viewer.layout.AbstractLayoutProvider):
    """
    A layout provider that works on JungDirectedVisualGraphs.  This class allows the
     Jung layouts to be used where VisualGraphs are used.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getActionIcon(self) -> javax.swing.Icon: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getLayout(self, __a0: ghidra.graph.graphs.JungDirectedVisualGraph, __a1: ghidra.util.task.TaskMonitor) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    @overload
    def getLayout(self, __a0: ghidra.graph.VisualGraph, __a1: ghidra.util.task.TaskMonitor) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    def getLayoutName(self) -> unicode: ...

    def getPriorityLevel(self) -> int: ...

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

    @property
    def actionIcon(self) -> javax.swing.Icon: ...
