from typing import List
import ghidra.app.util.bin.format.macho.prelink
import ghidra.util.task
import java.lang


class PrelinkParser(object):




    def __init__(self, mainHeader: ghidra.app.util.bin.format.macho.MachHeader, provider: ghidra.app.util.bin.ByteProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.app.util.bin.format.macho.prelink.PrelinkMap]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
