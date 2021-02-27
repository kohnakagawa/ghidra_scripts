import ghidra.graph.job
import ghidra.util.task
import java.lang


class TwinkleVertexAnimator(ghidra.graph.job.AbstractAnimator):
    """
    A class to animate a vertex in order to draw attention to it.

     Note: this class is not a AbstractAnimatorJob so that it can run concurrently
     with jobs in the graph (jobs run one-at-a-time).
    """





    def __init__(self, __a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: ghidra.graph.viewer.VisualVertex, __a2: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getVertex(self) -> V: ...

    def hasFinished(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isRunning(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBusyListener(self, listener: ghidra.util.task.BusyListener) -> None: ...

    def setCurrentEmphasis(self, currentEmphasis: float) -> None: ...

    def start(self) -> None: ...

    def stop(self) -> None:
        """
        Stops this animator <b>and all scheduled animators!</b>
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
    def currentEmphasis(self) -> None: ...  # No getter available.

    @currentEmphasis.setter
    def currentEmphasis(self, value: float) -> None: ...

    @property
    def vertex(self) -> ghidra.graph.viewer.VisualVertex: ...
