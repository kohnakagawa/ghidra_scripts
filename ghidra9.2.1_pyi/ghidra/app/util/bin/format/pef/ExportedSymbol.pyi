import ghidra.app.util.bin.format.pef
import ghidra.program.model.data
import java.lang


class ExportedSymbol(ghidra.app.util.bin.format.pef.AbstractSymbol):
    """
    See Apple's -- PEFBinaryFormat.h

     struct PEFExportedSymbol { //! This structure is 10 bytes long and arrays are packed.
         UInt32  classAndName;  //A combination of class and name offset.
         UInt32  symbolValue;   //Typically the symbol's offset within a section.
         SInt16  sectionIndex;  //The index of the section, or pseudo-section, for the symbol.
     };

    """

    kPEFAbsoluteExport: int = -2
    kPEFExpSymClassShift: int = 24
    kPEFReexportedImport: int = -3







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getNameOffset(self) -> int:
        """
        Returns offset of symbol name in loader string table.
        @return offset of symbol name in loader string table
        """
        ...

    def getSectionIndex(self) -> int:
        """
        Returns the index of the section, or pseudo-section, for the symbol.
        @return the index of the section, or pseudo-section, for the symbol
        """
        ...

    def getSymbolClass(self) -> ghidra.app.util.bin.format.pef.SymbolClass: ...

    def getSymbolValue(self) -> int:
        """
        Typically the symbol's offset within a section.
        @return the symbol's offset within a section
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
    def name(self) -> unicode: ...

    @property
    def nameOffset(self) -> int: ...

    @property
    def sectionIndex(self) -> int: ...

    @property
    def symbolClass(self) -> ghidra.app.util.bin.format.pef.SymbolClass: ...

    @property
    def symbolValue(self) -> int: ...
