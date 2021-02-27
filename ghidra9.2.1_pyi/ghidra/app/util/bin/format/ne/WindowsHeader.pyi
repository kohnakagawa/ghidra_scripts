import ghidra.app.util.bin.format.ne
import java.lang


class WindowsHeader(object):
    """
    A class to represent and parse the
     Windows new-style executable (NE) header.
    """

    IMAGE_NE_SIGNATURE: int = 17742



    def __init__(self, reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, baseAddr: ghidra.program.model.address.SegmentedAddress, index: int):
        """
        Constructor
        @param reader the binary reader
        @param baseAddr the image base address
        @param index the index where the windows headers begins
        @throws InvalidWindowsHeaderException if the bytes defined in the binary reader at
         the specified index do not constitute a valid windows header.
        @throws IOException for problems reading the header bytes
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntryTable(self) -> ghidra.app.util.bin.format.ne.EntryTable:
        """
        Returns the entry table.
        @return the entry table
        """
        ...

    def getImportedNameTable(self) -> ghidra.app.util.bin.format.ne.ImportedNameTable:
        """
        Returns the imported name table.
        @return the imported name table
        """
        ...

    def getInformationBlock(self) -> ghidra.app.util.bin.format.ne.InformationBlock:
        """
        Returns the information block.
        @return the information block
        """
        ...

    def getModuleReferenceTable(self) -> ghidra.app.util.bin.format.ne.ModuleReferenceTable:
        """
        Returns the module reference table.
        @return the module reference table
        """
        ...

    def getNonResidentNameTable(self) -> ghidra.app.util.bin.format.ne.NonResidentNameTable:
        """
        Returns the non-resident name table.
        @return the non-resident name table
        """
        ...

    def getProcessorName(self) -> unicode:
        """
        Returns the processor name.
        @return the processor name
        """
        ...

    def getResidentNameTable(self) -> ghidra.app.util.bin.format.ne.ResidentNameTable:
        """
        Returns the resident name table.
        @return the resident name table
        """
        ...

    def getResourceTable(self) -> ghidra.app.util.bin.format.ne.ResourceTable:
        """
        Returns the resource table.
        @return the resource table
        """
        ...

    def getSegmentTable(self) -> ghidra.app.util.bin.format.ne.SegmentTable:
        """
        Returns the segment table.
        @return the segment table
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
    def entryTable(self) -> ghidra.app.util.bin.format.ne.EntryTable: ...

    @property
    def importedNameTable(self) -> ghidra.app.util.bin.format.ne.ImportedNameTable: ...

    @property
    def informationBlock(self) -> ghidra.app.util.bin.format.ne.InformationBlock: ...

    @property
    def moduleReferenceTable(self) -> ghidra.app.util.bin.format.ne.ModuleReferenceTable: ...

    @property
    def nonResidentNameTable(self) -> ghidra.app.util.bin.format.ne.NonResidentNameTable: ...

    @property
    def processorName(self) -> unicode: ...

    @property
    def residentNameTable(self) -> ghidra.app.util.bin.format.ne.ResidentNameTable: ...

    @property
    def resourceTable(self) -> ghidra.app.util.bin.format.ne.ResourceTable: ...

    @property
    def segmentTable(self) -> ghidra.app.util.bin.format.ne.SegmentTable: ...
