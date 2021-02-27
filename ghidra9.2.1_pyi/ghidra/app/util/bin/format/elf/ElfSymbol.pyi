from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import ghidra.util
import java.lang


class ElfSymbol(object, ghidra.app.util.bin.ByteArrayConverter):
    """
    A class to represent the ELF 32bit and 64bit Symbol data structures.


     typedef struct {
         Elf32_Word      st_name;     //Symbol name (string tbl index)
         Elf32_Addr      st_value;    //Symbol value
         Elf32_Word      st_size;     //Symbol size
         unsigned char   st_info;     //Symbol type and binding
         unsigned char   st_other;    //Symbol visibility
         Elf32_Section   st_shndx;    //Section index
     } Elf32_Sym;

     typedef struct {
         Elf64_Word       st_name;    //Symbol name (string tbl index)
         unsigned char    st_info;    //Symbol type and binding
         unsigned char    st_other;   //Symbol visibility
         Elf64_Section    st_shndx;   //Section index
         Elf64_Addr       st_value;   //Symbol value
         Elf64_Xword      st_size;    //Symbol size
     } Elf64_Sym;


    """

    STB_GLOBAL: int = 1
    STB_GNU_UNIQUE: int = 10
    STB_LOCAL: int = 0
    STB_WEAK: int = 2
    STT_COMMON: int = 5
    STT_FILE: int = 4
    STT_FUNC: int = 2
    STT_NOTYPE: int = 0
    STT_OBJECT: int = 1
    STT_RELC: int = 8
    STT_SECTION: int = 3
    STT_SRELC: int = 9
    STT_TLS: int = 6
    STV_DEFAULT: int = 0
    STV_HIDDEN: int = 2
    STV_INTERNAL: int = 1
    STV_PROTECTED: int = 3



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createElfSymbol(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, symbolIndex: int, symbolTable: ghidra.app.util.bin.format.elf.ElfSymbolTable, stringTable: ghidra.app.util.bin.format.elf.ElfStringTable, header: ghidra.app.util.bin.format.elf.ElfHeader) -> ghidra.app.util.bin.format.elf.ElfSymbol: ...

    @staticmethod
    def createGlobalFunctionSymbol(header: ghidra.app.util.bin.format.elf.ElfHeader, name: int, nameAsString: unicode, addr: long, symbolIndex: int, symbolTable: ghidra.app.util.bin.format.elf.ElfSymbolTable) -> ghidra.app.util.bin.format.elf.ElfSymbol:
        """
        Creates a new global function symbol.
        @param header the corresponding ELF header
        @param name the byte index of the name
        @param nameAsString the string name of the section
        @param addr the address of the function
        @param symbolIndex index of symbol within corresponding symbol table
        @param symbolTable symbol table
        @return the new global function symbol
        """
        ...

    @staticmethod
    def createSectionSymbol32(header: ghidra.app.util.bin.format.elf.ElfHeader, sectionAddress: long, sectionHeaderIndex: int, name: unicode, symbolIndex: int, symbolTable: ghidra.app.util.bin.format.elf.ElfSymbolTable) -> ghidra.app.util.bin.format.elf.ElfSymbol:
        """
        Creates a new section symbol.
        @param header the corresponding ELF header
        @param sectionAddress the start address of the section
        @param sectionHeaderIndex the index of the section in the section header table
        @param name the string name of the section
        @param symbolIndex index of symbol within corresponding symbol table
        @param symbolTable symbol table
        @return the new section symbol
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getBind(self) -> int:
        """
        Returns the symbol's binding. For example, global.
        @return the symbol's binding
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getInfo(self) -> int:
        """
        This member specifies the symbol's type and binding attributes.
        @return the symbol's type and binding attributes
        """
        ...

    def getName(self) -> int:
        """
        This member holds an index into the object file's symbol
         string table, which holds the character representations
         of the symbol names. If the value is non-zero, it represents a
         string table index that gives the symbol name.
         Otherwise, the symbol table entry has no name.
        @return the index to the symbol's name
        """
        ...

    def getNameAsString(self) -> unicode:
        """
        Returns the actual string name for this symbol. The symbol only
         stores an byte index into the string table where
         the name string is located.
        @return the actual string name for this symbol
        """
        ...

    def getOther(self) -> int:
        """
        This member currently holds 0 and has no defined meaning.
        @return no defined meaning
        """
        ...

    def getSectionHeaderIndex(self) -> int:
        """
        Every symbol table entry is "defined" in relation to some section;
         this member holds the relevant section header table index.
        @return the relevant section header table index
        """
        ...

    def getSize(self) -> long:
        """
        Many symbols have associated sizes. For example, a data object's size is the number of
         bytes contained in the object. This member holds 0 if the symbol has no size or an
         unknown size.
        @return the symbol's size
        """
        ...

    def getSymbolTable(self) -> ghidra.app.util.bin.format.elf.ElfSymbolTable:
        """
        Get the symbol table containing this symbol
        @return symbol table
        """
        ...

    def getSymbolTableIndex(self) -> int:
        """
        Get the index of this symbol within the corresponding symbol table.
        @return index of this symbol within the corresponding symbol table
        """
        ...

    def getType(self) -> int:
        """
        Returns the symbol's binding. For example, section.
        @return the symbol's binding
        """
        ...

    def getValue(self) -> long:
        """
        This member gives the value of the associated symbol.
         Depending on the context, this may be an absolute value,
         an address, etc.
        @return the symbol's value
        """
        ...

    def getVisibility(self) -> int:
        """
        Returns the symbol's visibility. For example, default.
        @return the symbol's visibility
        """
        ...

    def hashCode(self) -> int: ...

    def isAbsolute(self) -> bool:
        """
        Returns true if the symbol has an absolute
         value that will not change because of relocation.
        @return true if the symbol value will not change due to relocation
        """
        ...

    def isCommon(self) -> bool:
        """
        The symbol labels a common block that has not yet been allocated. The symbol's value
         gives alignment constraints, similar to a section's sh_addralign member. That is, the
         link editor will allocate the storage for the symbol at an address that is a multiple of
         st_value. The symbol's size tells how many bytes are required.
        @return true if this is a common symbol
        """
        ...

    def isExternal(self) -> bool:
        """
        Returns true if this is an external symbol.
         A symbol is considered external if it's
         binding is global and it's size is zero.
        @return true if this is an external symbol
        """
        ...

    def isFile(self) -> bool:
        """
        Returns true if this symbol defines a file.
        @return true if this symbol defines a file
        """
        ...

    def isFunction(self) -> bool:
        """
        Returns true if this symbol defines a function.
        @return true if this symbol defines a function
        """
        ...

    def isGlobal(self) -> bool:
        """
        Returns true if this symbol is global.
         Global symbols are visible to all object files
         being combined. One object file's definition
         of a global symbol will satisfy another
         file's undefined reference to the same
         global symbol.
        @return true if this symbol is global
        """
        ...

    def isLocal(self) -> bool:
        """
        Returns true if this symbol is local.
         Local symbols are not visible outside the object file
         containing their definition. Local symbols of the same
         name may exist in multiple files without colliding.
        @return true if this symbol is local
        """
        ...

    def isNoType(self) -> bool:
        """
        Returns true if this symbol's type is not specified.
        @return true if this symbol's type is not specified
        """
        ...

    def isObject(self) -> bool:
        """
        Returns true if this symbol defines an object.
        @return true if this symbol defines an object
        """
        ...

    def isSection(self) -> bool:
        """
        Returns true if this symbol defines a section.
        @return true if this symbol defines a section
        """
        ...

    def isTLS(self) -> bool:
        """
        Returns true if this symbol defines a thread-local symbol.
        @return true if this symbol defines a thread-local symbol
        """
        ...

    def isWeak(self) -> bool:
        """
        Returns true if this symbol is weak.
         Weak symbols resemble global symbols,
         but their definitions have lower precedence.
        @return true if this symbol is weak
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setValue(self, value: long) -> None:
        """
        Sets the value of this symbol. The value is generally an address.
        @param value the new value of the symbol
        """
        ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]:
        """
        @see ghidra.app.util.bin.ByteArrayConverter#toBytes(ghidra.util.DataConverter)
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def TLS(self) -> bool: ...

    @property
    def absolute(self) -> bool: ...

    @property
    def bind(self) -> int: ...

    @property
    def common(self) -> bool: ...

    @property
    def external(self) -> bool: ...

    @property
    def file(self) -> bool: ...

    @property
    def function(self) -> bool: ...

    @property
    def global(self) -> bool: ...

    @property
    def info(self) -> int: ...

    @property
    def local(self) -> bool: ...

    @property
    def name(self) -> int: ...

    @property
    def nameAsString(self) -> unicode: ...

    @property
    def noType(self) -> bool: ...

    @property
    def object(self) -> bool: ...

    @property
    def other(self) -> int: ...

    @property
    def section(self) -> bool: ...

    @property
    def sectionHeaderIndex(self) -> int: ...

    @property
    def size(self) -> long: ...

    @property
    def symbolTable(self) -> ghidra.app.util.bin.format.elf.ElfSymbolTable: ...

    @property
    def symbolTableIndex(self) -> int: ...

    @property
    def type(self) -> int: ...

    @property
    def value(self) -> long: ...

    @value.setter
    def value(self, value: long) -> None: ...

    @property
    def visibility(self) -> int: ...

    @property
    def weak(self) -> bool: ...
