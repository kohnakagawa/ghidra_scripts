import ghidra.app.plugin.core.function
import java.lang
import java.util


class StackDepthChangeListener(java.util.EventListener, object):








    def actionPerformed(self, __a0: ghidra.app.plugin.core.function.StackDepthChangeEvent) -> None: ...

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
