import ghidra.app.util.bin.format.macho.commands.dyld
import ghidra.util.task
import java.lang


class LazyBindState(ghidra.app.util.bin.format.macho.commands.dyld.AbstractDyldInfoState):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def perform(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def print(self) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
