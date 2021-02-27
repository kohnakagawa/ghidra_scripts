from typing import List
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.attribs
import ghidra.app.util.bin.format.dwarf4.next
import java.lang


class DIEAggregate(object):
    """
    DIEAggregate groups related DebugInfoEntry records together in a single interface
     for querying attribute values.

     Information about program elements are written into the .debug_info as partial snapshots
     of the element, with later follow-up records that more fully specify the program element.

     (For instance, a declaration-only DIE that introduces the name of a structure type
     will be found at the beginning of a compilation unit, followed later by a DIE that
     specifies the contents of the structure type)

     A DIEAggregate groups these DebugInfoEntry records under one interface so a fully
     specified view of the program element can be presented.
    """









    @staticmethod
    def createFromHead(die: ghidra.app.util.bin.format.dwarf4.DebugInfoEntry) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate:
        """
        Creates a {@link DIEAggregate} starting from a 'head' {@link DebugInfoEntry} instance.
         <p>
         DW_AT_abstract_origin and DW_AT_specification attributes are followed to find the previous
         {@link DebugInfoEntry} instances.
         <p>
        @param die starting DIE record
        @return new {@link DIEAggregate} made up of the starting DIE and all DIEs that it points
         to via abstract_origin and spec attributes.
        """
        ...

    @staticmethod
    def createSingle(die: ghidra.app.util.bin.format.dwarf4.DebugInfoEntry) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate:
        """
        Create a {@link DIEAggregate} from a single {@link DebugInfoEntry DIE}.
         <p>
         Mainly useful early in the {@link DWARFCompilationUnit}'s bootstrapping process
         when it needs to read values from DIEs.
         <p>
        @param die
        @return
        """
        ...

    @staticmethod
    def createSkipHead(source: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate:
        """
        Creates a new {@link DIEAggregate} from the contents of the specified DIEA, using
         all the source's {@link DebugInfoEntry} fragments except for the head fragment
         which is skipped.
         <p>
         Used when a DIEA is composed of a head DIE with a different TAG type than the rest of
         the DIEs.  (ie. a dw_tag_call_site -&gt; dw_tag_sub DIEA)
        @param source
        @return
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def evaluateLocation(self, location: ghidra.app.util.bin.format.dwarf4.DWARFLocation) -> long:
        """
        Evaluate the DWARFExpression located in the DWARFLocation object in the context of
         this DIEA.
         <p>
        @param location
        @return
        @throws IOException
        @throws DWARFExpressionException
        """
        ...

    def getAsLocation(self, attribute: int) -> List[ghidra.app.util.bin.format.dwarf4.DWARFLocation]:
        """
        Returns the location list info specified in the attribute.
         <p>
         Numeric attributes are treated as offsets into the debug_loc section.
         <p>
         Blob attributes are treated as a single location record for the current CU, using the
         blob bytes as the DWARF expression of the location record.
         <p>
        @param attribute
        @return
        @throws IOException
        """
        ...

    @overload
    def getAttribute(self, attribute: int) -> ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue: ...

    @overload
    def getAttribute(self, attribute: int, clazz: java.lang.Class) -> object:
        """
        Finds a {@link DWARFAttributeValue attribute} with a matching {@link DWARFAttribute} type
         <p>
         Returns null if the attribute does not exist or is wrong java class type.
         <p>
         Attributes are searched for in each fragment in this aggregate, starting with the
         'head' fragment, progressing toward the 'decl' fragment.
         <p>
        @param attribute See {@link DWARFAttribute}
        @param clazz must be derived from {@link DWARFAttributeValue}
        @return
        """
        ...

    def getBool(self, attribute: int, defaultValue: bool) -> bool:
        """
        Returns the boolean value of the requested attribute, or -defaultValue- if
         the attribute is missing or not the correct type.
         <p>
        @param attribute
        @param defaultValue
        @return
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilationUnit(self) -> ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit: ...

    def getContainingTypeRef(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate:
        """
        Returns the DIE pointed to by a DW_AT_containing_type attribute.
        @return DIEA pointed to by the DW_AT_containing_type attribute, or null if not present.
        """
        ...

    def getDeclOffset(self) -> long: ...

    def getDeclParent(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...

    def getDepth(self) -> int:
        """
        Returns the depth of the head fragment, where depth is defined as
         the distance between the DIE and the root DIE of the owning compilation
         unit.
         <p>
         The root die would return 0, the children of the root will return 1, etc.
         <p>
         This value matches the nesting value shown when dumping DWARF
         info using 'readelf'.
        @return
        """
        ...

    def getFragmentCount(self) -> int: ...

    def getHeadFragment(self) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry:
        """
        Returns the first {@link DebugInfoEntry DIE} fragment, ie. the spec or abstract_origin
         DIE.
        @return
        """
        ...

    def getHexOffset(self) -> unicode:
        """
        Returns {@link #getOffset()} as a hex string.
        @return
        """
        ...

    def getHighPC(self) -> long:
        """
        Returns the value of the DW_AT_high_pc attribute, adjusted
         if necessary by the value of DW_AT_low_pc.
         <p>
        @return
        @throws IOException if the DW_AT_high_pc attribute isn't a numeric
         attribute, or if the DW_AT_low_pc value is needed and is not present.
        """
        ...

    def getLastFragment(self) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry:
        """
        Returns the last {@link DebugInfoEntry DIE} fragment, ie. the decl DIE.
        @return
        """
        ...

    def getLong(self, attribute: int, defaultValue: long) -> long:
        """
        Returns the value of the requested attribute, or -defaultValue- if the
         attribute is missing.
        @param attribute
        @param defaultValue
        @return
        """
        ...

    def getLowPC(self, defaultValue: long) -> long:
        """
        Returns the value of the DW_AT_low_pc attribute, if it exists.
        @param defaultValue
        @return
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the string value of the {@link DWARFAttribute#DW_AT_name dw_at_name} attribute,
         or null if it is missing.
         <p>
        @return
        """
        ...

    def getOffset(self) -> long: ...

    def getOffsets(self) -> List[long]: ...

    def getParent(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...

    def getProgram(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFProgram: ...

    def getRef(self, attribute: int) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...

    def getRefDIE(self, attribute: int) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry:
        """
        Returns the {@link DebugInfoEntry die} instance pointed to by the requested attribute,
         or null if the attribute does not exist.
         <p>
        @param attribute
        @return
        """
        ...

    def getString(self, attribute: int, defaultValue: unicode) -> unicode:
        """
        Returns the string value of the requested attribute, or -defaultValue- if
         the attribute is missing or not the correct type.
         <p>
        @param attribute
        @param defaultValue
        @return
        """
        ...

    def getTag(self) -> int: ...

    def getTypeRef(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...

    def getUnsignedLong(self, attribute: int, defaultValue: long) -> long:
        """
        Returns the unsigned long integer value of the requested attribute, or -defaultValue-
         if the attribute is missing.
         <p>
         The 'unsigned'ness of this method refers to how the binary value is read from
         the dwarf information (ie. a value with the high bit set is not treated as signed).
         <p>
         The -defaultValue- parameter can accept a negative value.
        @param attribute
        @param defaultValue
        @return
        """
        ...

    def hasAttribute(self, attribute: int) -> bool: ...

    def hasOffset(self, offset: long) -> bool:
        """
        Returns true if any of the {@link DebugInfoEntry DIEs} that makeup this aggregate
         have the specified offset.
        @param offset DIE offset to search for
        @return true if this {@link DIEAggregate} has a fragment DIE at that offset.
        """
        ...

    def hashCode(self) -> int: ...

    def isDanglingDeclaration(self) -> bool:
        """
        Returns true if this DIE has a DW_AT_declaration attribute and
         does NOT have a matching inbound DW_AT_specification reference.
         <p>
        @return
        """
        ...

    def isFuncDefType(self) -> bool: ...

    def isNameSpaceContainer(self) -> bool:
        """
        Returns true if the children of this DIE are within a new namespace.
         <p>
         Ie. Namespaces, subprogram, class, interface, struct, union, enum
        @return
        """
        ...

    def isNamedType(self) -> bool: ...

    def isPartialDeclaration(self) -> bool:
        """
        Returns true if this DIE has a DW_AT_declaration attribute.
        @return
        """
        ...

    def isStructureType(self) -> bool:
        """
        Returns true if this DIE defines a structure-like element (class, struct, interface, union).
        @return
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseDataMemberOffset(self, attribute: int, defaultValue: int) -> int:
        """
        Returns the unsigned integer value of the requested attribute after resolving
         any DWARF expression opcodes.
        @param attribute
        @param defaultValue
        @return
        @throws IOException
        @throws DWARFExpressionException
        """
        ...

    def parseDebugRange(self, attribute: int) -> List[ghidra.app.util.bin.format.dwarf4.DWARFRange]:
        """
        Parses a range list from the debug_ranges section.
         See DWARF4 Section 2.17.3 (Non-Contiguous Address Ranges).
         <p>
        @param attribute attribute ie. {@link DWARFAttribute#DW_AT_ranges}
        @return list of ranges
        @throws IOException if an I/O error occurs
        """
        ...

    def parseInt(self, attribute: int, defaultValue: int) -> int:
        """
        Returns the signed integer value of the requested attribute after resolving
         any DWARF expression opcodes.
         <p>
        @param attribute
        @param defaultValue
        @return
        @throws IOException
        @throws DWARFExpressionException
        """
        ...

    def parseUnsignedLong(self, attribute: int, defaultValue: long) -> long:
        """
        Returns the unsigned integer value of the requested attribute after resolving
         any DWARF expression opcodes.
         <p>
        @param attribute
        @param defaultValue
        @return
        @throws IOException
        @throws DWARFExpressionException
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
    def compilationUnit(self) -> ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit: ...

    @property
    def containingTypeRef(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...

    @property
    def danglingDeclaration(self) -> bool: ...

    @property
    def declOffset(self) -> long: ...

    @property
    def declParent(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...

    @property
    def depth(self) -> int: ...

    @property
    def fragmentCount(self) -> int: ...

    @property
    def funcDefType(self) -> bool: ...

    @property
    def headFragment(self) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry: ...

    @property
    def hexOffset(self) -> unicode: ...

    @property
    def highPC(self) -> long: ...

    @property
    def lastFragment(self) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nameSpaceContainer(self) -> bool: ...

    @property
    def namedType(self) -> bool: ...

    @property
    def offset(self) -> long: ...

    @property
    def offsets(self) -> List[long]: ...

    @property
    def parent(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...

    @property
    def partialDeclaration(self) -> bool: ...

    @property
    def program(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFProgram: ...

    @property
    def structureType(self) -> bool: ...

    @property
    def tag(self) -> int: ...

    @property
    def typeRef(self) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate: ...
