from typing import List
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.importer
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class SegmentCommand(ghidra.app.util.bin.format.macho.commands.LoadCommand):
    """
    Represents a segment_command and segment_command_64 structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createSegmentCommand(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, is32bit: bool) -> ghidra.app.util.bin.format.macho.commands.SegmentCommand: ...

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

    def getFileOffset(self) -> long: ...

    def getFileSize(self) -> long: ...

    def getFlags(self) -> int: ...

    def getInitProtection(self) -> int:
        """
        Returns a octal model value reflecting the
         segment's initial protection value.
         For example:{@code
         7 -> 0x111 -> rwx
         5 -> 0x101 -> rx}
        @return the initial protections of a segment
        """
        ...

    def getMaxProtection(self) -> int:
        """
        Returns a octal model value reflecting the
         segment's maximum protection value allowed.
         For example:{@code
         7 -> 0x111 -> rwx
         5 -> 0x101 -> rx}
        @return the maximum protections of a segment
        """
        ...

    def getNumberOfSections(self) -> int: ...

    def getSectionByName(self, sectionName: unicode) -> ghidra.app.util.bin.format.macho.Section: ...

    def getSectionContaining(self, address: ghidra.program.model.address.Address) -> ghidra.app.util.bin.format.macho.Section: ...

    def getSections(self) -> List[ghidra.app.util.bin.format.macho.Section]: ...

    def getSegmentName(self) -> unicode: ...

    def getStartIndex(self) -> long:
        """
        Returns the binary start index of this load command.
        @return the binary start index of this load command
        """
        ...

    def getVMaddress(self) -> long: ...

    def getVMsize(self) -> long: ...

    def hashCode(self) -> int: ...

    def isAppleProtected(self) -> bool: ...

    def isExecute(self) -> bool:
        """
        Returns true if the initial protections include EXECUTE.
        @return true if the initial protections include EXECUTE
        """
        ...

    def isRead(self) -> bool:
        """
        Returns true if the initial protections include READ.
        @return true if the initial protections include READ
        """
        ...

    def isWrite(self) -> bool:
        """
        Returns true if the initial protections include WRITE.
        @return true if the initial protections include WRITE
        """
        ...

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
    def VMaddress(self) -> long: ...

    @property
    def VMsize(self) -> long: ...

    @property
    def appleProtected(self) -> bool: ...

    @property
    def commandName(self) -> unicode: ...

    @property
    def execute(self) -> bool: ...

    @property
    def fileOffset(self) -> long: ...

    @property
    def fileSize(self) -> long: ...

    @property
    def flags(self) -> int: ...

    @property
    def initProtection(self) -> int: ...

    @property
    def maxProtection(self) -> int: ...

    @property
    def numberOfSections(self) -> int: ...

    @property
    def read(self) -> bool: ...

    @property
    def sections(self) -> List[object]: ...

    @property
    def segmentName(self) -> unicode: ...

    @property
    def write(self) -> bool: ...
