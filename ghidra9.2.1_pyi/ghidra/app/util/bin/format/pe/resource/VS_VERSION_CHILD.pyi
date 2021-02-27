from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.resource
import ghidra.program.model.data
import java.lang


class VS_VERSION_CHILD(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the VS_VERSION_CHILD data structure which generally corresponds
     to either StringFileInfo or VarFileInfo.  Only a single instance of each childName
     is expected.
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







    def equals(self, __a0: object) -> bool: ...

    def getChildName(self) -> unicode:
        """
        Returns the version child name.
        @return the version child name
        """
        ...

    def getChildSize(self) -> int:
        """
        Returns the version child size.
        @return the version child size
        """
        ...

    def getChildren(self) -> List[ghidra.app.util.bin.format.pe.resource.VS_VERSION_CHILD]:
        """
        Returns the array of children
        @return the array of children
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getNameRelativeOffset(self) -> long:
        """
        Return unicode name string offset relative to parent structure start
        @return relative name offset or 0 if data type is unknown
        """
        ...

    def getRelativeOffset(self) -> long:
        """
        Return structure offset relative to parent structure start
        @return relative offset
        """
        ...

    def getValueRelativeOffset(self) -> long:
        """
        Return value offset relative to parent structure start.
        @return relative value offset or 0 if no value exists
        """
        ...

    def hasChildren(self) -> bool:
        """
        @return true if this child has children
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    def valueIsDWord(self) -> bool:
        """
        @return true if value is 4-byte integer value in memory
         while string value return by {@link DataType#getValue(ghidra.program.model.mem.MemBuffer, ghidra.docking.settings.Settings, int) DataType.getValue(MemBuffer, Settings, int)} is a numeric hex string.
        """
        ...

    def valueIsUnicodeString(self) -> bool:
        """
        @return true if value is unicode string
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def childName(self) -> unicode: ...

    @property
    def childSize(self) -> int: ...

    @property
    def children(self) -> List[ghidra.app.util.bin.format.pe.resource.VS_VERSION_CHILD]: ...

    @property
    def nameRelativeOffset(self) -> long: ...

    @property
    def relativeOffset(self) -> long: ...

    @property
    def valueRelativeOffset(self) -> long: ...
