from typing import List
import ghidra.program.database.bookmark
import java.lang


class BookmarkTypeDBAdapterNoTable(ghidra.program.database.bookmark.BookmarkTypeDBAdapter):




    def __init__(self, dbHandle: db.DBHandle):
        """
        @param dbHandle the database handle
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTypeIds(self) -> List[int]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOldBookmarkManager(self, oldMgr: ghidra.program.database.bookmark.OldBookmarkManager) -> None:
        """
        Set the old bookmark manager which handles read-only access
         to bookmarks stored within property maps.
         The old bookmark manager must be set prior to invoking any other method;
        @param oldMgr old bookmark manager
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
    def oldBookmarkManager(self) -> None: ...  # No getter available.

    @oldBookmarkManager.setter
    def oldBookmarkManager(self, value: ghidra.program.database.bookmark.OldBookmarkManager) -> None: ...

    @property
    def typeIds(self) -> List[int]: ...
