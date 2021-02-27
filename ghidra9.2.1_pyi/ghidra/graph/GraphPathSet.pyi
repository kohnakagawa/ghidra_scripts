import ghidra.graph
import java.lang
import java.util


class GraphPathSet(object):




    def __init__(self): ...



    def add(self, path: ghidra.graph.GraphPath) -> None: ...

    def containSomePathStartingWith(self, otherPath: ghidra.graph.GraphPath) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPathsContaining(self, __a0: object) -> java.util.Set: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def size(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
