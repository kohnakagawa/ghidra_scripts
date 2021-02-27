import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.cli
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CliStreamStrings(ghidra.app.util.bin.format.pe.cli.streams.CliAbstractStream):
    """
    The Strings stream contains null-terminated UTF8 strings.
     When the stream is present, the first entry is always the empty string.
     This stream may contain garbage in its unreachable parts.
    """





    def __init__(self, header: ghidra.app.util.bin.format.pe.cli.CliStreamHeader, offset: long, rva: int, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new Strings stream.
        @param header The stream header associated with this stream.
        @param offset The reader offset where this stream starts.
        @param rva The relative virtual address where this stream starts.
        @param reader A reader that is used to read the stream.
        @throws IOException if there is a problem reading the stream.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getName() -> unicode:
        """
        Gets the name of this stream.
        @return The name of this stream.
        """
        ...

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

    def getString(self, index: int) -> unicode:
        """
        Gets the string at the given index.
        @param index The index of the string to get.
        @return The string at the given index.  Could be null if the index was invalid or there was
           a problem reading the string.
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

    def parse(self) -> bool: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
