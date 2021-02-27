import ghidra.graph.viewer.actions
import java.lang


class VisualGraphVertexActionContext(ghidra.graph.viewer.actions.VisualGraphActionContext, object):
    """
    Context for a VisualGraph when a vertex is selected
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getVertex(self) -> V: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shouldShowSatelliteActions(self) -> bool:
        """
        Returns true actions that manipulate the satellite viewer should be enabled for this context
        @return true actions that manipulate the satellite viewer should be enabled for this context
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
    def vertex(self) -> ghidra.graph.viewer.VisualVertex: ...
