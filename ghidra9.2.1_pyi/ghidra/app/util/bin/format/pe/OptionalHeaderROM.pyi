from typing import List
import java.lang


class OptionalHeaderROM(object):
    """
    A class to represent the IMAGE_ROM_OPTIONAL_HEADER
     data structure.


     typedef struct _IMAGE_ROM_OPTIONAL_HEADER {
         WORD   Magic;
         BYTE   MajorLinkerVersion;
         BYTE   MinorLinkerVersion;
         DWORD  SizeOfCode;
         DWORD  SizeOfInitializedData;
         DWORD  SizeOfUninitializedData;
         DWORD  AddressOfEntryPoint;
         DWORD  BaseOfCode;
         DWORD  BaseOfData;
         DWORD  BaseOfBss;
         DWORD  GprMask;
         DWORD  CprMask[4];
         DWORD  GpValue;
     } IMAGE_ROM_OPTIONAL_HEADER, *PIMAGE_ROM_OPTIONAL_HEADER;

    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getAddressOfEntryPoint(self) -> int: ...

    def getBaseOfBss(self) -> int: ...

    def getBaseOfCode(self) -> int: ...

    def getBaseOfData(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getCprMask(self) -> List[int]: ...

    def getGpValue(self) -> int: ...

    def getGprMask(self) -> int: ...

    def getMagic(self) -> int: ...

    def getMajorLinkerVersion(self) -> int: ...

    def getMinorLinkerVersion(self) -> int: ...

    def getSizeOfCode(self) -> int: ...

    def getSizeOfInitializedData(self) -> int: ...

    def getSizeOfUninitializedData(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressOfEntryPoint(self) -> int: ...

    @property
    def baseOfBss(self) -> int: ...

    @property
    def baseOfCode(self) -> int: ...

    @property
    def baseOfData(self) -> int: ...

    @property
    def cprMask(self) -> List[int]: ...

    @property
    def gpValue(self) -> int: ...

    @property
    def gprMask(self) -> int: ...

    @property
    def magic(self) -> int: ...

    @property
    def majorLinkerVersion(self) -> int: ...

    @property
    def minorLinkerVersion(self) -> int: ...

    @property
    def sizeOfCode(self) -> int: ...

    @property
    def sizeOfInitializedData(self) -> int: ...

    @property
    def sizeOfUninitializedData(self) -> int: ...
