import ghidra.graph.viewer.layout
import java.lang
import java.util


class JungLayoutProviderFactory(object):
    """
    A factory to produce JungLayoutProviders that can be used to layout
     VisualGraphs
    """





    def __init__(self): ...



    @staticmethod
    def create(name: unicode, layoutClass: java.lang.Class) -> ghidra.graph.viewer.layout.JungLayoutProvider: ...

    @staticmethod
    def createLayouts() -> java.util.Set: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
