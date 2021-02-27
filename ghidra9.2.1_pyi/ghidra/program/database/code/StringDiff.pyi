import ghidra.program.database.code
import java.lang


class StringDiff(object):
    """
    Container object that holds a start and end position within a string. A list of StringDiffs
     is used to keep track of changes made to a string.
    """

    text: unicode







    @staticmethod
    def allTextReplaced(newText: unicode) -> ghidra.program.database.code.StringDiff:
        """
        Construct a new StringDiff with pos1 and pos2 are initialized to -1
        @param newText string
        @return the new diff
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restore(text: unicode, start: int, end: int) -> ghidra.program.database.code.StringDiff: ...

    @staticmethod
    def textDeleted(start: int, end: int) -> ghidra.program.database.code.StringDiff:
        """
        Construct a new StringDiff that indicates text was deleted from pos1 to pos2
        @param start position 1 for the diff
        @param end position 2 for the diff
        @return the new diff
        """
        ...

    @staticmethod
    def textInserted(newText: unicode, start: int) -> ghidra.program.database.code.StringDiff:
        """
        Construct a new StringDiff that indicates that insertData was inserted at the given position
        @param newText inserted string
        @param start position where the text was inserted
        @return the new diff
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
