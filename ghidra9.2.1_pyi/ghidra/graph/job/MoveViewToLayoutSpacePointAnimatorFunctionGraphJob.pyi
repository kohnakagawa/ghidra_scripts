import ghidra.graph.job
import ghidra.util.task
import java.awt.geom
import java.lang


class MoveViewToLayoutSpacePointAnimatorFunctionGraphJob(ghidra.graph.job.MoveViewAnimatorFunctionGraphJob):




    def __init__(self, viewer: edu.uci.ics.jung.visualization.VisualizationServer, layoutSpacePoint: java.awt.geom.Point2D, useAnimation: bool): ...



    def canShortcut(self) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, listener: ghidra.graph.job.GraphJobListener) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isFinished(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBusyListener(self, listener: ghidra.util.task.BusyListener) -> None: ...

    def setOffset(self, offsetFromOriginalPoint: java.awt.geom.Point2D) -> None: ...

    def shortcut(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
