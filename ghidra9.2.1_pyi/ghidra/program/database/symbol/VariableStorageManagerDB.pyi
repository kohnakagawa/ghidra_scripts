import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.task
import java.lang


class VariableStorageManagerDB(object):




    def __init__(self, handle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new variable manager.
        @param handle the database handle.
        @param addrMap the address map
        @param openMode the open mode
        @param lock the program synchronization lock
        @param monitor the task monitor.
        @throws IOException if a database error occurs.
        @throws VersionException if the table version is different from this adapter.
        @throws IOException
        @throws CancelledException if the user cancels the upgrade.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getVariableStorageAddress(self, storage: ghidra.program.model.listing.VariableStorage, create: bool) -> ghidra.program.model.address.Address: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform language translation.
         Update variable storage specifications to reflect address space and register mappings
        @param translator
        @param monitor
        @throws CancelledException
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
