import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class VTFunctionSizeUtil(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def minimumSizeFunctionFilter(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressSetView, __a2: int, __a3: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
