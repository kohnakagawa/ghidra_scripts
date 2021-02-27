from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class DataBuffer(object):
    """
    DataBuffer provides an array like interface into a set of Data
     at a specific index.  Data can be retrieved by using a positive
     offset from the current position.  The purpose of this class is to
     provide an opaque storage mechanism for Data that is made up of other
     Data items.

     This interface does not provide methods to reposition the data item
     buffer.  This is so that it is clear that methods accepeting this
     base class are not to mess which the base Address for this object.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the Address which corresponds to the offset 0.
        @return the current address of offset 0.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getData(self, offset: int) -> ghidra.program.model.listing.Data:
        """
        Get one Data item from the buffer at the current position plus offset.
        @param offset the displacement from the current position.
        @return the Data item at offset from the current position.
        @throws ghidra.program.model.address.AddressOutOfBoundsException if offset exceeds
         address space
        @throws IndexOutOfBoundsException if offset is negative
        """
        ...

    @overload
    def getData(self, start: int, end: int) -> List[ghidra.program.model.listing.Data]:
        """
        Get an array of data items that begin at or after start up to end.
           Data items that exist before start are not returned
           Data items that exist before end, but terminate after end ARE returned
        @param start start offset
        @param end end offset
        @return array of CodeDatas that exist between start and end.
        """
        ...

    def getDataAfter(self, offset: int) -> ghidra.program.model.listing.Data:
        """
        Get the next data item starting after offset.
        @param offset offset to look after
        @return Data item starting after this offset
        """
        ...

    def getDataBefore(self, offset: int) -> ghidra.program.model.listing.Data:
        """
        Get the previous data item starting before offset.
        @param offset offset to look before
        @return Data item starting before this offset
        """
        ...

    def getNextOffset(self, offset: int) -> int:
        """
        Get the offset to the next data item found after offset.
        @param offset offset to look after
        @return offset of the first data item existing after this one.
        """
        ...

    def getPreviousOffset(self, offset: int) -> int:
        """
        Get the offset to the previous data item existing before this offset.
        @param offset offset to look before
        @return offset of the first data item existing before this one.
        """
        ...

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
    def address(self) -> ghidra.program.model.address.Address: ...
