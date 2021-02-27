from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.program.model.data
import ghidra.util
import java.lang


class BoundImportDescriptor(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.ByteArrayConverter):
    """
    A class to represent the
     IMAGE_BOUND_IMPORT_DESCRIPTOR
     data structure defined in winnt.h.


     typedef struct _IMAGE_BOUND_IMPORT_DESCRIPTOR {
         DWORD   TimeDateStamp;
         WORD    OffsetModuleName;
         WORD    NumberOfModuleForwarderRefs;
         // Array of zero or more IMAGE_BOUND_FORWARDER_REF follows
     } IMAGE_BOUND_IMPORT_DESCRIPTOR,  *PIMAGE_BOUND_IMPORT_DESCRIPTOR;

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_SIZEOF_BOUND_IMPORT_DESCRIPTOR: int = 8
    NAME: unicode = u'IMAGE_BOUND_IMPORT_DESCRIPTOR'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    @overload
    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...

    @overload
    def __init__(self, name: unicode, timeDateStamp: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getBoundImportForwarderRef(self, index: int) -> ghidra.app.util.bin.format.pe.BoundImportForwarderRef:
        """
        Returns the forwarder ref at the specified index
        @param index the index of the forwarder ref
        @return the forwarder ref at the specified index
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getModuleName(self) -> unicode:
        """
        Returns the module name of the imported DLL.
        @return the module name of the imported DLL
        """
        ...

    def getNumberOfModuleForwarderRefs(self) -> int:
        """
        Returns the number of IMAGE_BOUND_FORWARDER_REF
         structures that immediately follow this structure.
        @return the number of IMAGE_BOUND_FORWARDER_REF structures that immediately follow this structure
        """
        ...

    def getOffsetModuleName(self) -> int:
        """
        Returns an offset to a string with the name of the imported DLL.
        @return an offset to a string with the name
        """
        ...

    def getTimeDateStamp(self) -> int:
        """
        Returns the time/data stamp of the imported DLL.
        @return the time/data stamp of the imported DLL
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

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def moduleName(self) -> unicode: ...

    @property
    def numberOfModuleForwarderRefs(self) -> int: ...

    @property
    def offsetModuleName(self) -> int: ...

    @property
    def timeDateStamp(self) -> int: ...
