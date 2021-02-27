import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.PortableExecutable
import ghidra.program.model.data
import java.lang


class NTHeader(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.pe.OffsetValidator):
    """
    A class to represent the IMAGE_NT_HEADERS32 and
     IMAGE_NT_HEADERS64 structs as defined in
     winnt.h.

     typedef struct _IMAGE_NT_HEADERS {
        DWORD Signature;
        IMAGE_FILE_HEADER FileHeader;
        IMAGE_OPTIONAL_HEADER32 OptionalHeader;
     };

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    MAX_SANE_COUNT: int = 65536
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF_SIGNATURE: int = 4
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def checkPointer(self, ptr: long) -> bool: ...

    def checkRVA(self, rva: long) -> bool: ...

    @staticmethod
    def createNTHeader(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int, layout: ghidra.app.util.bin.format.pe.PortableExecutable.SectionLayout, advancedProcess: bool, parseCliHeaders: bool) -> ghidra.app.util.bin.format.pe.NTHeader:
        """
        Constructs a new NT header.
        @param reader the binary reader
        @param index the index into the reader to the start of the NT header
        @param advancedProcess if true, information rafside of the base header will be processed
        @param parseCliHeaders if true, CLI headers are parsed (if present)
        @throws InvalidNTHeaderException if the bytes the specified index
         do not constitute an accurate NT header.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFileHeader(self) -> ghidra.app.util.bin.format.pe.FileHeader:
        """
        Returns the file header.
        @return the file header
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name to use when converting into a structure data type.
        @return the name to use when converting into a structure data type
        """
        ...

    def getOptionalHeader(self) -> ghidra.app.util.bin.format.pe.OptionalHeader:
        """
        Returns the optional header.
        @return the optional header
        """
        ...

    def hashCode(self) -> int: ...

    def isRVAResoltionSectionAligned(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def rvaToPointer(self, rva: long) -> long:
        """
        @param rva the relative virtual address
        @return the pointer into binary image, 0 if not valid
        """
        ...

    @overload
    def rvaToPointer(self, rva: int) -> int:
        """
        Converts a relative virtual address (RVA) into a pointer.
        @see #rvaToPointer(long)
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def vaToPointer(self, va: long) -> long:
        """
        @param va the virtual address
        @return the pointer into binary image, 0 if not valid
        """
        ...

    @overload
    def vaToPointer(self, va: int) -> int:
        """
        Converts a virtual address (VA) into a pointer.
        @see #vaToPointer(long)
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def RVAResoltionSectionAligned(self) -> bool: ...

    @property
    def fileHeader(self) -> ghidra.app.util.bin.format.pe.FileHeader: ...

    @property
    def name(self) -> unicode: ...

    @property
    def optionalHeader(self) -> ghidra.app.util.bin.format.pe.OptionalHeader: ...
