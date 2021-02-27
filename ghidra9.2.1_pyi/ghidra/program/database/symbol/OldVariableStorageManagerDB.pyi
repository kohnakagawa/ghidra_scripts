import db
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.util
import ghidra.util.task
import java.lang


class OldVariableStorageManagerDB(object, ghidra.program.database.ManagerDB):




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



    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getStorageAddress(self, variableAddr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None: ...

    @staticmethod
    def isOldVariableStorageManagerUpgradeRequired(handle: db.DBHandle) -> bool: ...

    def isUpgradeOldVariableAddressesRequired(self) -> bool: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Update storage locations to reflect register changes resulting from
         a new/updated language.  Programs address map must already be updated
         to reflect new language.
        @param translator
        @param monitor
        @throws CancelledException
        @throws IOException
        """
        ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None: ...

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
    def upgradeOldVariableAddressesRequired(self) -> bool: ...
