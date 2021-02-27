import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.importer
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class BuildVersionCommand(ghidra.app.util.bin.format.macho.commands.LoadCommand):
    """
    Represents a build_version_command structure.
    """






    class BuildToolVersion(object, ghidra.app.util.bin.StructConverter):
        ASCII: ghidra.program.model.data.DataType = char
        BYTE: ghidra.program.model.data.DataType = byte
        DWORD: ghidra.program.model.data.DataType = dword
        IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
        POINTER: ghidra.program.model.data.DataType = pointer
        QWORD: ghidra.program.model.data.DataType = qword
        STRING: ghidra.program.model.data.DataType = string
        UTF16: ghidra.program.model.data.DataType = unicode
        UTF8: ghidra.program.model.data.DataType = string-utf8
        VOID: ghidra.program.model.data.DataType = void
        WORD: ghidra.program.model.data.DataType = word



        def __init__(self, __a0: int, __a1: int): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getTool(self) -> int: ...

        def getVersion(self) -> int: ...

        def hashCode(self) -> int: ...

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
        def tool(self) -> int: ...

        @property
        def version(self) -> int: ...

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

    def getMinOS(self) -> int: ...

    def getNumTools(self) -> int: ...

    def getPlatform(self) -> int: ...

    def getSdk(self) -> int: ...

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
    def minOS(self) -> int: ...

    @property
    def numTools(self) -> int: ...

    @property
    def platform(self) -> int: ...

    @property
    def sdk(self) -> int: ...
