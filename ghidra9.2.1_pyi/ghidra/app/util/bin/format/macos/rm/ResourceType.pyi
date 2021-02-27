from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macos.rm
import ghidra.program.model.data
import java.lang


class ResourceType(object, ghidra.app.util.bin.StructConverter):
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







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNumberOfResources(self) -> int:
        """
        Returns the number of resources of this type
         in map minus 1.
        @return the number of resources
        """
        ...

    def getOffsetToReferenceList(self) -> int:
        """
        Returns the offset from the beginning of the
         resource type list to reference list for this type.
        @return the offset to reference list
        """
        ...

    def getReferenceList(self) -> List[ghidra.app.util.bin.format.macos.rm.ReferenceListEntry]: ...

    def getResourceObject(self) -> object: ...

    def getType(self) -> int:
        """
        Returns the resource type.
        @return the resource type
        """
        ...

    def getTypeAsString(self) -> unicode: ...

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
    def numberOfResources(self) -> int: ...

    @property
    def offsetToReferenceList(self) -> int: ...

    @property
    def referenceList(self) -> List[object]: ...

    @property
    def resourceObject(self) -> object: ...

    @property
    def type(self) -> int: ...

    @property
    def typeAsString(self) -> unicode: ...
