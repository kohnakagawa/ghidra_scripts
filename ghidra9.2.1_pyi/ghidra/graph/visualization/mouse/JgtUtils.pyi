import java.awt.event
import java.lang
import org.jungrapht.visualization


class JgtUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getEdge(__a0: java.awt.event.MouseEvent, __a1: org.jungrapht.visualization.VisualizationViewer) -> object: ...

    @staticmethod
    def getVertex(__a0: java.awt.event.MouseEvent, __a1: org.jungrapht.visualization.VisualizationViewer) -> object: ...

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
