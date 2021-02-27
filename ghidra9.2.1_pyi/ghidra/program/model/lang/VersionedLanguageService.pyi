from typing import List
import ghidra.program.model.lang
import java.lang


class VersionedLanguageService(ghidra.program.model.lang.LanguageService, object):
    """
    Service that provides a Language given a name, and
     information about the language.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultLanguage(self, __a0: ghidra.program.model.lang.Processor) -> ghidra.program.model.lang.Language: ...

    @overload
    def getLanguage(self, __a0: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.Language: ...

    @overload
    def getLanguage(self, languageID: ghidra.program.model.lang.LanguageID, version: int) -> ghidra.program.model.lang.Language:
        """
        Returns a specific language version with the given language ID.
         This form should only be used when handling language upgrade concerns.
        @param languageID the ID of language to retrieve.
        @param version major version
        @throws LanguageNotFoundException if the specified language version can not be found
         for the given ID.
        """
        ...

    @overload
    def getLanguageCompilerSpecPairs(self, __a0: ghidra.program.model.lang.ExternalLanguageCompilerSpecQuery) -> List[object]: ...

    @overload
    def getLanguageCompilerSpecPairs(self, __a0: ghidra.program.model.lang.LanguageCompilerSpecQuery) -> List[object]: ...

    @overload
    def getLanguageDescription(self, __a0: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.LanguageDescription: ...

    @overload
    def getLanguageDescription(self, languageID: ghidra.program.model.lang.LanguageID, version: int) -> ghidra.program.model.lang.LanguageDescription:
        """
        Get language information for a specific version of the given language ID.
         This form should only be used when handling language upgrade concerns.
        @param languageID the id for the language.
        @return language information for the given language ID.
        @throws LanguageNotFoundException if there is no language for the given ID.
        """
        ...

    @overload
    def getLanguageDescriptions(self, __a0: bool) -> List[object]: ...

    @overload
    def getLanguageDescriptions(self, __a0: ghidra.program.model.lang.Processor) -> List[object]: ...

    @overload
    def getLanguageDescriptions(self, __a0: ghidra.program.model.lang.Processor, __a1: ghidra.program.model.lang.Endian, __a2: int, __a3: unicode) -> List[object]: ...

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
