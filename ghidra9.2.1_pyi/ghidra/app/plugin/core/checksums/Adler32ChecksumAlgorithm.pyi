from typing import List
import ghidra.app.plugin.core.checksums
import ghidra.program.model.address
import ghidra.program.model.mem
import ghidra.util.task
import java.lang


class Adler32ChecksumAlgorithm(ghidra.app.plugin.core.checksums.ChecksumAlgorithm):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def format(__a0: List[int], __a1: bool) -> unicode: ...

    def getChecksum(self) -> List[int]: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reset(self) -> None: ...

    def supportsDecimal(self) -> bool: ...

    @staticmethod
    def toArray(__a0: long, __a1: int) -> List[int]: ...

    def toString(self) -> unicode: ...

    @overload
    def updateChecksum(self, __a0: ghidra.program.model.mem.Memory, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def updateChecksum(self, __a0: ghidra.program.model.mem.Memory, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.util.task.TaskMonitor, __a3: ghidra.app.plugin.core.checksums.ComputeChecksumsProvider) -> None: ...

    @overload
    def updateChecksum(self, __a0: ghidra.program.model.mem.Memory, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.util.task.TaskMonitor, __a3: bool, __a4: bool) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
