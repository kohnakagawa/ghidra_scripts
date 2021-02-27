from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.next
import ghidra.util.task
import java.lang
import java.util


class DWARFAbbreviation(object):
    """
    This class represents the 'schema' for a DWARF DIE record.

     A raw DWARF DIE record specifies its abbreviation code (pointing to an instance of
     this class) and the corresponding DWARFAbbreviation instance has the information
     about how the raw DIE is laid out.
    """





    def __init__(self, abbreviationCode: int, tag: int, hasChildren: bool, attributes: List[ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification]): ...



    def equals(self, __a0: object) -> bool: ...

    def findAttribute(self, attribute: int) -> ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification:
        """
        Get the attribute with the given attribute key.
        @param attribute attribute key
        @return attribute specification
        """
        ...

    def getAbbreviationCode(self) -> int:
        """
        Get the abbreviation code.
        @return the abbreviation code
        """
        ...

    def getAttributeAt(self, index: int) -> ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification:
        """
        Get the attribute at the given index.
        @param index index of the attribute
        @return attribute specification
        """
        ...

    def getAttributeCount(self) -> int: ...

    def getAttributes(self) -> List[ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification]:
        """
        Return a live list of the attributes.
        @return list of attributes
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getTag(self) -> int:
        """
        Get the tag value.
        @return the tag value
        """
        ...

    def hasChildren(self) -> bool:
        """
        Checks to see if this abbreviation has any DIE children.
        @return true if this abbreviation has DIE children
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def read(reader: ghidra.app.util.bin.BinaryReader, prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, monitor: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.format.dwarf4.DWARFAbbreviation: ...

    @staticmethod
    def readAbbreviations(reader: ghidra.app.util.bin.BinaryReader, prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, monitor: ghidra.util.task.TaskMonitor) -> java.util.Map: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def abbreviationCode(self) -> int: ...

    @property
    def attributeCount(self) -> int: ...

    @property
    def attributes(self) -> List[ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification]: ...

    @property
    def tag(self) -> int: ...
