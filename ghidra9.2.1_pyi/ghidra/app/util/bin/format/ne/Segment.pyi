from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class Segment(object):
    """
    A class to represent a new-executable segment.
    """









    def equals(self, __a0: object) -> bool: ...

    def getBytes(self) -> List[int]:
        """
        Returns the bytes the comprise this segment.
         The size of the byte array is MAX(length,minalloc).
        @return the bytes the comprise this segment
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFlagword(self) -> int:
        """
        Returns the flag word of this segment.
        @return the flag word of this segment
        """
        ...

    def getLength(self) -> int:
        """
        Returns the length of this segment.
        @return the length of this segment
        """
        ...

    def getMinAllocSize(self) -> int:
        """
        Returns the minimum allocation size of this segment.
        @return the minimum allocation size of this segment
        """
        ...

    def getOffset(self) -> int:
        """
        Returns the offset to the contents of this segment.
         NOTE: This value needs to be shift aligned.
        @return the offset to the contents of this segment
        """
        ...

    def getOffsetShiftAligned(self) -> int:
        """
        Returns the actual (shifted) offset to the contents.
        @return the actual (shifted) offset to the contents
        """
        ...

    def getRelocations(self) -> List[ghidra.app.util.bin.format.ne.SegmentRelocation]:
        """
        Returns an array of the relocations defined for this segment.
        @return an array of the relocations defined for this segment
        """
        ...

    def getSegmentID(self) -> int:
        """
        Returns segment ID.
        @return segment ID
        """
        ...

    def hasRelocation(self) -> bool:
        """
        Returns true if this segment has relocations.
        @return true if this segment has relocations
        """
        ...

    def hashCode(self) -> int: ...

    def is32bit(self) -> bool:
        """
        Returns true if the segment should operate in 32 bit mode.
        @return true if the segment should operate in 32 bit mode
        """
        ...

    def isCode(self) -> bool:
        """
        Returns true if this is a code segment.
        @return true if this is a code segment
        """
        ...

    def isData(self) -> bool:
        """
        Returns true if this is a data segment.
        @return true if this is a data segment
        """
        ...

    def isDiscardable(self) -> bool:
        """
        Returns true if this segment is discardable.
        @return true if this segment is discardable
        """
        ...

    def isExecuteOnly(self) -> bool:
        """
        Returns true if this segment is execute-only.
        @return true if this segment is execute-only
        """
        ...

    def isLoaded(self) -> bool:
        """
        Returns true if this segment is loaded.
        @return true if this segment is loaded
        """
        ...

    def isLoaderAllocated(self) -> bool:
        """
        Returns true if this segment is loader allocated.
        @return true if this segment is loader allocated
        """
        ...

    def isMoveable(self) -> bool:
        """
        Returns true if this segment is moveable.
        @return true if this segment is moveable
        """
        ...

    def isPreload(self) -> bool:
        """
        Returns true if this segment is preloaded.
        @return true if this segment is preloaded
        """
        ...

    def isPure(self) -> bool:
        """
        Returns true if this segment is pure.
        @return true if this segment is pure
        """
        ...

    def isReadOnly(self) -> bool:
        """
        Returns true if this segment is read-only.
        @return true if this segment is read-only
        """
        ...

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
    def 32bit(self) -> bool: ...

    @property
    def bytes(self) -> List[int]: ...

    @property
    def code(self) -> bool: ...

    @property
    def data(self) -> bool: ...

    @property
    def discardable(self) -> bool: ...

    @property
    def executeOnly(self) -> bool: ...

    @property
    def flagword(self) -> int: ...

    @property
    def length(self) -> int: ...

    @property
    def loaded(self) -> bool: ...

    @property
    def loaderAllocated(self) -> bool: ...

    @property
    def minAllocSize(self) -> int: ...

    @property
    def moveable(self) -> bool: ...

    @property
    def offset(self) -> int: ...

    @property
    def offsetShiftAligned(self) -> int: ...

    @property
    def preload(self) -> bool: ...

    @property
    def pure(self) -> bool: ...

    @property
    def readOnly(self) -> bool: ...

    @property
    def relocations(self) -> List[ghidra.app.util.bin.format.ne.SegmentRelocation]: ...

    @property
    def segmentID(self) -> int: ...
