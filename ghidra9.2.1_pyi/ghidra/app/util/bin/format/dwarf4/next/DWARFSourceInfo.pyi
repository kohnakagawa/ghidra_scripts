import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.next
import java.lang


class DWARFSourceInfo(object):
    """
    Small class to hold the filename and line number info values from
     DWARF DebugInfoEntry.
    """









    @staticmethod
    def create(diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> ghidra.app.util.bin.format.dwarf4.next.DWARFSourceInfo:
        """
        Creates a new {@link DWARFSourceInfo} instance from the supplied {@link DIEAggregate}
         if the info is present, otherwise returns null;
        @param diea {@link DIEAggregate} to query for source info
        @return new {@link DWARFSourceInfo} with filename:linenum info, or null if no info present in DIEA.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getDescriptionStr(self) -> unicode:
        """
        Returns the source location info as a string formatted as "filename:linenum"
        @return "filename:linenum"
        """
        ...

    @overload
    @staticmethod
    def getDescriptionStr(diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> unicode:
        """
        Returns the source file and line number info attached to the specified {@link DIEAggregate}
         formatted as {@link #getDescriptionStr()}, or null if not present.
        @param diea {@link DIEAggregate} to query
        @return string, see {@link #getDescriptionStr()}
        """
        ...

    def getDescriptionStr2(self) -> unicode:
        """
        Returns the source location info as a string formatted as "File: filename Line: linenum"
        @return "File: filename Line: linenum"
        """
        ...

    def getFilename(self) -> unicode:
        """
        Returns the filename
        @return string filename.
        """
        ...

    @staticmethod
    def getSourceInfoWithFallbackToParent(diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> ghidra.app.util.bin.format.dwarf4.next.DWARFSourceInfo:
        """
        Creates a new {@link DWARFSourceInfo} instance from the supplied {@link DIEAggregate},
         falling back to the parent containing DIE record if the first record did not have any
         source info.
        @param diea {@link DIEAggregate} to query for source info.
        @return new {@link DWARFSourceInfo} with filename:linenum info, or null if no info
         present in the specified DIEA and its parent.
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
    def descriptionStr(self) -> unicode: ...

    @property
    def descriptionStr2(self) -> unicode: ...

    @property
    def filename(self) -> unicode: ...
