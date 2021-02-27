from typing import List
import ghidra.graph.algo
import java.lang


class GraphAlgorithmStatusListener(object):
    """
    An interface and state values used to follow the state of vertices as they are processed by
     algorithms
    """






    class STATUS(java.lang.Enum):
        BLOCKED: ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS = BLOCKED
        EXPLORING: ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS = EXPLORING
        IN_PATH: ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS = IN_PATH
        SCHEDULED: ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS = SCHEDULED
        WAITING: ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS = WAITING







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def finished(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getTotalStatusChanges(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def statusChanged(self, __a0: object, __a1: ghidra.graph.algo.GraphAlgorithmStatusListener.STATUS) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def totalStatusChanges(self) -> int: ...
