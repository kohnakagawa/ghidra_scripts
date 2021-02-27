import ghidra.util.task
import java.lang


class CachingLoader(object):








    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, monitor: ghidra.util.task.TaskMonitor) -> object: ...

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
