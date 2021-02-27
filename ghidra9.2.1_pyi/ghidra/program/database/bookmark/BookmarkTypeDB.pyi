import ghidra.program.model.listing
import java.awt
import java.lang
import javax.swing


class BookmarkTypeDB(object, ghidra.program.model.listing.BookmarkType):
    ALL_TYPES: unicode = u'All Bookmark Types'
    ANALYSIS: unicode = u'Analysis'
    ERROR: unicode = u'Error'
    INFO: unicode = u'Info'
    NOTE: unicode = u'Note'
    WARNING: unicode = u'Warning'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIcon(self) -> javax.swing.ImageIcon: ...

    def getMarkerColor(self) -> java.awt.Color: ...

    def getMarkerPriority(self) -> int: ...

    def getTypeId(self) -> int: ...

    def getTypeString(self) -> unicode: ...

    def hasBookmarks(self) -> bool: ...

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
    def icon(self) -> javax.swing.ImageIcon: ...

    @property
    def markerColor(self) -> java.awt.Color: ...

    @property
    def markerPriority(self) -> int: ...

    @property
    def typeId(self) -> int: ...

    @property
    def typeString(self) -> unicode: ...
