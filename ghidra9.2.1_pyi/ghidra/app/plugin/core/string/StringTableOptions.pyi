import ghidra.app.plugin.core.string
import ghidra.program.model.address
import java.lang


class StringTableOptions(object):




    def __init__(self): ...



    def copy(self) -> ghidra.app.plugin.core.string.StringTableOptions: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getAlignment(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getIncludeAllCharSizes(self) -> bool: ...

    def getMinStringSize(self) -> int: ...

    def getWordModelFile(self) -> unicode: ...

    def getWordModelInitialized(self) -> bool: ...

    def hashCode(self) -> int: ...

    def includeConflictingStrings(self) -> bool: ...

    def includeDefinedStrings(self) -> bool: ...

    def includePartiallyDefinedStrings(self) -> bool: ...

    def includeUndefinedStrings(self) -> bool: ...

    def isNullTerminationRequired(self) -> bool: ...

    def isPascalRequired(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def onlyShowWordStrings(self) -> bool: ...

    def setAddressSet(self, __a0: ghidra.program.model.address.AddressSetView) -> None: ...

    def setAlignment(self, __a0: int) -> None: ...

    def setIncludeAllCharSizes(self, __a0: bool) -> None: ...

    def setIncludeConflictingStrings(self, __a0: bool) -> None: ...

    def setIncludeDefinedStrings(self, __a0: bool) -> None: ...

    def setIncludePartiallyDefinedStrings(self, __a0: bool) -> None: ...

    def setIncludeUndefinedStrings(self, __a0: bool) -> None: ...

    def setMinStringSize(self, __a0: int) -> None: ...

    def setNullTerminationRequired(self, __a0: bool) -> None: ...

    def setOnlyShowWordStrings(self, __a0: bool) -> None: ...

    def setRequirePascal(self, __a0: bool) -> None: ...

    def setUseLoadedBlocksOnly(self, __a0: bool) -> None: ...

    def setWordModelFile(self, __a0: unicode) -> None: ...

    def setWordModelInitialized(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    def useLoadedBlocksOnly(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @addressSet.setter
    def addressSet(self, value: ghidra.program.model.address.AddressSetView) -> None: ...

    @property
    def alignment(self) -> int: ...

    @alignment.setter
    def alignment(self, value: int) -> None: ...

    @property
    def includeAllCharSizes(self) -> bool: ...

    @includeAllCharSizes.setter
    def includeAllCharSizes(self, value: bool) -> None: ...

    @property
    def minStringSize(self) -> int: ...

    @minStringSize.setter
    def minStringSize(self, value: int) -> None: ...

    @property
    def nullTerminationRequired(self) -> bool: ...

    @nullTerminationRequired.setter
    def nullTerminationRequired(self, value: bool) -> None: ...

    @property
    def pascalRequired(self) -> bool: ...

    @property
    def requirePascal(self) -> None: ...  # No getter available.

    @requirePascal.setter
    def requirePascal(self, value: bool) -> None: ...

    @property
    def wordModelFile(self) -> unicode: ...

    @wordModelFile.setter
    def wordModelFile(self, value: unicode) -> None: ...

    @property
    def wordModelInitialized(self) -> bool: ...

    @wordModelInitialized.setter
    def wordModelInitialized(self, value: bool) -> None: ...
