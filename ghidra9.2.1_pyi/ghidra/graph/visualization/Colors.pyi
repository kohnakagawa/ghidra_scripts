import ghidra.service.graph
import java.awt
import java.lang


class Colors(object):
    EDGE_TYPE_TO_COLOR_MAP: java.util.Map
    VERTEX_TYPE_TO_COLOR_MAP: java.util.Map







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getColor(__a0: ghidra.service.graph.Attributed) -> java.awt.Paint: ...

    @staticmethod
    def getHexColor(__a0: unicode) -> java.awt.Color: ...

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
