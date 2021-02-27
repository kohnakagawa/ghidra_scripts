from typing import List
import db
import ghidra.feature.vt.api.db
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.io
import java.lang


class AddressCorrelatorDB(object):








    def addAddressCorrelation(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.address.Address) -> None: ...

    def close(self) -> None: ...

    @staticmethod
    def createAddressCorrelator(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.listing.Program) -> ghidra.feature.vt.api.db.AddressCorrelatorDB: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressCorrelations(self, __a0: ghidra.program.model.address.Address) -> List[object]: ...

    @staticmethod
    def getAddressCorrelator(__a0: db.DBHandle, __a1: ghidra.program.model.listing.Program, __a2: ghidra.program.model.listing.Program, __a3: ghidra.util.task.TaskMonitor) -> ghidra.feature.vt.api.db.AddressCorrelatorDB: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def save(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def saveAs(self, __a0: java.io.File, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
