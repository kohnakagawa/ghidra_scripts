import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.importer
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class RoutinesCommand(ghidra.app.util.bin.format.macho.commands.LoadCommand):
    """
    Represents a routines_command and routines_command_64 structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



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

    def getInitializationRoutineAddress(self) -> long:
        """
        Address of initialization routine.
        @return address of initialization routine
        """
        ...

    def getInitializationRoutineModuleIndex(self) -> long:
        """
        Index into the module table that the init routine is defined in.
        @return index into the module table that the init routine is defined in
        """
        ...

    def getReserved1(self) -> long: ...

    def getReserved2(self) -> long: ...

    def getReserved3(self) -> long: ...

    def getReserved4(self) -> long: ...

    def getReserved5(self) -> long: ...

    def getReserved6(self) -> long: ...

    def getStartIndex(self) -> long:
        """
        Returns the binary start index of this load command.
        @return the binary start index of this load command
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
    def commandName(self) -> unicode: ...

    @property
    def initializationRoutineAddress(self) -> long: ...

    @property
    def initializationRoutineModuleIndex(self) -> long: ...

    @property
    def reserved1(self) -> long: ...

    @property
    def reserved2(self) -> long: ...

    @property
    def reserved3(self) -> long: ...

    @property
    def reserved4(self) -> long: ...

    @property
    def reserved5(self) -> long: ...

    @property
    def reserved6(self) -> long: ...
