import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.bin.format.macho.threadcommand
import ghidra.app.util.importer
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ThreadCommand(ghidra.app.util.bin.format.macho.commands.LoadCommand):
    """
    Represents a thread_command structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createThreadCommand(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, header: ghidra.app.util.bin.format.macho.MachHeader) -> ghidra.app.util.bin.format.macho.threadcommand.ThreadCommand: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCommandName(self) -> unicode: ...

    def getCommandSize(self) -> int:
        """
        Total size of command in bytes
        @return total size of command in bytes
        """
        ...

    def getCommandType(self) -> int:
        """
        Type of load command
        @return type of load command
        """
        ...

    def getInitialInstructionPointer(self) -> long: ...

    def getStartIndex(self) -> long:
        """
        Returns the binary start index of this load command.
        @return the binary start index of this load command
        """
        ...

    def getThreadState(self) -> ghidra.app.util.bin.format.macho.threadcommand.ThreadState: ...

    def getThreadStateHeader(self) -> ghidra.app.util.bin.format.macho.threadcommand.ThreadStateHeader: ...

    def hashCode(self) -> int: ...

    def markup(self, header: ghidra.app.util.bin.format.macho.MachHeader, api: ghidra.program.flatapi.FlatProgramAPI, baseAddress: ghidra.program.model.address.Address, isBinary: bool, parentModule: ghidra.program.model.listing.ProgramModule, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def commandName(self) -> unicode: ...

    @property
    def initialInstructionPointer(self) -> long: ...

    @property
    def threadState(self) -> ghidra.app.util.bin.format.macho.threadcommand.ThreadState: ...

    @property
    def threadStateHeader(self) -> ghidra.app.util.bin.format.macho.threadcommand.ThreadStateHeader: ...
