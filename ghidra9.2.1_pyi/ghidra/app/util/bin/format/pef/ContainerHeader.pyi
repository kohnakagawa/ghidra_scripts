from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pef
import ghidra.program.model.data
import java.lang


class ContainerHeader(object, ghidra.app.util.bin.StructConverter):
    """
    See Apple's -- PEFBinaryFormat.h

     struct PEFContainerHeader {
         OSType  tag1;              //Must contain 'Joy!'.
         SType   tag2;              //Must contain 'peff'.  (Yes, with two 'f's.)
         OSType  architecture;      //The ISA for code sections.  Constants in CodeFragments.h.
         UInt32  formatVersion;     //The physical format version.
         UInt32  dateTimeStamp;     //Macintosh format creation/modification stamp.
         UInt32  oldDefVersion;     //Old definition version number for the code fragment.
         UInt32  oldImpVersion;     //Old implementation version number for the code fragment.
         UInt32  currentVersion;    //Current version number for the code fragment.
         UInt16  sectionCount;      //Total number of section headers that follow.
         UInt16  instSectionCount;  //Number of instantiated sections.
         UInt32  reservedA;         //Reserved, must be written as zero
     };

    """

    ARCHITECTURE_68k: unicode = u'm68k'
    ARCHITECTURE_PPC: unicode = u'pwpc'
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    TAG1: unicode = u'Joy!'
    TAG2: unicode = u'peff'
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, provider: ghidra.app.util.bin.ByteProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getArchitecture(self) -> unicode:
        """
        Returns the architecture for this container.
         Either PowerPC CFM or CFm-68k.
        @return the architecture for this container
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentVersion(self) -> int:
        """
        Returns the current CFM version.
        @return the current CFM version
        """
        ...

    def getDateTimeStamp(self) -> int:
        """
        Returns the creation date of this PEF container.
         The stamp follows the Mac time-measurement scheme.
         That is, the number of seconds measured from Jan 1, 1904.
        @return the creation date of this PEF container
        """
        ...

    def getFormatVersion(self) -> int:
        """
        Returns the version of this PEF container.
         The current version is 1.
        @return the version of this PEF container
        """
        ...

    def getImageBase(self) -> long: ...

    def getInstantiatedSectionCount(self) -> int:
        """
        Returns the number of instantiated sections.
         Instantiated sections contain code or data that
         are required for execution.
        @return the number of instantiated sections
        """
        ...

    def getLoader(self) -> ghidra.app.util.bin.format.pef.LoaderInfoHeader: ...

    def getOldDefVersion(self) -> int:
        """
        Returns the old CFM version.
        @return the old CFM version
        """
        ...

    def getOldImpVersion(self) -> int:
        """
        Returns the old CFM implementation version.
        @return the old CFM implementation version
        """
        ...

    def getReservedA(self) -> int:
        """
        Reserved field, always returns zero (0).
        @return always returns zero (0)
        """
        ...

    def getSectionCount(self) -> int:
        """
        Returns the total sections in this container.
        @return the total sections in this container
        """
        ...

    def getSections(self) -> List[ghidra.app.util.bin.format.pef.SectionHeader]: ...

    def getTag1(self) -> unicode:
        """
        Always returns "Joy!"
        @return always returns "Joy!"
        """
        ...

    def getTag2(self) -> unicode:
        """
        Always returns "peff"
        @return always returns "peff"
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def architecture(self) -> unicode: ...

    @property
    def currentVersion(self) -> int: ...

    @property
    def dateTimeStamp(self) -> int: ...

    @property
    def formatVersion(self) -> int: ...

    @property
    def imageBase(self) -> long: ...

    @property
    def instantiatedSectionCount(self) -> int: ...

    @property
    def loader(self) -> ghidra.app.util.bin.format.pef.LoaderInfoHeader: ...

    @property
    def oldDefVersion(self) -> int: ...

    @property
    def oldImpVersion(self) -> int: ...

    @property
    def reservedA(self) -> int: ...

    @property
    def sectionCount(self) -> int: ...

    @property
    def sections(self) -> List[object]: ...

    @property
    def tag1(self) -> unicode: ...

    @property
    def tag2(self) -> unicode: ...
