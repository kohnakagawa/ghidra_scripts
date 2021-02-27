import ghidra.file.formats.ios.png
import ghidra.util.task
import java.io
import java.lang


class CrushedPNGUtil(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getUncrushedPNGBytes(self, __a0: ghidra.file.formats.ios.png.ProcessedPNG, __a1: ghidra.util.task.TaskMonitor) -> java.io.InputStream: ...

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
