from typing import List
import ghidra.program.model.lang
import ghidra.program.util
import java.io
import java.lang


class OldLanguageFactory(object):
    OLD_LANGUAGE_FILE_EXT: unicode = u'.lang'







    @staticmethod
    def createOldLanguageFile(lang: ghidra.program.model.lang.Language, file: java.io.File) -> None:
        """
        Create old-language file for the specified language.
        @param lang language
        @param file output file
        @throws IOException if file error occurs
        @throws LanguageNotFoundException if lang is unknown to DefaultLanguageService
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLatestOldLanaguageDescriptions(self) -> List[ghidra.program.model.lang.LanguageDescription]:
        """
        Return the Language Descriptions for the latest version of all old languages.
        """
        ...

    def getLatestOldLanguage(self, languageID: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.LanguageDescription:
        """
        Return language description for the latest version of an old language
        @param languageID
        @return old language description or null if specification not found.
        """
        ...

    def getOldLanguage(self, languageID: ghidra.program.model.lang.LanguageID, majorVersion: int) -> ghidra.program.model.lang.Language:
        """
        Return old language if an old language specification file exists for the specified language and version.
        @param languageID
        @param majorVersion language major version, or -1 for latest version
        @return old language or null if specification not found.
        """
        ...

    @staticmethod
    def getOldLanguageFactory() -> ghidra.program.util.OldLanguageFactory:
        """
        Returns the single instance of the OldLanguageFactory.
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
    def latestOldLanaguageDescriptions(self) -> List[ghidra.program.model.lang.LanguageDescription]: ...
