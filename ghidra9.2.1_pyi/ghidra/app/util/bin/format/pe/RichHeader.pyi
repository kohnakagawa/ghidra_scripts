from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.rich
import ghidra.program.model.data
import ghidra.util
import java.io
import java.lang


class RichHeader(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.Writeable):
    """
    The "Rich" header contains encoded metadata about the tool chain used to generate the binary.
     This class decodes and writes the Rich header (if it exists).
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_DANS_SIGNATURE: int = 1399742788
    IMAGE_RICH_SIGNATURE: int = 1751345490
    NAME: unicode = u'IMAGE_RICH_HEADER'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        Do not directly call this constructor.
         <p>
         Use {@link #createRichHeader(FactoryBundledWithBinaryReader)}
        """
        ...



    @staticmethod
    def createRichHeader(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader) -> ghidra.app.util.bin.format.pe.RichHeader:
        """
        Create and returns the Rich header found from the given reader.  The reader should be
         positioned directly after the DOS header.
        @param reader The reader to read the PE with.
        @return The Rich header associated with the given reader.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMask(self) -> int:
        """
        Gets the Rich header mask.
        @return the Rich header mask, or -1 if a Rich header was not found.
        """
        ...

    def getOffset(self) -> int:
        """
        Gets the offset of the Rich header.
        @return the offset of the Rich header, or -1 if a Rich header was not found.
        """
        ...

    def getRecords(self) -> List[ghidra.app.util.bin.format.pe.rich.RichHeaderRecord]:
        """
        Gets the Rich header records.
        @return the Rich header records.  Could be empty if a Rich header was not found.
        """
        ...

    def getSize(self) -> int:
        """
        Gets the size of the Rich header.
        @return the size of the Rich header.  Will be 0 if a Rich header was not found.
        """
        ...

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

    def write(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None: ...

    @property
    def mask(self) -> int: ...

    @property
    def offset(self) -> int: ...

    @property
    def records(self) -> List[ghidra.app.util.bin.format.pe.rich.RichHeaderRecord]: ...

    @property
    def size(self) -> int: ...
