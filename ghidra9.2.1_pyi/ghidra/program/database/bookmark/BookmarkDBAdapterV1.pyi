import ghidra.program.database.bookmark
import java.lang


class BookmarkDBAdapterV1(ghidra.program.database.bookmark.BookmarkDBAdapter):




    def __init__(self):
        """
        Constructor (used by BookmarkDBAdapterV2)
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
