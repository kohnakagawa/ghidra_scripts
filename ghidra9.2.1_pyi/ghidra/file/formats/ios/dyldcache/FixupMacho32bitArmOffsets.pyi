import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import ghidra.util.task
import java.io
import java.lang


class FixupMacho32bitArmOffsets(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def fix(self, __a0: ghidra.formats.gfilesystem.GFile, __a1: long, __a2: ghidra.app.util.bin.ByteProvider, __a3: ghidra.util.task.TaskMonitor) -> java.io.InputStream: ...

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
