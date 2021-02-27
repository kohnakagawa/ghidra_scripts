import ghidra.graph.job
import ghidra.util.task
import java.lang


class MergeVertexFunctionGraphJob(ghidra.graph.job.AbstractAnimatorJob):




    def __init__(self, __a0: ghidra.app.plugin.core.functiongraph.mvc.FGController, __a1: edu.uci.ics.jung.visualization.VisualizationServer, __a2: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a3: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a4: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a5: bool): ...



    def canShortcut(self) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, __a0: ghidra.graph.job.GraphJobListener) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isFinished(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBusyListener(self, __a0: ghidra.util.task.BusyListener) -> None: ...

    def setPercentComplete(self, __a0: float) -> None: ...

    def shortcut(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def percentComplete(self) -> None: ...  # No getter available.

    @percentComplete.setter
    def percentComplete(self, value: float) -> None: ...
