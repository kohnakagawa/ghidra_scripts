from typing import List
import ghidra.program.database.map
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.util
import java.lang


class AddressMap(object):
    """
    Address map interface add methods need by the program database implementation to manage its address map.
     NOTE: Objects implementing this interface are not intended for use outside of the
     ghidra.program.database packages.
    """

    INVALID_ADDRESS_KEY: long = -0x1L







    def decodeAddress(self, value: long) -> ghidra.program.model.address.Address:
        """
        Returns the address that was used to generate the given long key. (If the image base was
         moved, then a different address is returned unless the value was encoded using the
         "absoluteEncoding" method.  If the program's default address space is segmented (i.e., SegmentedAddressSpace).
         the address returned will be always be normalized to defined segmented memory blocks if possible.
        @param value the long value to convert to an address.
        """
        ...

    def deleteOverlaySpace(self, name: unicode) -> None:
        """
        Delete the specified overlay space from this address map.
        @param name overlay space name (must be unique among all space names within this map)
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findKeyRange(self, __a0: List[object], __a1: ghidra.program.model.address.Address) -> int: ...

    def getAbsoluteEncoding(self, addr: ghidra.program.model.address.Address, create: bool) -> long:
        """
        Get the database key associated with the given absolute address.
         This key uniquely identifies an absolute location within the program.
         If the requested key does not exist and create is false, INVALID_ADDRESS_KEY
         will be returned.  Note that nothing should ever be stored using the returned key unless
         create is true.
        @param addr the address for which to get a database key.
        @param create true if a new key may be generated
        @return the database key for the given address or INVALID_ADDRESS_KEY if
         create is false and one does not exist for the specified addr.
        """
        ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory:
        """
        Returns the address factory associated with this map.
         Null may be returned if map not associated with a specific address factory.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getImageBase(self) -> ghidra.program.model.address.Address:
        """
        Returns the current image base setting.
        """
        ...

    def getKey(self, addr: ghidra.program.model.address.Address, create: bool) -> long:
        """
        Get the database key associated with the given relative address.
         This key uniquely identifies a relative location within the program.
         If the program's image base is moved to another address, this key will map to a new
         address that is the same distance to the new base as the old address was to the old base.
         If the requested key does not exist and create is false, INVALID_ADDRESS_KEY
         will be returned.  Note that nothing should ever be stored using the returned key unless
         create is true.
        @param addr the address for which to get a database key.
        @param create true if a new key may be generated
        @return the database key for the given address or INVALID_ADDRESS_KEY if
         create is false and one does not exist for the specified addr.
        """
        ...

    @overload
    def getKeyRanges(self, set: ghidra.program.model.address.AddressSetView, create: bool) -> List[ghidra.program.model.address.KeyRange]:
        """
        Generates a properly ordered list of database key ranges for a
         a specified address set.  If absolute encodings are requested,
         only memory addresses will be included.
        @param set address set or null for all real address.
        @param create true if a new keys may be generated, otherwise returned
         key-ranges will be limited to those already defined.
        @return "sorted" list of KeyRange objects
        """
        ...

    @overload
    def getKeyRanges(self, set: ghidra.program.model.address.AddressSetView, absolute: bool, create: bool) -> List[ghidra.program.model.address.KeyRange]:
        """
        Generates a properly ordered list of database key ranges for a
         a specified address set.  If absolute encodings are requested,
         only memory addresses will be included.
        @param set address set or null for all real address.
        @param absolute if true, absolute key encodings are returned, otherwise
         standard/relocatable address key encodings are returned.
        @param create true if a new keys may be generated, otherwise returned
         key-ranges will be limited to those already defined.
        @return "sorted" list of KeyRange objects
        """
        ...

    @overload
    def getKeyRanges(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, create: bool) -> List[ghidra.program.model.address.KeyRange]:
        """
        Generates a properly ordered list of database key ranges for a
         a specified address range.  If absolute encodings are requested,
         only memory addresses will be included.  Returned key ranges are
         generally intended for read-only operations since new keys will
         never be generated.  The returned key ranges will correspond
         to those key ranges which have previously been created within
         the specified address range and may represent a much smaller subset
         of addresses within the specified range.
        @param start minimum address of range
        @param end maximum address of range
        @param create true if a new keys may be generated, otherwise returned
         key-ranges will be limited to those already defined.
        @return "sorted" list of KeyRange objects
        """
        ...

    @overload
    def getKeyRanges(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, absolute: bool, create: bool) -> List[ghidra.program.model.address.KeyRange]:
        """
        Generates a properly ordered list of database key ranges for a
         a specified address range.  If absolute encodings are requested,
         only memory addresses will be included.
        @param start minimum address of range
        @param end maximum address of range
        @param absolute if true, absolute key encodings are returned, otherwise
         standard/relocatable address key encodings are returned.
        @param create true if a new keys may be generated, otherwise returned
         key-ranges will be limited to those already defined.
        @return "sorted" list of KeyRange objects
        """
        ...

    def getModCount(self) -> int:
        """
        Returns a modification number that always increases when the address map base table has
         changed.
        """
        ...

    def getOldAddressMap(self) -> ghidra.program.database.map.AddressMap:
        """
        Returns an address map capable of decoding old address encodings.
        """
        ...

    def hasSameKeyBase(self, addrKey1: long, addrKey2: long) -> bool:
        """
        Returns true if the two address keys share a common key base and can be
         used within a single key-range.
        @param addrKey1
        @param addrKey2
        """
        ...

    def hashCode(self) -> int: ...

    def invalidateCache(self) -> None:
        """
        Clears any cached values.
        @throws IOException
        """
        ...

    def isKeyRangeMax(self, addrKey: long) -> bool:
        """
        Returns true if the specified addrKey is the maximum key within
         its key-range.
        @param addrKey
        """
        ...

    def isKeyRangeMin(self, addrKey: long) -> bool:
        """
        Returns true if the specified addrKey is the minimum key within
         its key-range.
        @param addrKey
        """
        ...

    def isUpgraded(self) -> bool:
        """
        Returns true if this address map has been upgraded.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def renameOverlaySpace(self, oldName: unicode, newName: unicode) -> None:
        """
        Rename an existing overlay space.
        @param oldName old overlay name
        @param newName new overlay name (must be unique among all space names within this map)
        @throws IOException
        """
        ...

    def setImageBase(self, base: ghidra.program.model.address.Address) -> None:
        """
        Sets the image base, effectively changing the mapping between addresses and longs.
        @param base the new base address.
        """
        ...

    def setLanguage(self, newLanguage: ghidra.program.model.lang.Language, addrFactory: ghidra.program.model.address.AddressFactory, translator: ghidra.program.util.LanguageTranslator) -> None:
        """
        Converts the current base addresses to addresses compatible with the new language.
        @param newLanguage the new language to use.
        @param addrFactory the new AddressFactory.
        @param translator translates address spaces from the old language to the new language.
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
