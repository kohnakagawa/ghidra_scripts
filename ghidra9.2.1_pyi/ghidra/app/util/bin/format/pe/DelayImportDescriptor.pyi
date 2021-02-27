from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.program.model.data
import java.lang
import java.util


class DelayImportDescriptor(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the
     ImgDelayDescr
     data structure defined in DELAYIMP.H.


     typedef struct ImgDelayDescr {
         DWORD           grAttrs;        // attributes
         LPCSTR          szName;         // pointer to dll name
         HMODULE *       phmod;          // address of module handle
         PImgThunkData   pIAT;           // address of the IAT
         PCImgThunkData  pINT;           // address of the INT
         PCImgThunkData  pBoundIAT;      // address of the optional bound IAT
         PCImgThunkData  pUnloadIAT;     // address of optional copy of original IAT
         DWORD           dwTimeStamp;    // 0 if not bound,
                                         // O.W. date/time stamp of DLL bound to (old BIND)
     } ImgDelayDescr, * PImgDelayDescr;

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'ImgDelayDescr'
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

    def getAddressOfBoundIAT(self) -> long:
        """
        Returns the address of the optional bound IAT.
        @return the address of the optional bound IAT
        """
        ...

    def getAddressOfIAT(self) -> long:
        """
        Returns the address of the import address table.
        @return the address of the import address table
        """
        ...

    def getAddressOfINT(self) -> long:
        """
        Returns the address of the import name table.
        @return the address of the import name table
        """
        ...

    def getAddressOfModuleHandle(self) -> long:
        """
        Returns the address of the module handle.
        @return the address of the module handle
        """
        ...

    def getAddressOfOriginalIAT(self) -> long:
        """
        Returns the address of the optional copy of original IAT.
        @return the address of the optional copy of original IAT
        """
        ...

    def getAttibutes(self) -> int:
        """
        Returns the attributes.
        @return the attributes
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDLLName(self) -> unicode:
        """
        Returns the DLL name.
        @return the DLL name
        """
        ...

    def getImportByNameMap(self) -> java.util.Map: ...

    def getImportList(self) -> List[ghidra.app.util.bin.format.pe.DelayImportInfo]: ...

    def getPointerToDLLName(self) -> long:
        """
        Returns the pointer to the DLL name.
        @return the pointer to the DLL name
        """
        ...

    def getThunksBoundIAT(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]: ...

    def getThunksIAT(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]: ...

    def getThunksINT(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]: ...

    def getThunksUnloadIAT(self) -> List[ghidra.app.util.bin.format.pe.ThunkData]: ...

    def getTimeStamp(self) -> int:
        """
        Returns the date/time stamp of DLL bound to (Old BIND),
         otherwise 0 if not bound.
        @return if bound returns the time stamp, otherwise 0
        """
        ...

    def hashCode(self) -> int: ...

    def isUsingRVA(self) -> bool:
        """
        Returns true if the "using relative virtual address" is flag is set
        @return true if the "using relative virtual address" is flag is set
        """
        ...

    def isValid(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sizeof(self) -> int:
        """
        Returns the size of this structure. It accounts for 32 vs 64 bit.
        @return the size of this structure
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def DLLName(self) -> unicode: ...

    @property
    def addressOfBoundIAT(self) -> long: ...

    @property
    def addressOfIAT(self) -> long: ...

    @property
    def addressOfINT(self) -> long: ...

    @property
    def addressOfModuleHandle(self) -> long: ...

    @property
    def addressOfOriginalIAT(self) -> long: ...

    @property
    def attibutes(self) -> int: ...

    @property
    def importByNameMap(self) -> java.util.Map: ...

    @property
    def importList(self) -> List[object]: ...

    @property
    def pointerToDLLName(self) -> long: ...

    @property
    def thunksBoundIAT(self) -> List[object]: ...

    @property
    def thunksIAT(self) -> List[object]: ...

    @property
    def thunksINT(self) -> List[object]: ...

    @property
    def thunksUnloadIAT(self) -> List[object]: ...

    @property
    def timeStamp(self) -> int: ...

    @property
    def usingRVA(self) -> bool: ...

    @property
    def valid(self) -> bool: ...
