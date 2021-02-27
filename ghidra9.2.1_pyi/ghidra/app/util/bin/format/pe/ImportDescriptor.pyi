from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.program.model.data
import ghidra.util
import java.lang


class ImportDescriptor(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.ByteArrayConverter):
    """

     typedef struct _IMAGE_IMPORT_DESCRIPTOR {
         union {
             DWORD   Characteristics;            // 0 for terminating null import descriptor
             DWORD   OriginalFirstThunk;         // RVA to original unbound IAT (PIMAGE_THUNK_DATA)
         };
         DWORD   TimeDateStamp;
         DWORD   ForwarderChain;                 // -1 if no forwarders
         DWORD   Name;
         DWORD   FirstThunk;                     // RVA to IAT (if bound this IAT has actual addresses)
     }

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'IMAGE_IMPORT_DESCRIPTOR'
    NOT_BOUND: int = 0
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 20
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        Constructs a new import descriptor initialized to zero.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getCharacteristics(self) -> int:
        """
        At one time, this may have been a set of flags.
         However, Microsoft changed its meaning and
         never bothered to update WINNT.H.
         This field is really an offset (an RVA) to an
         array of pointers. Each of these pointers points
         to an IMAGE_IMPORT_BY_NAME structure.
        @return an offset (an RVA) to an array of pointers
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDLL(self) -> unicode: ...

    def getFirstThunk(self) -> int:
        """
        This field is an offset (an RVA) to an
         IMAGE_THUNK_DATA union. In almost every case,
         the union is interpreted as a pointer to an
         IMAGE_IMPORT_BY_NAME structure. If the field
         isn't one of these pointers, then it's supposedly
         treated as an export ordinal value for the DLL
         that's being imported. It's not clear from the
         documentation if you really can import a function
         by ordinal rather than by name.
        @return an offset (an RVA) to an IMAGE_THUNK_DATA union
        """
        ...

    def getForwarderChain(self) -> int:
        """
        This field relates to forwarding.
         Forwarding involves one DLL sending on
         references to one of its functions to
         another DLL. For example, in Windows NT,
         NTDLL.DLL appears to forward some of its
         exported functions to KERNEL32.DLL. An
         application may think it's calling a function
         in NTDLL.DLL, but it actually ends up calling
         into KERNEL32.DLL. This field contains an index
         into FirstThunk array (described momentarily).
         The function indexed by this field will be
         forwarded to another DLL. Unfortunately, the
         format of how a function is forwarded isn't
         documented, and examples of forwarded functions
         are hard to find.
        @return the forwarder chain
        """
        ...

    def getImportAddressTableThunkData(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]:
        """
        Returns the array of thunks from the import address table.
        @return the array of thunks from the import address table
        """
        ...

    def getImportNameTableThunkData(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]:
        """
        Returns the array of thunks from the import name table.
        @return the array of thunks from the import name table
        """
        ...

    def getName(self) -> int:
        """
        Returns an RVA to a NULL-terminated
         ASCII string containing the imported
         DLL's name. Common examples are
         "KERNEL32.DLL" and "USER32.DLL".
        @return an RVA to a NULL-terminated ASCII string
        """
        ...

    def getOriginalFirstThunk(self) -> int:
        """
        At one time, this may have been a set of flags.
         However, Microsoft changed its meaning and
         never bothered to update WINNT.H.
         This field is really an offset (an RVA) to an
         array of pointers. Each of these pointers points
         to an IMAGE_IMPORT_BY_NAME structure.
        @return an offset (an RVA) to an array of pointers
        """
        ...

    def getTimeDateStamp(self) -> int:
        """
        Returns the time/date stamp indicating when the file was built.
        @return the time/date stamp indicating when the file was built
        """
        ...

    def hashCode(self) -> int: ...

    def isBound(self) -> bool:
        """
        Returns true if the import descriptor is bound to an imported library.
         Being bound implies that the import has the function's preferred address
        @return true if the import descriptor is bound
        """
        ...

    def isNullEntry(self) -> bool:
        """
        Checks to see if this descriptor is a null entry.  A null entry
         indicates that no more descriptors follow in the import table.
        @return True if this descriptor is a null entry; otherwise, false.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setFirstThunk(self, i: int) -> None:
        """
        Sets the first thunk to the specifed value.
        @param i the new first thunk value.
        @see #getFirstThunk()
        """
        ...

    def setForwarderChain(self, i: int) -> None:
        """
        Sets the forwarder to the specifed value.
        @param i the new forwarder value.
        @see #getForwarderChain()
        """
        ...

    def setName(self, i: int) -> None:
        """
        Sets the name to the specifed value.
        @param i the new name value.
        @see #getName()
        """
        ...

    def setOriginalFirstThunk(self, i: int) -> None:
        """
        Sets the original first thunk to the specifed value.
        @param i the new original first thunk value.
        @see #getOriginalFirstThunk()
        """
        ...

    def setTimeDateStamp(self, i: int) -> None:
        """
        Sets the time/date stamp to the specifed value.
        @param i the new time/date stamp value.
        @see #getTimeDateStamp()
        """
        ...

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
    def DLL(self) -> unicode: ...

    @property
    def bound(self) -> bool: ...

    @property
    def characteristics(self) -> int: ...

    @property
    def firstThunk(self) -> int: ...

    @firstThunk.setter
    def firstThunk(self, value: int) -> None: ...

    @property
    def forwarderChain(self) -> int: ...

    @forwarderChain.setter
    def forwarderChain(self, value: int) -> None: ...

    @property
    def importAddressTableThunkData(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]: ...

    @property
    def importNameTableThunkData(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]: ...

    @property
    def name(self) -> int: ...

    @name.setter
    def name(self, value: int) -> None: ...

    @property
    def nullEntry(self) -> bool: ...

    @property
    def originalFirstThunk(self) -> int: ...

    @originalFirstThunk.setter
    def originalFirstThunk(self, value: int) -> None: ...

    @property
    def timeDateStamp(self) -> int: ...

    @timeDateStamp.setter
    def timeDateStamp(self, value: int) -> None: ...
