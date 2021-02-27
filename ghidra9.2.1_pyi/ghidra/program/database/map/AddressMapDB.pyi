from typing import List
import ghidra.program.database.map
import ghidra.program.database.mem
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.util
import java.lang


class AddressMapDB(object, ghidra.program.database.map.AddressMap):
    """
    Class used to map addresses to longs and longs to addresses. Several different encodings
     are depending on the nature of the address to be converted.
     The upper 4 bits in the long are used to specify the encoding used. Currently the encoding are:
     0 - use the original ghidra encoding - used for backwards compatibility.
     1 - absolute encoding - ignores the image base - used only by the memory map.
     2 - relocatable - most common encoding - allows address to move with the image base.
     3 - register - used to encode register addresses
     4 - stack - used to encode stack addresses (includes namespace information to make them unique between functions)
     5 - external - used to encode addresses in another program
     15 - no address - used to represent the null address or a meaningless address.
    """

    INVALID_ADDRESS_KEY: long = -0x1L



    def __init__(self, handle: db.DBHandle, openMode: int, factory: ghidra.program.model.address.AddressFactory, baseImageOffset: long, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructs a new AddressMapDB object
        @param handle the handle to the database
        @param openMode the mode that program was opened.
        @param factory the address factory containing all the address spaces for the program.
        @param baseImageOffset the current image base offset.
        @param monitor the progress monitory used for upgrading.
        @throws IOException thrown if a dabase io error occurs.
        @throws VersionException if the database version does not match the expected version.
        """
        ...



    @overload
    def decodeAddress(self, value: long) -> ghidra.program.model.address.Address: ...

    @overload
    def decodeAddress(self, value: long, useMemorySegmentation: bool) -> ghidra.program.model.address.Address:
        """
        Returns the address that was used to generate the given long key. (If the image base was
         moved, then a different address is returned unless the value was encoded using the
         "absoluteEncoding" method
        @param value the long value to convert to an address.
        @param useMemorySegmentation if true and the program's default address space is segmented (i.e., SegmentedAddressSpace).
         the address returned will be normalized to defined segmented memory blocks if possible.  This parameter should
         generally always be true except when used by the Memory map objects to avoid recursion problems.
        """
        ...

    def deleteOverlaySpace(self, name: unicode) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findKeyRange(self, __a0: List[object], __a1: ghidra.program.model.address.Address) -> int: ...

    def getAbsoluteEncoding(self, addr: ghidra.program.model.address.Address, create: bool) -> long: ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    def getClass(self) -> java.lang.Class: ...

    def getImageBase(self) -> ghidra.program.model.address.Address: ...

    def getKey(self, addr: ghidra.program.model.address.Address, create: bool) -> long: ...

    @overload
    def getKeyRanges(self, set: ghidra.program.model.address.AddressSetView, create: bool) -> List[ghidra.program.model.address.KeyRange]: ...

    @overload
    def getKeyRanges(self, set: ghidra.program.model.address.AddressSetView, absolute: bool, create: bool) -> List[ghidra.program.model.address.KeyRange]: ...

    @overload
    def getKeyRanges(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, create: bool) -> List[ghidra.program.model.address.KeyRange]: ...

    @overload
    def getKeyRanges(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, absolute: bool, create: bool) -> List[ghidra.program.model.address.KeyRange]: ...

    def getModCount(self) -> int: ...

    def getOldAddressMap(self) -> ghidra.program.database.map.AddressMap:
        """
        Returns an address map which may be used during the upgrade of old address
         encodings.  If the address map is up-to-date, then this method will return
         this instance of AddressMapDB.
        """
        ...

    def hasSameKeyBase(self, addrKey1: long, addrKey2: long) -> bool: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self) -> None: ...

    def isKeyRangeMax(self, addrKey: long) -> bool: ...

    def isKeyRangeMin(self, addrKey: long) -> bool: ...

    def isUpgraded(self) -> bool: ...

    def memoryMapChanged(self, mem: ghidra.program.database.mem.MemoryMapDB) -> None:
        """
        Notification when the memory map changes.  If we are segemented, we need to update our
         list of address ranges used for address normalization.
        @param mem the changed memory map.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def renameOverlaySpace(self, oldName: unicode, newName: unicode) -> None: ...

    def setImageBase(self, base: ghidra.program.model.address.Address) -> None: ...

    def setLanguage(self, newLanguage: ghidra.program.model.lang.Language, addrFactory: ghidra.program.model.address.AddressFactory, translator: ghidra.program.util.LanguageTranslator) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    @property
    def imageBase(self) -> ghidra.program.model.address.Address: ...

    @imageBase.setter
    def imageBase(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def modCount(self) -> int: ...

    @property
    def oldAddressMap(self) -> ghidra.program.database.map.AddressMap: ...

    @property
    def upgraded(self) -> bool: ...
