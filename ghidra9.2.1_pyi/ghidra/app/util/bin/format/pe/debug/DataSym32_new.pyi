import ghidra.app.util.bin.format.pe.debug
import java.lang


class DataSym32_new(ghidra.app.util.bin.format.pe.debug.DebugSymbol):
    """

     typedef struct DATASYM32_NEW {
         unsigned short  reclen;         // Record length
         unsigned short  rectyp;         // S_LDATA32, S_GDATA32 or S_PUB32
         CVTYPEINDEX     typind;
         unsigned long   off;
         unsigned short  seg;
         unsigned char   name[1];        // Length-prefixed name
     } DATASYM32_NEW;

    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int:
        """
        Returns the length of the symbol.
        @return the length of the symbol
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the symbol.
        @return the name of the symbol
        """
        ...

    def getOffset(self) -> int:
        """
        Returns the offset.
        @return the offset
        """
        ...

    def getSection(self) -> int:
        """
        Returns the section number.
        @return the section number
        """
        ...

    def getType(self) -> int:
        """
        Returns the type of the symbol.
        @return the type of the symbol
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
