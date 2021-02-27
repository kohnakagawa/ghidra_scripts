from typing import List
import ghidra.app.util
import java.lang


class XmlProgramOptions(object):
    """
    A class to hold XML options.
    """

    ADD_2_PROG: long = 0x80000000L
    OPT_CODE: long = 0x4L
    OPT_COMMENTS: long = 0x40L
    OPT_DATA: long = 0x8L
    OPT_EMPTY_TREE_NODES: long = 0x200L
    OPT_EQUATES: long = 0x20L
    OPT_FUNCTIONS: long = 0x800L
    OPT_MEMORY_BLOCKS: long = 0x1L
    OPT_MEMORY_CONTENTS: long = 0x2L
    OPT_PROPERTIES: long = 0x80L
    OPT_REFERENCES: long = 0x400L
    OPT_SYMBOLS: long = 0x10L
    OPT_TREES: long = 0x100L
    OVERWRITE_REFS: long = 0x40000000L
    OVERWRITE_SYMBOLS: long = 0x20000000L



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOptions(self, isAddToProgram: bool) -> List[ghidra.app.util.Option]:
        """
        Returns an array of importer options representing
         the flags in this class.
        @param isAddToProgram if true then adding to existing program
        @return the array of importer options
        """
        ...

    def hashCode(self) -> int: ...

    def isBookmarks(self) -> bool:
        """
        If true, then bookmarks should be read/written.
        @return true if bookmarks should be read/written
        """
        ...

    def isComments(self) -> bool:
        """
        If true, then comments should be read/written.
        @return true if comments should be read/written
        """
        ...

    def isData(self) -> bool:
        """
        If true, then data should be read/written.
        @return true if data should be read/written
        """
        ...

    def isEntryPoints(self) -> bool:
        """
        If true, then the entry points should be read/written.
        @return true if the entry points should be read/written
        """
        ...

    def isEquates(self) -> bool:
        """
        If true, then equates should be read/written.
        @return true if equates should be read/written
        """
        ...

    def isExternalLibraries(self) -> bool:
        """
        If true, then the external libraries should be read/written.
        @return true if the external libraries should be read/written
        """
        ...

    def isFunctions(self) -> bool:
        """
        If true, then functions should be read/written.
        @return true if functions should be read/written
        """
        ...

    def isInstructions(self) -> bool:
        """
        If true, then instructions should be read/written.
        @return true if instructions should be read/written
        """
        ...

    def isMemoryBlocks(self) -> bool:
        """
        If true, then memory blocks should be read/written.
        @return true if memory blocks should be read/written
        """
        ...

    def isMemoryContents(self) -> bool:
        """
        If true, then memory contents should be read/written.
        @return true if memory contents should be read/written
        """
        ...

    def isOverwriteBookmarkConflicts(self) -> bool:
        """
        If true, then bookmark conflicts will be overwritten.
        @return true if bookmark conflicts will be overwritten
        """
        ...

    def isOverwriteDataConflicts(self) -> bool:
        """
        If true, then data conflicts will be overwritten.
        @return true if data conflicts will be overwritten
        """
        ...

    def isOverwriteMemoryConflicts(self) -> bool:
        """
        If true, then memory conflicts will be overwritten.
        @return true if memory conflicts will be overwritten
        """
        ...

    def isOverwritePropertyConflicts(self) -> bool:
        """
        If true, then property conflicts will be overwritten.
        @return true if property conflicts will be overwritten
        """
        ...

    def isOverwriteReferenceConflicts(self) -> bool:
        """
        If true, then reference conflicts will be overwritten.
        @return true if reference conflicts will be overwritten
        """
        ...

    def isOverwriteSymbolConflicts(self) -> bool:
        """
        If true, then symbol conflicts will be overwritten.
        @return true if symbol conflicts will be overwritten
        """
        ...

    def isProperties(self) -> bool:
        """
        If true, then properties should be read/written.
        @return true if properties should be read/written
        """
        ...

    def isReferences(self) -> bool:
        """
        If true, then references (memory, stack, external) should be read/written.
        @return true if references should be read/written
        """
        ...

    def isRegisters(self) -> bool:
        """
        If true, then registers should be read/written.
        @return true if registers should be read/written
        """
        ...

    def isRelocationTable(self) -> bool:
        """
        If true, then the relocation table should be read/written.
        @return true if the relocation table should be read/written
        """
        ...

    def isSymbols(self) -> bool:
        """
        If true, then symbols should be read/written.
        @return true if symbols should be read/written
        """
        ...

    def isTrees(self) -> bool:
        """
        If true, then program trees should be read/written.
        @return true if program trees should be read/written
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAddToProgram(self, addToProgram: bool) -> None: ...

    def setBookmarks(self, b: bool) -> None:
        """
        Sets bookmarks to be read/written.
        @param b true if bookmarks should read/written
        """
        ...

    def setComments(self, b: bool) -> None:
        """
        Sets comments to be read/written.
        @param b true if comments should read/written
        """
        ...

    def setData(self, b: bool) -> None:
        """
        Sets data to be read/written.
        @param b true if data should read/written
        """
        ...

    def setEntryPoints(self, b: bool) -> None:
        """
        Sets entry points to be read/written.
        @param b true if entry points should read/written
        """
        ...

    def setEquates(self, b: bool) -> None:
        """
        Sets equates to be read/written.
        @param b true if equates should read/written
        """
        ...

    def setExternalLibraries(self, b: bool) -> None:
        """
        Sets external libraries to be read/written.
        @param b true if external libraries should read/written
        """
        ...

    def setFunctions(self, b: bool) -> None:
        """
        Sets functions to be read/written.
        @param b true if functions should read/written
        """
        ...

    def setInstructions(self, b: bool) -> None:
        """
        Sets instructions to be read/written.
        @param b true if instructions should read/written
        """
        ...

    def setMemoryBlocks(self, b: bool) -> None:
        """
        Sets memory blocks to be read/written.
        @param b true if memory blocks should read/written
        """
        ...

    def setMemoryContents(self, b: bool) -> None:
        """
        Sets memory contents to be read/written.
        @param b true if memory contents should read/written
        """
        ...

    def setOptions(self, __a0: List[object]) -> None: ...

    def setOverwriteBookmarkConflicts(self, b: bool) -> None:
        """
        Sets bookmark conflicts to always be overwritten.
        @param b true if bookmark conflicts should always be overwritten
        """
        ...

    def setOverwriteDataConflicts(self, b: bool) -> None:
        """
        Sets data conflicts to always be overwritten.
        @param b true if data conflicts should always be overwritten
        """
        ...

    def setOverwriteMemoryConflicts(self, b: bool) -> None:
        """
        Sets memory conflicts to always be overwritten.
        @param b true if memory conflicts should always be overwritten
        """
        ...

    def setOverwritePropertyConflicts(self, b: bool) -> None:
        """
        Sets property conflicts to always be overwritten.
        @param b true if property conflicts should always be overwritten
        """
        ...

    def setOverwriteReferenceConflicts(self, b: bool) -> None:
        """
        Sets reference conflicts to always be overwritten.
        @param b true if reference conflicts should always be overwritten
        """
        ...

    def setOverwriteSymbolConflicts(self, b: bool) -> None:
        """
        Sets symbol conflicts to always be overwritten.
        @param b true if symbol conflicts should always be overwritten
        """
        ...

    def setProperties(self, b: bool) -> None:
        """
        Sets properties to be read/written.
        @param b true if properties should read/written
        """
        ...

    def setReferences(self, b: bool) -> None:
        """
        Sets references to be read/written.
        @param b true if references should read/written
        """
        ...

    def setRegisters(self, b: bool) -> None:
        """
        Sets registers to be read/written.
        @param b true if registers should read/written
        """
        ...

    def setRelocationTable(self, b: bool) -> None:
        """
        Sets relocation tables to be read/written.
        @param b true if relocation table should read/written
        """
        ...

    def setSymbols(self, b: bool) -> None:
        """
        Sets symbols to be read/written.
        @param b true if symbols should read/written
        """
        ...

    def setTrees(self, b: bool) -> None:
        """
        Sets program trees to be read/written.
        @param b true if program trees should read/written
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
    def addToProgram(self) -> None: ...  # No getter available.

    @addToProgram.setter
    def addToProgram(self, value: bool) -> None: ...

    @property
    def bookmarks(self) -> bool: ...

    @bookmarks.setter
    def bookmarks(self, value: bool) -> None: ...

    @property
    def comments(self) -> bool: ...

    @comments.setter
    def comments(self, value: bool) -> None: ...

    @property
    def data(self) -> bool: ...

    @data.setter
    def data(self, value: bool) -> None: ...

    @property
    def entryPoints(self) -> bool: ...

    @entryPoints.setter
    def entryPoints(self, value: bool) -> None: ...

    @property
    def equates(self) -> bool: ...

    @equates.setter
    def equates(self, value: bool) -> None: ...

    @property
    def externalLibraries(self) -> bool: ...

    @externalLibraries.setter
    def externalLibraries(self, value: bool) -> None: ...

    @property
    def functions(self) -> bool: ...

    @functions.setter
    def functions(self, value: bool) -> None: ...

    @property
    def instructions(self) -> bool: ...

    @instructions.setter
    def instructions(self, value: bool) -> None: ...

    @property
    def memoryBlocks(self) -> bool: ...

    @memoryBlocks.setter
    def memoryBlocks(self, value: bool) -> None: ...

    @property
    def memoryContents(self) -> bool: ...

    @memoryContents.setter
    def memoryContents(self, value: bool) -> None: ...

    @property
    def options(self) -> None: ...  # No getter available.

    @options.setter
    def options(self, value: List[object]) -> None: ...

    @property
    def overwriteBookmarkConflicts(self) -> bool: ...

    @overwriteBookmarkConflicts.setter
    def overwriteBookmarkConflicts(self, value: bool) -> None: ...

    @property
    def overwriteDataConflicts(self) -> bool: ...

    @overwriteDataConflicts.setter
    def overwriteDataConflicts(self, value: bool) -> None: ...

    @property
    def overwriteMemoryConflicts(self) -> bool: ...

    @overwriteMemoryConflicts.setter
    def overwriteMemoryConflicts(self, value: bool) -> None: ...

    @property
    def overwritePropertyConflicts(self) -> bool: ...

    @overwritePropertyConflicts.setter
    def overwritePropertyConflicts(self, value: bool) -> None: ...

    @property
    def overwriteReferenceConflicts(self) -> bool: ...

    @overwriteReferenceConflicts.setter
    def overwriteReferenceConflicts(self, value: bool) -> None: ...

    @property
    def overwriteSymbolConflicts(self) -> bool: ...

    @overwriteSymbolConflicts.setter
    def overwriteSymbolConflicts(self, value: bool) -> None: ...

    @property
    def properties(self) -> bool: ...

    @properties.setter
    def properties(self, value: bool) -> None: ...

    @property
    def references(self) -> bool: ...

    @references.setter
    def references(self, value: bool) -> None: ...

    @property
    def registers(self) -> bool: ...

    @registers.setter
    def registers(self, value: bool) -> None: ...

    @property
    def relocationTable(self) -> bool: ...

    @relocationTable.setter
    def relocationTable(self, value: bool) -> None: ...

    @property
    def symbols(self) -> bool: ...

    @symbols.setter
    def symbols(self, value: bool) -> None: ...

    @property
    def trees(self) -> bool: ...

    @trees.setter
    def trees(self, value: bool) -> None: ...
