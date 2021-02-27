from typing import List
import ghidra.program.model.lang
import java.lang


class LanguageService(object):
    """
    Service that provides a Language given a name, and
     information about the language.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultLanguage(self, processor: ghidra.program.model.lang.Processor) -> ghidra.program.model.lang.Language:
        """
        Returns the default Language to use for the given processor;
        @param processor the processor for which to get a language.
        @throws LanguageNotFoundException if there is no languages at all for the given processor.
        """
        ...

    def getLanguage(self, languageID: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.Language:
        """
        Returns the language with the given language ID
        @param languageID the ID of language to retrieve
        @return the {@link Language} matching the given ID
        @throws LanguageNotFoundException if no language can be found for the given ID
        """
        ...

    @overload
    def getLanguageCompilerSpecPairs(self, query: ghidra.program.model.lang.ExternalLanguageCompilerSpecQuery) -> List[ghidra.program.model.lang.LanguageCompilerSpecPair]:
        """
        Returns all known language/compiler spec pairs which satisfy the criteria
         identify by the non-null parameters. A null value implies a don't-care
         wildcard value.  OMITS DEPRECATED LANGUAGES.
         This uses an ExternalLanguageCompilerSpecQuery rather than a
         LanguageCompilerSpecQuery.
        @param query
        @return
        """
        ...

    @overload
    def getLanguageCompilerSpecPairs(self, query: ghidra.program.model.lang.LanguageCompilerSpecQuery) -> List[ghidra.program.model.lang.LanguageCompilerSpecPair]:
        """
        Returns all known language/compiler spec pairs which satisfy the criteria
         identify by the non-null parameters. A null value implies a don't-care
         wildcard value.  OMITS DEPRECATED LANGUAGES.
        @param query TODO
        @return
        """
        ...

    def getLanguageDescription(self, languageID: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.LanguageDescription:
        """
        Get language information for the given language ID.
        @param languageID the id for the language.
        @return language information for the given language ID.
        @throws LanguageNotFoundException if there is no language for the given ID.
        """
        ...

    @overload
    def getLanguageDescriptions(self, includeDeprecatedLanguages: bool) -> List[ghidra.program.model.lang.LanguageDescription]:
        """
        Returns all known language Descriptions
        @param includeDeprecatedLanguages TODO
        @return all know language Descriptions.
        """
        ...

    @overload
    def getLanguageDescriptions(self, processor: ghidra.program.model.lang.Processor) -> List[ghidra.program.model.lang.LanguageDescription]:
        """
        Returns all language Descriptions associated with the given processor.
        @param processor the processor for which to retrieve all know language descriptions.
        """
        ...

    @overload
    def getLanguageDescriptions(self, processor: ghidra.program.model.lang.Processor, endianess: ghidra.program.model.lang.Endian, size: int, variant: unicode) -> List[ghidra.program.model.lang.LanguageDescription]:
        """
        Returns all known language descriptions which satisfy the criteria identify by the
         non-null parameters.  A null value implies a don't-care wildcard value.
        @param processor the processor for which to get a language
        @param endianess big or little
        @param size processor address space size (in bits)
        @param variant the processor version (usually 'default')
        @return the language descriptions that fit the parameters
        @deprecated use {@link #getLanguageDescriptions(Processor)} instead
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
