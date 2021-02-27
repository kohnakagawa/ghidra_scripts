import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class Bookmark(java.lang.Comparable, object):
    """
    Interface for bookmarks.  Bookmarks are locations that are marked within the program so
     that they can be easily found.
    """









    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns address at which this bookmark is applied.
        """
        ...

    def getCategory(self) -> unicode:
        """
        Returns bookmark category
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Returns bookmark comment
        """
        ...

    def getId(self) -> long:
        """
        Returns the id of the bookmark.
        """
        ...

    def getType(self) -> ghidra.program.model.listing.BookmarkType:
        """
        Returns bookmark type object.
        """
        ...

    def getTypeString(self) -> unicode:
        """
        Returns bookmark type as a string
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def set(self, category: unicode, comment: unicode) -> None:
        """
        Set the category and comment associated with a bookmark.
        @param category category
        @param comment single line comment
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def category(self) -> unicode: ...

    @property
    def comment(self) -> unicode: ...

    @property
    def id(self) -> long: ...

    @property
    def type(self) -> ghidra.program.model.listing.BookmarkType: ...

    @property
    def typeString(self) -> unicode: ...
