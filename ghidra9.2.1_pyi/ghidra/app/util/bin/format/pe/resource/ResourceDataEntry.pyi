import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class ResourceDataEntry(object, ghidra.app.util.bin.StructConverter):
    """

     typedef struct _IMAGE_RESOURCE_DATA_ENTRY {
         DWORD   OffsetToData;
         DWORD   Size;
         DWORD   CodePage;
         DWORD   Reserved;
     };

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'IMAGE_RESOURCE_DATA_ENTRY'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 16
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int):
        """
        Constructor.
        @param reader the binary reader
        @param index the index where this entry begins
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodePage(self) -> int:
        """
        @return a CodePage that should be used when decoding the resource data
        """
        ...

    def getOffsetToData(self) -> int:
        """
        Returns the offset, relative to the beginning of the resource
         directory of the data for the resource.
        @return the offset, relative to the beginning of the resource directory
        """
        ...

    def getReserved(self) -> int:
        """
        Reserved, use unknown.
        @return reserved, use unknown
        """
        ...

    def getSize(self) -> int:
        """
        Returns a size field that gives the number of bytes of data at that offset.
        @return a size field that gives the number of bytes of data at that offset,
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

    @property
    def codePage(self) -> int: ...

    @property
    def offsetToData(self) -> int: ...

    @property
    def reserved(self) -> int: ...

    @property
    def size(self) -> int: ...
