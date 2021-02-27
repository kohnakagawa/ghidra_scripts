import ghidra.graph
import ghidra.graph.algo
import ghidra.util.datastruct
import ghidra.util.task
import java.lang


class IterativeFindPathsAlgorithm(object, ghidra.graph.algo.FindPathsAlgorithm):
    """
    Finds all paths between two vertices for a given graph.

     Note: this algorithm is based on the JohnsonCircuitsAlgorithm, modified to be
     iterative instead of recursive.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def findPaths(self, __a0: ghidra.graph.GDirectedGraph, __a1: object, __a2: object, __a3: ghidra.util.datastruct.Accumulator, __a4: ghidra.util.task.TaskMonitor) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setStatusListener(self, listener: ghidra.graph.algo.GraphAlgorithmStatusListener) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def statusListener(self) -> None: ...  # No getter available.

    @statusListener.setter
    def statusListener(self, value: ghidra.graph.algo.GraphAlgorithmStatusListener) -> None: ...
