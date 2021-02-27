from typing import List
import java.lang


class Resource(object):
    """
    An implementation of the new-executable TNAMEINFO structure.
    """

    FLAG_MOVEABLE: int = 16
    FLAG_PRELOAD: int = 64
    FLAG_PURE: int = 32







    def equals(self, __a0: object) -> bool: ...

    def getBytes(self) -> List[int]:
        """
        Returns the actual bytes for this resource.
        @return the actual bytes for this resource
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileLength(self) -> int:
        """
        Returns the file length of this resource.
        @return the file length of this resource
        """
        ...

    def getFileLengthShifted(self) -> int:
        """
        Returns the shifted file length of this resource.
         <code>this.getFileLength() &lt;&lt; ResourceTable.getAlignmentShiftCount()</code>
        @return the shifted file length of this resource
        """
        ...

    def getFileOffset(self) -> int:
        """
        Returns the file offset of this resource.
        @return the file offset of this resource
        """
        ...

    def getFileOffsetShifted(self) -> int:
        """
        Returns the shifted file offset of this resource.
         <code>this.getFileOffset() &lt;&lt; ResourceTable.getAlignmentShiftCount()</code>
        @return the shifted file offset of this resource
        """
        ...

    def getFlagword(self) -> int:
        """
        Returns the flag word of this resource.
        @return the flag word of this resource
        """
        ...

    def getHandle(self) -> int:
        """
        Returns the handle of this resource.
        @return the handle of this resource
        """
        ...

    def getResourceID(self) -> int:
        """
        Returns the resource ID of this resource.
        @return the resource ID of this resource
        """
        ...

    def getUsage(self) -> int:
        """
        Returns the usage of this resource.
        @return the usage of this resource
        """
        ...

    def hashCode(self) -> int: ...

    def isMoveable(self) -> bool:
        """
        Returns true if this resource is moveable.
        @return true if this resource is moveable
        """
        ...

    def isPreload(self) -> bool:
        """
        Returns true if this resource is preloaded.
        @return true if this resource is preloaded
        """
        ...

    def isPure(self) -> bool:
        """
        Returns true if this resource is pure.
        @return true if this resource is pure
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bytes(self) -> List[int]: ...

    @property
    def fileLength(self) -> int: ...

    @property
    def fileLengthShifted(self) -> int: ...

    @property
    def fileOffset(self) -> int: ...

    @property
    def fileOffsetShifted(self) -> int: ...

    @property
    def flagword(self) -> int: ...

    @property
    def handle(self) -> int: ...

    @property
    def moveable(self) -> bool: ...

    @property
    def preload(self) -> bool: ...

    @property
    def pure(self) -> bool: ...

    @property
    def resourceID(self) -> int: ...

    @property
    def usage(self) -> int: ...
