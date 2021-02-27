from typing import List
import ghidra.app.util
import ghidra.app.util.bin
import ghidra.app.util.importer
import ghidra.app.util.opinion
import ghidra.framework.model
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util


class ElfLoader(ghidra.app.util.opinion.AbstractLibrarySupportLoader):
    """
    A Loader for processing executable and linking files (ELF).
    """

    ELF_ENTRY_FUNCTION_NAME: unicode = u'entry'
    ELF_FILE_TYPE_PROPERTY: unicode = u'ELF File Type'
    ELF_NAME: unicode = u'Executable and Linking Format (ELF)'
    ELF_ORIGINAL_IMAGE_BASE_PROPERTY: unicode = u'ELF Original Image Base'
    ELF_PRELINKED_PROPERTY: unicode = u'ELF Prelinked'
    ELF_REQUIRED_LIBRARY_PROPERTY_PREFIX: unicode = u'ELF Required Library ['
    ELF_SOURCE_FILE_PROPERTY_PREFIX: unicode = u'ELF Source File ['



    def __init__(self): ...



    @overload
    def compareTo(self, __a0: ghidra.app.util.opinion.Loader) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def findSupportedLoadSpecs(self, provider: ghidra.app.util.bin.ByteProvider) -> java.util.Collection: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultOptions(self, provider: ghidra.app.util.bin.ByteProvider, loadSpec: ghidra.app.util.opinion.LoadSpec, domainObject: ghidra.framework.model.DomainObject, loadIntoProgram: bool) -> List[ghidra.app.util.Option]: ...

    @staticmethod
    def getElfOriginalImageBase(program: ghidra.program.model.listing.Program) -> long:
        """
        Getter for the {@link #ELF_ORIGINAL_IMAGE_BASE_PROPERTY} property.
        @param program Ghidra program that has the property to get
        @return Long value of the original image base, or null if the property is not present
        """
        ...

    def getName(self) -> unicode: ...

    def getPreferredFileName(self, __a0: ghidra.app.util.bin.ByteProvider) -> unicode: ...

    def getTier(self) -> ghidra.app.util.opinion.LoaderTier: ...

    def getTierPriority(self) -> int: ...

    def hashCode(self) -> int: ...

    @overload
    def load(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: ghidra.app.util.opinion.LoadSpec, __a2: List[object], __a3: ghidra.program.model.listing.Program, __a4: ghidra.util.task.TaskMonitor, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @overload
    def load(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: unicode, __a2: ghidra.framework.model.DomainFolder, __a3: ghidra.app.util.opinion.LoadSpec, __a4: List[object], __a5: ghidra.app.util.importer.MessageLog, __a6: object, __a7: ghidra.util.task.TaskMonitor) -> List[object]: ...

    def loadInto(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: ghidra.app.util.opinion.LoadSpec, __a2: List[object], __a3: ghidra.app.util.importer.MessageLog, __a4: ghidra.program.model.listing.Program, __a5: ghidra.util.task.TaskMonitor) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def supportsLoadIntoProgram(self) -> bool: ...

    def toString(self) -> unicode: ...

    def validateOptions(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: ghidra.app.util.opinion.LoadSpec, __a2: List[object], __a3: ghidra.program.model.listing.Program) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...
