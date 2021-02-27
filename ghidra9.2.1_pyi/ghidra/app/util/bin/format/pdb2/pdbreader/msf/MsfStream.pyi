from typing import List
import ghidra.util.task
import java.lang


class MsfStream(object):
    MAX_STREAM_LENGTH: int = 2147483647







    def dump(self, __a0: int) -> unicode: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def read(self, __a0: int, __a1: int, __a2: ghidra.util.task.TaskMonitor) -> List[int]: ...

    @overload
    def read(self, __a0: int, __a1: List[int], __a2: int, __a3: int, __a4: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def length(self) -> int: ...
