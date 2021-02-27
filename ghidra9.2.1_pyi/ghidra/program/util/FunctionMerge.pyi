import ghidra.program.model.address
import ghidra.program.util
import ghidra.util.task
import java.lang


class FunctionMerge(object):




    def __init__(self, originToResultTranslator: ghidra.program.util.AddressTranslator): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def replaceFunctionsNames(self, originAddressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    @staticmethod
    def replaceFunctionsNames(pgmMerge: ghidra.program.util.ProgramMerge, addressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
