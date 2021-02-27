import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class ResourceDirectoryStringU(object, ghidra.app.util.bin.StructConverter):
    """

     typedef struct _IMAGE_RESOURCE_DIR_STRING_U {
         WORD    Length;
         WCHAR   NameString[ 1 ];
     };

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'IMAGE_RESOURCE_DIR_STRING_U'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int):
        """
        Constructor.
        @param reader the binary reader
        @param index the index where this resource string begins
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int:
        """
        Returns the length of the string, in bytes.
        @return the length of the string, in bytes
        """
        ...

    def getNameString(self) -> unicode:
        """
        Returns the resource name string.
        @return the resource name string
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
    def length(self) -> int: ...

    @property
    def nameString(self) -> unicode: ...
