import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.importer
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DyldInfoCommand(ghidra.app.util.bin.format.macho.commands.LoadCommand):
    """
    Represents a dyld_info_command structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBindOffset(self) -> int:
        """
        file offset to binding info
        @return file offset to binding info
        """
        ...

    def getBindSize(self) -> int:
        """
        size of binding info
        @return size of binding info
        """
        ...

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

    def getExportOffset(self) -> int:
        """
        @return
        """
        ...

    def getExportSize(self) -> int:
        """
        @return
        """
        ...

    def getLazyBindOffset(self) -> int:
        """
        file offset to lazy binding info
        @return file offset to lazy binding info
        """
        ...

    def getLazyBindSize(self) -> int:
        """
        size of lazy binding infs
        @return
        """
        ...

    def getRebaseOffset(self) -> int:
        """
        file offset to rebase info
        @return file offset to rebase info
        """
        ...

    def getRebaseSize(self) -> int:
        """
        size of rebase info
        @return size of rebase info
        """
        ...

    def getStartIndex(self) -> long:
        """
        Returns the binary start index of this load command.
        @return the binary start index of this load command
        """
        ...

    def getWeakBindOffset(self) -> int:
        """
        file offset to weak binding info
        @return file offset to weak binding info
        """
        ...

    def getWeakBindSize(self) -> int:
        """
        size of weak binding info
        @return size of weak binding info
        """
        ...

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
    def bindOffset(self) -> int: ...

    @property
    def bindSize(self) -> int: ...

    @property
    def commandName(self) -> unicode: ...

    @property
    def exportOffset(self) -> int: ...

    @property
    def exportSize(self) -> int: ...

    @property
    def lazyBindOffset(self) -> int: ...

    @property
    def lazyBindSize(self) -> int: ...

    @property
    def rebaseOffset(self) -> int: ...

    @property
    def rebaseSize(self) -> int: ...

    @property
    def weakBindOffset(self) -> int: ...

    @property
    def weakBindSize(self) -> int: ...
