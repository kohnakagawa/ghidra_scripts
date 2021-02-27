import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.cli
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CliAbstractStream(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.pe.PeMarkupable):
    """
    A abstract CLI stream type for convenience.  Streams that we support should subclass
     this class and override the #parse, #markup, and #toDataType
     methods appropriately.

     When streams are laid down in memory they are referred to as heaps, but we'll just stick
     with calling them streams because using both terms can get confusing.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    PATH: unicode = u'/PE/CLI/Streams'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, header: ghidra.app.util.bin.format.pe.cli.CliStreamHeader, offset: long, rva: int, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new generic CLI stream type.  This is intended to be called by a subclass
         stream during its creation.
        @param header The stream header associated with this stream.
        @param offset The reader offset where this stream starts.
        @param rva The relative virtual address where this stream starts.
        @param reader A reader that is used to read the stream.
        @throws IOException if there is a problem reading the stream.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getStreamHeader(self) -> ghidra.app.util.bin.format.pe.cli.CliStreamHeader:
        """
        Gets this stream's header.
        @return This stream's header.
        """
        ...

    @staticmethod
    def getStreamMarkupAddress(program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader, stream: ghidra.app.util.bin.format.pe.cli.streams.CliAbstractStream, streamIndex: int) -> ghidra.program.model.address.Address:
        """
        Gets the markup address of an offset in a given stream.
        @param program
        @param isBinary
        @param monitor
        @param log
        @param ntHeader
        @param stream The stream to offset into.
        @param streamIndex The index into the stream.
        @return The markup address of the given offset in the provided stream.
        """
        ...

    def hashCode(self) -> int: ...

    def markup(self, program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None:
        """
        Does basic markup that all streams will want:
         <ul>
           <li>Set monitor message</li>
           <li>Validate addresses</li>
           <li>Add bookmark</li>
           <li>Add symbol</li>
           <li>Create data type</li>
         </ul>
         Subclass should first call this and then provide any custom markup they need.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> bool:
        """
        Parses this stream.
        @return True if parsing completed successfully; otherwise, false.
        @throws IOException If there was an IO problem while parsing.
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def streamHeader(self) -> ghidra.app.util.bin.format.pe.cli.CliStreamHeader: ...
