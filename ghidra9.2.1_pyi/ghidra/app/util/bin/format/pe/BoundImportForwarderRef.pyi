from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import ghidra.util
import java.lang


class BoundImportForwarderRef(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.ByteArrayConverter):
    """
    A class to represent the
     IMAGE_BOUND_FORWARDER_REF
     data structure defined in winnt.h.


     typedef struct _IMAGE_BOUND_FORWARDER_REF {
         DWORD   TimeDateStamp;
         WORD    OffsetModuleName;
         WORD    Reserved;
     } IMAGE_BOUND_FORWARDER_REF, *PIMAGE_BOUND_FORWARDER_REF;

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_SIZEOF_BOUND_IMPORT_FORWARDER_REF: int = 8
    NAME: unicode = u'IMAGE_BOUND_FORWARDER_REF'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
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



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getModuleName(self) -> unicode:
        """
        Returns the imported module name.
        @return the imported module name
        """
        ...

    def getOffsetModuleName(self) -> int:
        """
        Returns the offset, relative the beginning of the Bound Import Table,
         to the import name.
        @return the offset to the import name
        """
        ...

    def getReserved(self) -> int:
        """
        Returns the reserved word (use unknown).
        @return the reserved word
        """
        ...

    def getTimeDateStamp(self) -> int:
        """
        Returns the time stamp.
        @return the time stamp
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]:
        """
        @see ghidra.app.util.bin.ByteArrayConverter#toBytes(ghidra.util.DataConverter)
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def moduleName(self) -> unicode: ...

    @property
    def offsetModuleName(self) -> int: ...

    @property
    def reserved(self) -> int: ...

    @property
    def timeDateStamp(self) -> int: ...
