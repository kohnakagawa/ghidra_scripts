import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.cli
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CliStreamHeader(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.pe.PeMarkupable):
    """
    A structure used by a CliMetadataRoot describe a CliAbstractStream.

     Note that this type of "header" isn't found at the start of the stream, but as
     elements of a list of headers at the end of a CliMetadataRoot.  They
     are kind of like PE section headers.
    """

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



    def __init__(self, metadataRoot: ghidra.app.util.bin.format.pe.cli.CliMetadataRoot, reader: ghidra.app.util.bin.BinaryReader):
        """
        Constructs a new CLI Stream Header datatype.
        @param metadataRoot the metadata root.
        @param reader A binary reader set to start reading at the start of this header.
        @throws IOException if there is a problem reading the header.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMetadataRoot(self) -> ghidra.app.util.bin.format.pe.cli.CliMetadataRoot:
        """
        Gets the {@link CliMetadataRoot} that contains us.
        @return The {@link CliMetadataRoot} that contains us.
        """
        ...

    def getName(self) -> unicode:
        """
        Gets the name of this header's stream.
        @return The name of this header's stream.
        """
        ...

    def getNameLength(self) -> int:
        """
        Gets the name length.
         <p>
         The name length may be larger than necessary because the name string is must
         be aligned to the next 4-byte boundary.
        @return The name length.
        """
        ...

    def getOffset(self) -> int:
        """
        Gets the offset.  This is not a file offset, but an offset that gets added to
         the metadata header's offset to obtain a file offset.
        @return The offset.
        """
        ...

    def getSize(self) -> int:
        """
        Gets the size of this header's stream.
        @return The size of this header's stream.
        """
        ...

    def getStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliAbstractStream:
        """
        Gets the {@link CliAbstractStream} that this is a header for.
        @return The {@link CliAbstractStream} that this is a header for.  Could be null if we
           don't support the stream type.
        """
        ...

    def hashCode(self) -> int: ...

    def markup(self, program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None: ...

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
    def metadataRoot(self) -> ghidra.app.util.bin.format.pe.cli.CliMetadataRoot: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nameLength(self) -> int: ...

    @property
    def offset(self) -> int: ...

    @property
    def size(self) -> int: ...

    @property
    def stream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliAbstractStream: ...
