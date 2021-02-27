import ghidra.app.util.importer
import ghidra.program.model.listing
import ghidra.util.classfinder
import ghidra.util.task
import java.lang


class BinaryAnalysisCommand(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL BinaryAnalysisCommand CLASSES MUST END IN "BinaryAnalysisCommand".  If not,
     the ClassSearcher will not find them.
    """









    def applyTo(self, program: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Applies the command to the given domain object.
        @param program domain object that this command is to be applied.
        @param monitor the task monitor
        @return true if the command applied successfully
        """
        ...

    def canApply(self, program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns TRUE if this command can be applied
         to the given domain object.
        @param program the domain object to inspect.
        @return TRUE if this command can be applied
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMessages(self) -> ghidra.app.util.importer.MessageLog:
        """
        Returns the status message indicating the status of the command.
        @return reason for failure, or null if the status of the command
                 was successful
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this command.
        @return the name of this command
        """
        ...

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

    @property
    def messages(self) -> ghidra.app.util.importer.MessageLog: ...

    @property
    def name(self) -> unicode: ...
