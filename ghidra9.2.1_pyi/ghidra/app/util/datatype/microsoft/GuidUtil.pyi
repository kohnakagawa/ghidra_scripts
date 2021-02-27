from typing import List
import ghidra.app.util.datatype.microsoft
import ghidra.app.util.datatype.microsoft.GuidUtil
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class GuidUtil(object):





    class GuidType(java.lang.Enum):
        CLSID: ghidra.app.util.datatype.microsoft.GuidUtil.GuidType = CLSID
        GUID: ghidra.app.util.datatype.microsoft.GuidUtil.GuidType = GUID
        IID: ghidra.app.util.datatype.microsoft.GuidUtil.GuidType = IID
        SYNTAX: ghidra.app.util.datatype.microsoft.GuidUtil.GuidType = SYNTAX







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def getFilename(self) -> unicode: ...

        def hasVersion(self) -> bool: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.datatype.microsoft.GuidUtil.GuidType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.datatype.microsoft.GuidUtil.GuidType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def filename(self) -> unicode: ...

    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getGuidString(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, validate: bool) -> unicode: ...

    @overload
    @staticmethod
    def getKnownGuid(guidString: unicode) -> ghidra.app.util.datatype.microsoft.GuidInfo: ...

    @overload
    @staticmethod
    def getKnownGuid(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> ghidra.app.util.datatype.microsoft.GuidInfo: ...

    @staticmethod
    def getKnownVersionedGuid(versionedGuidString: unicode) -> ghidra.app.util.datatype.microsoft.GuidInfo: ...

    @staticmethod
    def getVersionedGuidString(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, validate: bool) -> unicode: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isGuidLabel(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, label: unicode) -> bool:
        """
        Verify that the specified label correpsonds to a Microsoft symbol name
         for the GUID stored at the specified address within program.
        @param program program
        @param address memory address
        @param label symbol name to be checked
        @return true if label is a valid GUID label which corresponds to the GUID
         stored at address within program
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseLine(guidNameLine: unicode, delim: unicode, guidType: ghidra.app.util.datatype.microsoft.GuidUtil.GuidType) -> ghidra.app.util.datatype.microsoft.GuidInfo: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
