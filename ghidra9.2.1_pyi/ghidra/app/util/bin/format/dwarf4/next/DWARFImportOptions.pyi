import java.lang


class DWARFImportOptions(object):
    """
    Import options exposed by the DWARFAnalyzer
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getImportLimitDIECount(self) -> int:
        """
        Option to skip DWARF import if the DWARF record count is too large.
        @return integer count of the max number of DWARF records that will be attempted to import.
        """
        ...

    def getNameLengthCutoff(self) -> int:
        """
        Option to control how long DWARF symbol names are allowed to be before being truncated.
        @return integer max length of symbol names from DWARF.
        """
        ...

    def hashCode(self) -> int: ...

    def isCopyRenameAnonTypes(self) -> bool:
        """
        Option to control a feature that copies anonymous types into a structure's "namespace"
         CategoryPath and giving that anonymous type a new name based on the structure's field's
         name.
        @return boolean flag.
        """
        ...

    def isCreateFuncSignatures(self) -> bool:
        """
        Option to control creating FunctionSignature datatypes for each function defintion
         found in the DWARF debug data.
        @return boolean flag.
        """
        ...

    def isElideTypedefsWithSameName(self) -> bool:
        """
        Option to control eliding typedef creation if the dest type has the same name.
        @return boolean true if the DWARF importer should skip creating a typedef if its
         dest has the same name.
        """
        ...

    def isImportDataTypes(self) -> bool:
        """
        Option to turn on/off the import of data types.
        @return boolean true if import should import data types.
        """
        ...

    def isImportFuncs(self) -> bool:
        """
        Option to turn on/off the import of funcs.
        @return boolean true if import should import funcs.
        """
        ...

    def isOrganizeTypesBySourceFile(self) -> bool:
        """
        Option to organize imported datatypes into sub-folders based on their source file name.
        @return boolean flag
        """
        ...

    def isOutputDIEInfo(self) -> bool:
        """
        Option to control tagging data types and functions with their DWARF DIE
         record number.
        @return boolean true if the DWARF importer should tag items with their DIE record
         number.
        """
        ...

    def isOutputInlineFuncComments(self) -> bool:
        """
        Option to control tagging inlined-functions with comments.
        @return boolean flag.
        """
        ...

    def isOutputLexicalBlockComments(self) -> bool:
        """
        Option to control tagging lexical blocks with Ghidra comments.
        @return boolean flag.
        """
        ...

    def isOutputSourceLocationInfo(self) -> bool:
        """
        Option to control tagging data types and functions with their source code
         location (ie. filename : line number ) if the information is present in the DWARF record.
        @return boolean true if the DWARF importer should tag items with their source code location
         info.
        """
        ...

    def isPreloadAllDIEs(self) -> bool:
        """
        Option to cause the DWARF parser to load all DWARF records into memory, instead of
         processing one compile unit at a time.  Needed to handle binaries created by some
         toolchains.  The import pre-check will warn the user if this needs to be turned on.
        @return boolean flag
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCopyRenameAnonTypes(self, b: bool) -> None:
        """
        Option to control a feature that copies anonymous types into a structure's "namespace"
         CategoryPath and giving that anonymous type a new name based on the structure's field's
         name.
        @param b boolean flag to set.
        """
        ...

    def setCreateFuncSignatures(self, createFuncSignatures: bool) -> None:
        """
        Option to control creating FunctionSignature datatypes for each function defintion
         found in the DWARF debug data.
        @param createFuncSignatures boolean flag to set.
        """
        ...

    def setElideTypedefsWithSameName(self, elide_typedefs_with_same_name: bool) -> None:
        """
        Option to control eliding typedef creation if the dest type has the same name.
        @param elide_typedefs_with_same_name boolean to set
        """
        ...

    def setImportDataTypes(self, importDataTypes: bool) -> None:
        """
        Option to turn on/off the import of data types.
        @param importDataTypes boolean to set
        """
        ...

    def setImportFuncs(self, output_Funcs: bool) -> None: ...

    def setImportLimitDIECount(self, import_limit_die_count: int) -> None:
        """
        Option to skip DWARF import if the DWARF record count is too large.
        @param import_limit_die_count integer record count
        """
        ...

    def setNameLengthCutoff(self, name_length_cutoff: int) -> None:
        """
        Option to control how long DWARF symbol names are allowed to be before being truncated.
        @param name_length_cutoff integer max length.
        """
        ...

    def setOrganizeTypesBySourceFile(self, organizeTypesBySourceFile: bool) -> None:
        """
        Option to organize imported datatypes into sub-folders based on their source file name.
        @param organizeTypesBySourceFile boolean flag to set.
        """
        ...

    def setOutputDIEInfo(self, output_DWARF_die_info: bool) -> None:
        """
        Option to control tagging data types and functions with their DWARF DIE
         record number.
        @param output_DWARF_die_info boolean to set
        """
        ...

    def setOutputInlineFuncComments(self, output_InlineFunc_comments: bool) -> None: ...

    def setOutputLexicalBlockComments(self, output_LexicalBlock_comments: bool) -> None:
        """
        Option to control tagging lexical blocks with Ghidra comments.
        @param output_LexicalBlock_comments boolean flag to set.
        """
        ...

    def setOutputSourceLocationInfo(self, output_DWARF_location_info: bool) -> None:
        """
        Option to control tagging data types and functions with their source code
         location (ie. filename : line number ) if the information is present in the DWARF record.
        @param output_DWARF_location_info boolean to set
        """
        ...

    def setPreloadAllDIEs(self, b: bool) -> None:
        """
        Option to cause the DWARF parser to load all DWARF records into memory, instead of
         processing one compile unit at a time.  Needed to handle binaries created by some
         toolchains.  The import pre-check will warn the user if this needs to be turned on.
        @param b boolean flag to set
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
    def copyRenameAnonTypes(self) -> bool: ...

    @copyRenameAnonTypes.setter
    def copyRenameAnonTypes(self, value: bool) -> None: ...

    @property
    def createFuncSignatures(self) -> bool: ...

    @createFuncSignatures.setter
    def createFuncSignatures(self, value: bool) -> None: ...

    @property
    def elideTypedefsWithSameName(self) -> bool: ...

    @elideTypedefsWithSameName.setter
    def elideTypedefsWithSameName(self, value: bool) -> None: ...

    @property
    def importDataTypes(self) -> bool: ...

    @importDataTypes.setter
    def importDataTypes(self, value: bool) -> None: ...

    @property
    def importFuncs(self) -> bool: ...

    @importFuncs.setter
    def importFuncs(self, value: bool) -> None: ...

    @property
    def importLimitDIECount(self) -> int: ...

    @importLimitDIECount.setter
    def importLimitDIECount(self, value: int) -> None: ...

    @property
    def nameLengthCutoff(self) -> int: ...

    @nameLengthCutoff.setter
    def nameLengthCutoff(self, value: int) -> None: ...

    @property
    def organizeTypesBySourceFile(self) -> bool: ...

    @organizeTypesBySourceFile.setter
    def organizeTypesBySourceFile(self, value: bool) -> None: ...

    @property
    def outputDIEInfo(self) -> bool: ...

    @outputDIEInfo.setter
    def outputDIEInfo(self, value: bool) -> None: ...

    @property
    def outputInlineFuncComments(self) -> bool: ...

    @outputInlineFuncComments.setter
    def outputInlineFuncComments(self, value: bool) -> None: ...

    @property
    def outputLexicalBlockComments(self) -> bool: ...

    @outputLexicalBlockComments.setter
    def outputLexicalBlockComments(self, value: bool) -> None: ...

    @property
    def outputSourceLocationInfo(self) -> bool: ...

    @outputSourceLocationInfo.setter
    def outputSourceLocationInfo(self, value: bool) -> None: ...

    @property
    def preloadAllDIEs(self) -> bool: ...

    @preloadAllDIEs.setter
    def preloadAllDIEs(self, value: bool) -> None: ...
