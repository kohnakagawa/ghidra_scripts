from typing import List
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.debug
import java.lang


class SeparateDebugHeader(object, ghidra.app.util.bin.format.pe.OffsetValidator):
    """

     typedef struct _IMAGE_SEPARATE_DEBUG_HEADER {
         WORD        Signature;
         WORD        Flags;
         WORD        Machine;
         WORD        Characteristics;
         DWORD       TimeDateStamp;
         DWORD       CheckSum;
         DWORD       ImageBase;
         DWORD       SizeOfImage;
         DWORD       NumberOfSections;
         DWORD       ExportedNamesSize;
         DWORD       DebugDirectorySize;
         DWORD       SectionAlignment;
         DWORD       Reserved[2];
     } IMAGE_SEPARATE_DEBUG_HEADER, *PIMAGE_SEPARATE_DEBUG_HEADER;

    """

    IMAGE_SEPARATE_DEBUG_SIGNATURE: int = 18756
    IMAGE_SEPARATE_DEBUG_SIGNATURE_MAC: int = 17481



    def __init__(self, factory: generic.continues.GenericFactory, bp: ghidra.app.util.bin.ByteProvider):
        """
        Constructs a new separate debug header using the specified byte provider.
        @param bp the byte provider
        @throws IOException if an I/O error occurs.
        """
        ...



    def checkPointer(self, ptr: long) -> bool: ...

    def checkRVA(self, rva: long) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getCharacteristics(self) -> int:
        """
        Returns the characteristics.
        @return the characteristics
        """
        ...

    def getCheckSum(self) -> int:
        """
        Returns the check sum.
        @return the check sum
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugDirectorySize(self) -> int:
        """
        Returns the debug directory size.
        @return the debug directory size
        """
        ...

    def getExportedNamesSize(self) -> int:
        """
        Returns the exported names size.
        @return the exported names size
        """
        ...

    def getFlags(self) -> int:
        """
        Returns the flags.
        @return the flags
        """
        ...

    def getImageBase(self) -> int:
        """
        Returns the image base.
        @return the image base
        """
        ...

    def getMachine(self) -> int:
        """
        Returns the machine type (or processor).
        @return the machine type
        """
        ...

    def getMachineName(self) -> unicode:
        """
        Returns the machine name (or processor name).
        @return the machine name
        """
        ...

    def getNumberOfSections(self) -> int:
        """
        Returns the number of sections.
        @return the number of sections
        """
        ...

    def getParser(self) -> ghidra.app.util.bin.format.pe.debug.DebugDirectoryParser:
        """
        Returns the debug directory parser.
        @return the debug directory parser
        """
        ...

    def getReserved(self) -> List[int]:
        """
        Returns the reserved int array.
        @return the reserved int array
        """
        ...

    def getSectionAlignment(self) -> int:
        """
        Returns the section alignment value.
        @return the section alignment value
        """
        ...

    def getSignature(self) -> int:
        """
        Returns the signature (or magic number).
        @return the signature
        """
        ...

    def getSizeOfImage(self) -> int:
        """
        Returns the size of the image.
        @return the size of the image
        """
        ...

    def getTimeDateStamp(self) -> int:
        """
        Returns the time date stamp.
        @return the time date stamp
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
    def characteristics(self) -> int: ...

    @property
    def checkSum(self) -> int: ...

    @property
    def debugDirectorySize(self) -> int: ...

    @property
    def exportedNamesSize(self) -> int: ...

    @property
    def flags(self) -> int: ...

    @property
    def imageBase(self) -> int: ...

    @property
    def machine(self) -> int: ...

    @property
    def machineName(self) -> unicode: ...

    @property
    def numberOfSections(self) -> int: ...

    @property
    def parser(self) -> ghidra.app.util.bin.format.pe.debug.DebugDirectoryParser: ...

    @property
    def reserved(self) -> List[int]: ...

    @property
    def sectionAlignment(self) -> int: ...

    @property
    def signature(self) -> int: ...

    @property
    def sizeOfImage(self) -> int: ...

    @property
    def timeDateStamp(self) -> int: ...
