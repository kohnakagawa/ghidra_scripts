import db
import ghidra.feature.vt.api.db
import ghidra.util.task
import java.lang


class VTAddressCorrelationAdapterV0(ghidra.feature.vt.api.db.VTAddressCorrelatorAdapter):




    @overload
    def __init__(self, __a0: db.DBHandle): ...

    @overload
    def __init__(self, __a0: db.DBHandle, __a1: ghidra.util.task.TaskMonitor): ...



    @staticmethod
    def createAdapter(__a0: db.DBHandle) -> ghidra.feature.vt.api.db.VTAddressCorrelatorAdapter: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAdapter(__a0: db.DBHandle, __a1: ghidra.util.task.TaskMonitor) -> ghidra.feature.vt.api.db.VTAddressCorrelatorAdapter: ...

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
