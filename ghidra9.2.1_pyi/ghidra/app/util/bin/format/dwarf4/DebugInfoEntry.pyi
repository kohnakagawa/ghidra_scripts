from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.attribs
import java.lang


class DebugInfoEntry(object):
    """
    A DWARF Debug Info Entry is a collection of DWARFAttributeValue
     in a hierarchical structure (see #getParent(), #getChildren()).

     This class is a lower-level class and DIEAggregate should be used instead in most
     cases when examining information from the DWARF system.
    """





    def __init__(self, unit: ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit, offset: long, abbreviation: ghidra.app.util.bin.format.dwarf4.DWARFAbbreviation):
        """
        Creates an empty DIE.  Used by {@link #read(BinaryReader, DWARFCompilationUnit, DWARFAttributeFactory) static read()}
         and junit tests.
         <p>
        @param unit
        @param offset
        @param abbreviation
        """
        ...



    def addChild(self, child: ghidra.app.util.bin.format.dwarf4.DebugInfoEntry) -> None:
        """
        Add a child DIE to this DIE.
        @param child DIE of the child
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getAbbreviation(self) -> ghidra.app.util.bin.format.dwarf4.DWARFAbbreviation:
        """
        Get the abbreviation of this DIE.
        @return the abbreviation of this DIE
        """
        ...

    def getAttributes(self) -> List[ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue]: ...

    @overload
    def getChildren(self) -> List[ghidra.app.util.bin.format.dwarf4.DebugInfoEntry]:
        """
        Return a live list of the child DIE's.
        @return list of child DIE's
        """
        ...

    @overload
    def getChildren(self, childTag: int) -> List[ghidra.app.util.bin.format.dwarf4.DebugInfoEntry]:
        """
        Return a list of children that are of a specific DWARF type.
         <p>
        @param childTag
        @return
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilationUnit(self) -> ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit: ...

    def getOffset(self) -> long:
        """
        Get the offset of this DIE from the beginning of the debug_info section.
        @return the offset of this DIE from the beginning of the debug_info section
        """
        ...

    def getParent(self) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry:
        """
        Get the parent DIE of this DIE.
        @return the parent DIE
        """
        ...

    def getTag(self) -> int:
        """
        Get the DWARFTag value of this DIE.
        @return the DWARFTag value of this DIE
        """
        ...

    def hasAttribute(self, attribute: int) -> bool:
        """
        Check to see if this DIE has the given attribute key.
        @param attribute the attribute key
        @return true if the DIE contains the attribute and false otherwise
        """
        ...

    def hasChildren(self) -> bool:
        """
        Check to see if this DIE has any child DIE's.
        @return true if there are child DIE's and false otherwise
        """
        ...

    def hashCode(self) -> int: ...

    def isTerminator(self) -> bool:
        """
        Check to see if the DIE is a terminator.
        @return true if the DIE is a terminator and false otherwise
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def read(reader: ghidra.app.util.bin.BinaryReader, unit: ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit, attributeFactory: ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeFactory) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry:
        """
        Read a DIE record.
        @param reader
        @param unit
        @param attributeFactory
        @return
        @throws IOException
        """
        ...

    def setParent(self, parent: ghidra.app.util.bin.format.dwarf4.DebugInfoEntry) -> None:
        """
        Set the parent DIE of this DIE.
        @param parent the parent DIE
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
    def abbreviation(self) -> ghidra.app.util.bin.format.dwarf4.DWARFAbbreviation: ...

    @property
    def attributes(self) -> List[ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue]: ...

    @property
    def children(self) -> List[object]: ...

    @property
    def compilationUnit(self) -> ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit: ...

    @property
    def offset(self) -> long: ...

    @property
    def parent(self) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry: ...

    @parent.setter
    def parent(self, value: ghidra.app.util.bin.format.dwarf4.DebugInfoEntry) -> None: ...

    @property
    def tag(self) -> int: ...

    @property
    def terminator(self) -> bool: ...
