import java.awt.event
import java.lang


class MouseWheelAction(object, java.awt.event.MouseWheelListener):
    """
    Invoked when the user scrolls the mouse wheel either up or down. In this case we need to
     fire off an event telling the viewport (or any other subscribers) that a scroll needs to
     happen.
    """





    def __init__(self, eventListener: ghidra.framework.main.logviewer.event.FVEventListener): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def mouseWheelMoved(self, e: java.awt.event.MouseWheelEvent) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
