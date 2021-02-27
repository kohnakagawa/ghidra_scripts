import ghidra.program.database
import ghidra.program.model.address
import ghidra.util.task
import java.lang


class ManagerDB(object):
    """
    Interface that all subsection managers of a program must implement.
    """









    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Delete all objects which have been applied to the address range startAddr to endAddr
         and update the database accordingly.
        @param startAddr the first address in the range.
        @param endAddr the last address in the range.
        @param monitor the task monitor to use in any upgrade operations.
        @throws CancelledException if the user cancelled the operation via the task monitor.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None:
        """
        Clears all data caches.
        @param all if false, some managers may not need to update their cache if they can
         tell that its not necessary.  If this flag is true, then all managers should clear
         their cache no matter what.
        @throws IOException if a database io error occurs.
        """
        ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move all objects within an address range to a new location.
        @param fromAddr the first address of the range to be moved.
        @param toAddr the address where to the range is to be moved.
        @param length the number of addresses to move.
        @param monitor the task monitor to use in any upgrade operations.
        @throws CancelledException if the user cancelled the operation via the task monitor.
        @throws AddressOverflowException if the length is such that a address wrap occurs
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Callback from program made to each manager after the program has completed initialization.
         This method may be used by managers to perform additional upgrading which may have been deferred.
        @param openMode the mode that the program is being opened.
        @param currentRevision current program revision.  If openMode is UPGRADE, this value reflects
         the pre-upgrade value.
        @param monitor the task monitor to use in any upgrade operations.
        @throws IOException if a database io error occurs.
        @throws CancelledException if the user cancelled the operation via the task monitor.
        """
        ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None:
        """
        Callback from program used to indicate all manager have been created.
         When this method is invoked, all managers have been instantiated but may not be fully initialized.
        @param program the program is set when all the initializations have been completed.
        """
        ...

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
