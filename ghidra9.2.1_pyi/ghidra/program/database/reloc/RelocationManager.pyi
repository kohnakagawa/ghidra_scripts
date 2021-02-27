from typing import Iterator
from typing import List
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.reloc
import ghidra.util.task
import java.lang


class RelocationManager(object, ghidra.program.model.reloc.RelocationTable, ghidra.program.database.ManagerDB):
    """
    An implementation of the relocation table interface.
    """

    RELOCATABLE_PROP_NAME: unicode = u'Relocatable'



    def __init__(self, handle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructs a new relocation manager.
        @param handle the database handle
        @param addrMap the address map
        @param openMode the open mode; CREATE, UPDATE, READONLY, UPGRADE
        @param lock the program synchronization lock
        @param monitor the task monitor
        @throws VersionException
        @throws IOException
        """
        ...



    def add(self, addr: ghidra.program.model.address.Address, type: int, values: List[long], bytes: List[int], symbolName: unicode) -> ghidra.program.model.reloc.Relocation: ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRelocation(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.reloc.Relocation: ...

    def getRelocationAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.reloc.Relocation: ...

    @overload
    def getRelocations(self) -> Iterator[ghidra.program.model.reloc.Relocation]: ...

    @overload
    def getRelocations(self, set: ghidra.program.model.address.AddressSetView) -> Iterator[ghidra.program.model.reloc.Relocation]: ...

    def getSize(self) -> int: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None: ...

    def isRelocatable(self) -> bool: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def remove(self, reloc: ghidra.program.model.reloc.Relocation) -> None: ...

    def setProgram(self, p: ghidra.program.database.ProgramDB) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...

    @property
    def relocatable(self) -> bool: ...

    @property
    def relocations(self) -> java.util.Iterator: ...

    @property
    def size(self) -> int: ...
