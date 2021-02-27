import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class DebugCOFFSymbolAux(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the COFF Auxiliary Symbol data structure.


     typedef union _IMAGE_AUX_SYMBOL {
         struct {
             DWORD    TagIndex;                      // struct, union, or enum tag index
             union {
                 struct {
                     WORD    Linenumber;             // declaration line number
                     WORD    Size;                   // size of struct, union, or enum
                 } LnSz;
                DWORD    TotalSize;
             }Misc;
             union {
                 struct {                            // if ISFCN, tag, or .bb
                     DWORD    PointerToLinenumber;
                     DWORD    PointerToNextFunction;
                 } Function;
                 struct {                            // if ISARY, up to 4 dimen.
                     WORD     Dimension[4];
                 } Array;
             } FcnAry;
             WORD    TvIndex;                        // tv index
         } Sym;
         struct {
             BYTE    Name[IMAGE_SIZEOF_SYMBOL];
         } File;
         struct {
             DWORD   Length;                         // section length
             WORD    NumberOfRelocations;            // number of relocation entries
             WORD    NumberOfLinenumbers;            // number of line numbers
             DWORD   CheckSum;                       // checksum for communal
             SHORT   Number;                         // section number to associate with
             BYTE    Selection;                      // communal selection type
         } Section;
     } IMAGE_AUX_SYMBOL;

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_SIZEOF_AUX_SYMBOL: int = 18
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



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

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
