from typing import List
import generic.jar
import ghidra.program.model.lang
import java.lang
import java.util


class SleighLanguageDescription(ghidra.program.model.lang.BasicLanguageDescription):
    """
    Class for holding Language identifiers
    """





    def __init__(self, __a0: ghidra.program.model.lang.LanguageID, __a1: unicode, __a2: ghidra.program.model.lang.Processor, __a3: ghidra.program.model.lang.Endian, __a4: ghidra.program.model.lang.Endian, __a5: int, __a6: unicode, __a7: int, __a8: int, __a9: bool, __a10: java.util.Map, __a11: List[object], __a12: java.util.Map): ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompatibleCompilerSpecDescriptions(self) -> List[ghidra.program.model.lang.CompilerSpecDescription]: ...

    def getCompilerSpecDescriptionByID(self, compilerSpecID: ghidra.program.model.lang.CompilerSpecID) -> ghidra.program.model.lang.CompilerSpecDescription: ...

    def getDefsFile(self) -> generic.jar.ResourceFile:
        """
        Get the specification file (if it exists)
        @return specification file
        """
        ...

    def getDescription(self) -> unicode: ...

    def getEndian(self) -> ghidra.program.model.lang.Endian: ...

    def getExternalNames(self, key: unicode) -> List[unicode]: ...

    def getInstructionEndian(self) -> ghidra.program.model.lang.Endian: ...

    def getLanguageID(self) -> ghidra.program.model.lang.LanguageID: ...

    def getManualIndexFile(self) -> generic.jar.ResourceFile: ...

    def getMinorVersion(self) -> int: ...

    def getProcessor(self) -> ghidra.program.model.lang.Processor: ...

    def getSize(self) -> int: ...

    def getSlaFile(self) -> generic.jar.ResourceFile:
        """
        @return
        """
        ...

    def getSpecFile(self) -> generic.jar.ResourceFile:
        """
        Get the specification file (if it exists)
        @return specification file
        """
        ...

    def getTruncatedSpaceNames(self) -> java.util.Set:
        """
        @return set of address space names which have been identified for truncation
        """
        ...

    def getTruncatedSpaceSize(self, spaceName: unicode) -> int:
        """
        Get the truncated space size for the specified address space
        @param spaceName address space name
        @return truncated space size in bytes
        @throws NoSuchElementException
        """
        ...

    def getVariant(self) -> unicode: ...

    def getVersion(self) -> int: ...

    def hashCode(self) -> int: ...

    def isDeprecated(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDefsFile(self, defsFile: generic.jar.ResourceFile) -> None:
        """
        Set the (optional) specification file associated with this language
        @param defsFile the specFile to associate with this description.
        """
        ...

    def setManualIndexFile(self, manualIndexFile: generic.jar.ResourceFile) -> None: ...

    def setSlaFile(self, slaFile: generic.jar.ResourceFile) -> None:
        """
        @param slaFile
        """
        ...

    def setSpecFile(self, specFile: generic.jar.ResourceFile) -> None:
        """
        Set the (optional) specification file associated with this language
        @param specFile the specFile to associate with this description.
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
    def defsFile(self) -> generic.jar.ResourceFile: ...

    @defsFile.setter
    def defsFile(self, value: generic.jar.ResourceFile) -> None: ...

    @property
    def manualIndexFile(self) -> generic.jar.ResourceFile: ...

    @manualIndexFile.setter
    def manualIndexFile(self, value: generic.jar.ResourceFile) -> None: ...

    @property
    def slaFile(self) -> generic.jar.ResourceFile: ...

    @slaFile.setter
    def slaFile(self, value: generic.jar.ResourceFile) -> None: ...

    @property
    def specFile(self) -> generic.jar.ResourceFile: ...

    @specFile.setter
    def specFile(self, value: generic.jar.ResourceFile) -> None: ...

    @property
    def truncatedSpaceNames(self) -> java.util.Set: ...
