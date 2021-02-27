from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.pe.debug
import ghidra.program.model.data
import java.lang


class DebugCOFFSymbol(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the COFF symbol data structure.


     typedef struct _IMAGE_SYMBOL {
         union {
             BYTE    ShortName[8];
             struct {
                 DWORD   Short;     // if 0, use LongName
                 DWORD   Long;      // offset into string table
             } Name;
             DWORD   LongName[2];    // PBYTE [2]
         } N;
         DWORD   Value;
         SHORT   SectionNumber;
         WORD    Type;
         BYTE    StorageClass;
         BYTE    NumberOfAuxSymbols;
     } IMAGE_SYMBOL;

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_SIZEOF_SYMBOL: int = 18
    IMAGE_SYM_ABSOLUTE: int = -1
    IMAGE_SYM_CLASS_ARGUMENT: int = 9
    IMAGE_SYM_CLASS_AUTOMATIC: int = 1
    IMAGE_SYM_CLASS_BIT_FIELD: int = 18
    IMAGE_SYM_CLASS_BLOCK: int = 100
    IMAGE_SYM_CLASS_END_OF_FUNCTION: int = -1
    IMAGE_SYM_CLASS_END_OF_STRUCT: int = 102
    IMAGE_SYM_CLASS_ENUM_TAG: int = 15
    IMAGE_SYM_CLASS_EXTERNAL: int = 2
    IMAGE_SYM_CLASS_EXTERNAL_DEF: int = 5
    IMAGE_SYM_CLASS_FAR_EXTERNAL: int = 68
    IMAGE_SYM_CLASS_FILE: int = 103
    IMAGE_SYM_CLASS_FUNCTION: int = 101
    IMAGE_SYM_CLASS_LABEL: int = 6
    IMAGE_SYM_CLASS_MEMBER_OF_ENUM: int = 16
    IMAGE_SYM_CLASS_MEMBER_OF_STRUCT: int = 8
    IMAGE_SYM_CLASS_MEMBER_OF_UNION: int = 11
    IMAGE_SYM_CLASS_NULL: int = 0
    IMAGE_SYM_CLASS_REGISTER: int = 4
    IMAGE_SYM_CLASS_REGISTER_PARAM: int = 17
    IMAGE_SYM_CLASS_SECTION: int = 104
    IMAGE_SYM_CLASS_STATIC: int = 3
    IMAGE_SYM_CLASS_STRUCT_TAG: int = 10
    IMAGE_SYM_CLASS_TYPE_DEFINITION: int = 13
    IMAGE_SYM_CLASS_UNDEFINED_LABEL: int = 7
    IMAGE_SYM_CLASS_UNDEFINED_STATIC: int = 14
    IMAGE_SYM_CLASS_UNION_TAG: int = 12
    IMAGE_SYM_CLASS_WEAK_EXTERNAL: int = 105
    IMAGE_SYM_DEBUG: int = -2
    IMAGE_SYM_DTYPE_ARRAY: int = 3
    IMAGE_SYM_DTYPE_FUNCTION: int = 2
    IMAGE_SYM_DTYPE_NULL: int = 0
    IMAGE_SYM_DTYPE_POINTER: int = 1
    IMAGE_SYM_TYPE_BYTE: int = 12
    IMAGE_SYM_TYPE_CHAR: int = 2
    IMAGE_SYM_TYPE_DOUBLE: int = 7
    IMAGE_SYM_TYPE_DWORD: int = 15
    IMAGE_SYM_TYPE_ENUM: int = 10
    IMAGE_SYM_TYPE_FLOAT: int = 6
    IMAGE_SYM_TYPE_INT: int = 4
    IMAGE_SYM_TYPE_LONG: int = 5
    IMAGE_SYM_TYPE_MOE: int = 11
    IMAGE_SYM_TYPE_NULL: int = 0
    IMAGE_SYM_TYPE_PCODE: int = -32768
    IMAGE_SYM_TYPE_SHORT: int = 3
    IMAGE_SYM_TYPE_STRUCT: int = 8
    IMAGE_SYM_TYPE_UINT: int = 14
    IMAGE_SYM_TYPE_UNION: int = 9
    IMAGE_SYM_TYPE_VOID: int = 1
    IMAGE_SYM_TYPE_WORD: int = 13
    IMAGE_SYM_UNDEFINED: int = 0
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @overload
    @staticmethod
    def createDebugCOFFSymbol(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int, stringTableIndex: int) -> ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbol: ...

    @overload
    @staticmethod
    def createDebugCOFFSymbol(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int, symbolTable: ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbolTable) -> ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbol: ...

    def equals(self, __a0: object) -> bool: ...

    def getAuxiliarySymbols(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbolAux]:
        """
        Returns the auxiliary symbols related to this symbol.
        @return the auxiliary symbols related to this symbol
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns the name of this symbol.
        @return the name of this symbol
        """
        ...

    def getNumberOfAuxSymbols(self) -> int:
        """
        Returns the number of auxiliary symbols defined with this symbol.
        @return the number of auxiliary symbols defined with this symbol
        """
        ...

    def getSectionNumber(self) -> int:
        """
        Returns the section number if this symbol.
        @return the section number if this symbol
        """
        ...

    def getSectionNumberAsString(self) -> unicode:
        """
        Returns a string equivalent of the section number of this symbol.
        @return a string equivalent of the section number of this symbol
        """
        ...

    def getStorageClass(self) -> int:
        """
        Returns the storage class of this symbol.
        @return the storage class of this symbol
        """
        ...

    def getStorageClassAsString(self) -> unicode:
        """
        Returns a string equivalent of the storage class of this symbol.
        @return a string equivalent of the storage class of this symbol
        """
        ...

    def getType(self) -> int:
        """
        Returns the type of this symbol.
        @return the type of this symbol
        """
        ...

    def getTypeAsString(self) -> unicode:
        """
        Returns a string equivalent of the type of this symbol.
        @return a string equivalent of the type of this symbol
        """
        ...

    def getValue(self) -> int:
        """
        Returns the value of this symbol.
        @return the value of this symbol
        """
        ...

    def getValueAsString(self) -> unicode:
        """
        Returns a string equivalent of the value of this symbol.
        @return a string equivalent of the value of this symbol
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def auxiliarySymbols(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbolAux]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def numberOfAuxSymbols(self) -> int: ...

    @property
    def sectionNumber(self) -> int: ...

    @property
    def sectionNumberAsString(self) -> unicode: ...

    @property
    def storageClass(self) -> int: ...

    @property
    def storageClassAsString(self) -> unicode: ...

    @property
    def type(self) -> int: ...

    @property
    def typeAsString(self) -> unicode: ...

    @property
    def value(self) -> int: ...

    @property
    def valueAsString(self) -> unicode: ...
