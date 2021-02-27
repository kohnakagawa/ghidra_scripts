from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.awt
import java.lang
import javax.swing


class BookmarkManager(object):
    """
    Interface for managing bookmarks.
    """

    OLD_BOOKMARK_PROPERTY_OBJECT_CLASS1: unicode = u'ghidra.app.plugin.bookmark.BookmarkInfo'
    OLD_BOOKMARK_PROPERTY_OBJECT_CLASS2: unicode = u'ghidra.program.util.Bookmark'







    def defineType(self, type: unicode, icon: javax.swing.ImageIcon, color: java.awt.Color, priority: int) -> ghidra.program.model.listing.BookmarkType:
        """
        Define a bookmark type with its marker icon and color.  The icon and color
         values are not permanently stored.  Therefor, this method must be re-invoked
         by a plugin each time a program is opened if a custom icon and color
         are desired.
        @param type bookmark type
        @param icon marker icon which may get scaled
        @param color marker color
        @param priority the bookmark priority
        @return bookmark type object
        @throws IllegalArgumentException if any of the arguments are null or if the type is empty
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBookmark(self, id: long) -> ghidra.program.model.listing.Bookmark:
        """
        Returns the bookmark that has the given id or null if no such bookmark exists.
        @param id the id of the bookmark to be retrieved.
        @return the bookmark
        """
        ...

    @overload
    def getBookmark(self, addr: ghidra.program.model.address.Address, type: unicode, category: unicode) -> ghidra.program.model.listing.Bookmark:
        """
        Get a specific bookmark
        @param addr the address of the bookmark to retrieve
        @param type the name of the bookmark type.
        @param category the category of the bookmark.
        @return the bookmark with the given attributes, or null if no bookmarks match.
        """
        ...

    def getBookmarkAddresses(self, type: unicode) -> ghidra.program.model.address.AddressSetView:
        """
        Get addresses for bookmarks of a specified type.
        @param type bookmark type
        @return address set containing bookmarks of the specified type.
        """
        ...

    @overload
    def getBookmarkCount(self) -> int:
        """
        Returns the total number of bookmarks in the program
        @return the total number of bookmarks in the program
        """
        ...

    @overload
    def getBookmarkCount(self, type: unicode) -> int:
        """
        Return the number of bookmarks of the given type
        @param type the type of bookmarks to count
        @return the number of bookmarks of the given type
        """
        ...

    def getBookmarkType(self, type: unicode) -> ghidra.program.model.listing.BookmarkType:
        """
        Get a bookmark type
        @param type bookmark type name
        @return bookmark type or null if type is unknown
        """
        ...

    def getBookmarkTypes(self) -> List[ghidra.program.model.listing.BookmarkType]:
        """
        Returns list of known bookmark types
        @return list of known bookmark types
        """
        ...

    @overload
    def getBookmarks(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.listing.Bookmark]:
        """
        Get all bookmarks on a specific address
        @param addr the address at which to retrieve all bookmarks.
        @return array of bookmarks
        """
        ...

    @overload
    def getBookmarks(self, address: ghidra.program.model.address.Address, type: unicode) -> List[ghidra.program.model.listing.Bookmark]:
        """
        Get bookmarks of the indicated type on a specific address
        @param address the address at which to search for bookmarks.
        @param type bookmark type to search for
        @return array of bookmarks
        """
        ...

    @overload
    def getBookmarksIterator(self) -> Iterator[ghidra.program.model.listing.Bookmark]:
        """
        Returns an iterator over all bookmarks
        @return an iterator over all bookmarks
        """
        ...

    @overload
    def getBookmarksIterator(self, type: unicode) -> Iterator[ghidra.program.model.listing.Bookmark]:
        """
        Get iterator over all bookmarks of the specified type.
        @param type the bookmark type to search for
        @return an iterator over all bookmarks of the specified type.
        """
        ...

    @overload
    def getBookmarksIterator(self, startAddress: ghidra.program.model.address.Address, forward: bool) -> Iterator[ghidra.program.model.listing.Bookmark]:
        """
        Returns an iterator over all bookmark types, starting at the given address, with traversal
         in the given direction.
        @param startAddress the address at which to start
        @param forward true to iterate in the forward direction; false for backwards
        @return an iterator over all bookmark types, starting at the given address, with traversal
         		   in the given direction.
        """
        ...

    def getCategories(self, type: unicode) -> List[unicode]:
        """
        Get list of categories used for a specified type
        @param type bookmark type
        @return array of category strings
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program associated with this BookmarkManager.
        @return the program associated with this BookmarkManager.
        """
        ...

    def hasBookmarks(self, type: unicode) -> bool:
        """
        Returns true if program contains one or more bookmarks of the given type
        @param type the type of bookmark to check for.
        @return true if program contains one or more bookmarks of the given type
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeBookmark(self, bookmark: ghidra.program.model.listing.Bookmark) -> None:
        """
        Remove bookmark
        @param bookmark the bookmark to remove.
        """
        ...

    @overload
    def removeBookmarks(self, type: unicode) -> None:
        """
        Removes all bookmarks of the given type.
        @param type bookmark type
        """
        ...

    @overload
    def removeBookmarks(self, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Removes all bookmarks over the given address set.
        @param set the set of addresses from which to remove all bookmarks.
        @param monitor a task monitor to report the progress.
        @throws CancelledException if the user (via the monitor) cancelled the operation.
        """
        ...

    @overload
    def removeBookmarks(self, type: unicode, category: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Removes all bookmarks with the given type and category.
        @param type the type of the bookmarks to be removed.
        @param category bookmark category of the types to be removed.
        @param monitor a task monitor to report the progress.
        @throws CancelledException if the user (via the monitor) cancelled the operation.
        """
        ...

    @overload
    def removeBookmarks(self, set: ghidra.program.model.address.AddressSetView, type: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Removes all bookmarks of the given type over the given address set
        @param set the set of addresses from which to remove all bookmarks of the given type.
        @param type the type of bookmarks to remove.
        @param monitor a task monitor to report the progress.
        @throws CancelledException if the user (via the monitor) cancelled the operation.
        """
        ...

    @overload
    def removeBookmarks(self, set: ghidra.program.model.address.AddressSetView, type: unicode, category: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Removes all bookmarks of the given type and category over the given address set
        @param set the set of addresses from which to remove all bookmarks of the given type and category.
        @param type the type of bookmarks to remove.
        @param category the category of bookmarks to remove.
        @param monitor a task monitor to report the progress.
        @throws CancelledException if the user (via the monitor) cancelled the operation.
        """
        ...

    def setBookmark(self, addr: ghidra.program.model.address.Address, type: unicode, category: unicode, comment: unicode) -> ghidra.program.model.listing.Bookmark:
        """
        Set a bookmark.
        @param addr the address at which to set a bookmark
        @param type the name of the bookmark type.
        @param category the category for the bookmark.
        @param comment the comment to associate with the bookmark.
        @return the new bookmark
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
    def bookmarkCount(self) -> int: ...

    @property
    def bookmarkTypes(self) -> List[ghidra.program.model.listing.BookmarkType]: ...

    @property
    def bookmarksIterator(self) -> java.util.Iterator: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
