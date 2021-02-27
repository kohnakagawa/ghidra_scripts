from typing import List
import ghidra.app.util.bin.format.pe.debug
import java.lang


class DebugCOFFSymbolsHeader(object):
    """
    A class to represent the COFF Symbols Header.


     typedef struct _IMAGE_COFF_SYMBOLS_HEADER {
       DWORD   NumberOfSymbols;
       DWORD   LvaToFirstSymbol;
       DWORD   NumberOfLinenumbers;
       DWORD   LvaToFirstLinenumber;
       DWORD   RvaToFirstByteOfCode;
       DWORD   RvaToLastByteOfCode;
       DWORD   RvaToFirstByteOfData;
       DWORD   RvaToLastByteOfData;
     } IMAGE_COFF_SYMBOLS_HEADER, *PIMAGE_COFF_SYMBOLS_HEADER;

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstByteOfCodeRVA(self) -> int:
        """
        Returns the RVA of the first code byte.
        @return the RVA of the first code byte
        """
        ...

    def getFirstByteOfDataRVA(self) -> int:
        """
        Returns the RVA of the first data byte.
        @return the RVA of the first data byte
        """
        ...

    def getFirstLinenumberLVA(self) -> int:
        """
        Returns the LVA of the first line number.
        @return the LVA of the first line number
        """
        ...

    def getFirstSymbolLVA(self) -> int:
        """
        Returns the LVA of the first symbol.
        @return the LVA of the first symbol
        """
        ...

    def getLastByteOfCodeRVA(self) -> int:
        """
        Returns the RVA of the last code byte.
        @return the RVA of the last code byte
        """
        ...

    def getLastByteOfDataRVA(self) -> int:
        """
        Returns the RVA of the last data byte.
        @return the RVA of the last data byte
        """
        ...

    def getLineNumbers(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugCOFFLineNumber]:
        """
        Returns the COFF line numbers.
        @return the COFF line numbers
        """
        ...

    def getNumberOfLinenumbers(self) -> int:
        """
        Returns the number of line numbers in this header.
        @return the number of line numbers in this header
        """
        ...

    def getNumberOfSymbols(self) -> int:
        """
        Returns the number of symbols in this header.
        @return the number of symbols in this header
        """
        ...

    def getSymbolTable(self) -> ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbolTable:
        """
        Returns the COFF symbol table.
        @return the COFF symbol table
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
    def firstByteOfCodeRVA(self) -> int: ...

    @property
    def firstByteOfDataRVA(self) -> int: ...

    @property
    def firstLinenumberLVA(self) -> int: ...

    @property
    def firstSymbolLVA(self) -> int: ...

    @property
    def lastByteOfCodeRVA(self) -> int: ...

    @property
    def lastByteOfDataRVA(self) -> int: ...

    @property
    def lineNumbers(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugCOFFLineNumber]: ...

    @property
    def numberOfLinenumbers(self) -> int: ...

    @property
    def numberOfSymbols(self) -> int: ...

    @property
    def symbolTable(self) -> ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbolTable: ...
