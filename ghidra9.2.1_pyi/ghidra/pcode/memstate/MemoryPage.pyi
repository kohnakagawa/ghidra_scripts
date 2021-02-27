from typing import List
import java.lang


class MemoryPage(object):
    """
    MemoryPage is allows the contents/data of a memory page
     to be maintained along with an initializedMask.  Each bit within the
     initializedMask corresponds to a data byte within the page.  A null
     mask indicates that all data within the page is initialized.  A one-bit
     within the mask indicates that the corresponding data byte is initialized.
    """

    data: List[int]



    @overload
    def __init__(self, pageSize: int):
        """
        Construct a new fully initialized page containing
         all zero (0) byte data.
        """
        ...

    @overload
    def __init__(self, bytes: List[int]):
        """
        Construct a memory page with an existing data bytes buffer
        @param bytes buffer
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getInitializedByteCount(self, pageOffset: int, size: int) -> int:
        """
        Get number of leading bytes within page range which have been
         initialized.
        @param pageOffset
        @param size
        @return number of leading bytes within page range which have been
         initialized.
        """
        ...

    @overload
    @staticmethod
    def getInitializedByteCount(initializedMask: List[int], pageOffset: int, size: int) -> int:
        """
        Determine how many leading bytes of a specified page region is marked as
         initialized.  Valid page region defined by pageOffset and size is assumed.
        @param initializedMask
        @param pageOffset
        @param size
        @return number of leading bytes at pageOffset (upto size) are initialized.
        """
        ...

    @overload
    def getInitializedMask(self) -> List[int]: ...

    @overload
    @staticmethod
    def getInitializedMask(pageSize: int, initialized: bool) -> List[int]:
        """
        Generate an initialized mask for the specified page size
        @param pageSize
        @param initialized
        @return
        """
        ...

    @overload
    @staticmethod
    def getInitializedMask(pageSize: int, offset: int, size: int, initialized: bool) -> List[int]:
        """
        Generate an initialized mask for the specified page size.
         The region is identified by offset and size.  The remaining portions
         of the mask will be set based upon !initialized.
        @param pageSize
        @param offset
        @param size
        @param initialized
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setInitialized(self) -> None:
        """
        Mark entire page as uninitialized
        """
        ...

    @overload
    def setInitialized(self, pageOffset: int, size: int) -> None:
        """
        Mark specified page region as initialized.
        @param pageOffset
        @param size
        """
        ...

    @overload
    def setInitialized(self, pageOffset: int, size: int, maskUpdate: List[int]) -> None:
        """
        Update initialization mask
        @param pageOffset
        @param size
        @param maskUpdate
        """
        ...

    @overload
    @staticmethod
    def setInitialized(initializedMask: List[int], pageOffset: int, size: int) -> None:
        """
        Mark specified page region as initialized.
        @param initializedMask
        @param pageOffset
        @param size
        """
        ...

    @overload
    def setUninitialized(self) -> None:
        """
        Mark entire page as uninitialized
        """
        ...

    @overload
    def setUninitialized(self, pageOffset: int, size: int) -> None:
        """
        Mark specified page region as uninitialized.
        @param pageOffset
        @param size
        """
        ...

    @overload
    @staticmethod
    def setUninitialized(initializedMask: List[int], pageOffset: int, size: int) -> None:
        """
        Mark specified page region as uninitialized.
        @param initializedMask
        @param pageOffset
        @param size
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
    def initializedMask(self) -> List[int]: ...
