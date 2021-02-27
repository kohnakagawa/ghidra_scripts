import db.util
import ghidra.program.database
import ghidra.util.task
import java.io
import java.lang


class OldFunctionManager(object, db.util.ErrorHandler):
    """
    This class only exists to support upgrading Ghidra Version 2.1 and earlier.

     NOTE: Programmers should not use this class!
    """





    def __init__(self, dbHandle: db.DBHandle, errHandler: db.util.ErrorHandler, addrMap: ghidra.program.database.map.AddressMap):
        """
        Constructs a new OldFunctionManager.
        @param dbHandle data base handle
        @param errHandler the error handler
        @param addrMap the address map
        @throws VersionException if function manager's version does not match its expected version
        """
        ...



    def dbError(self, e: java.io.IOException) -> None:
        """
        @see db.util.ErrorHandler#dbError(java.io.IOException)
        """
        ...

    def dispose(self) -> None:
        """
        Permanently discards all data resources associated with the old function manager.
         This should be invoked when an upgrade of all function data has been completed.
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def upgrade(self, upgradeProgram: ghidra.program.database.ProgramDB, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Actually does the work of upgrading the old program function manager.
        @param upgradeProgram the program to upgrade
        @param monitor the task monitor to allow the user to cancel the upgrade
        @throws CancelledException if the user cancels the upgrade
        @throws IOException if an i/o error occurs
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
