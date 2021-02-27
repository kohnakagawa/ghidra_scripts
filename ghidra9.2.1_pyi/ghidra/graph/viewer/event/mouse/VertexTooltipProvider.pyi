import java.awt.event
import java.lang
import javax.swing


class VertexTooltipProvider(object):
    """
    Creates tooltips for a given vertex.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getTooltip(self, __a0: object) -> javax.swing.JComponent: ...

    @overload
    def getTooltip(self, __a0: object, __a1: object) -> javax.swing.JComponent: ...

    def getTooltipText(self, __a0: object, __a1: java.awt.event.MouseEvent) -> unicode: ...

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
