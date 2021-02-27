from typing import List
import ghidra.program.model.lang
import ghidra.util.classfinder
import java.lang


class LanguageProvider(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL LanguageProvider CLASSES MUST END IN "LanguageProvider".  If not,
     the ClassSearcher will not find them.

     Service for providing languages.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLanguage(self, languageId: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.Language:
        """
        Returns the language with the given name or null if no language has that name
        @param languageId the name of the language to be retrieved
        @return the {@link Language} with the given name
        """
        ...

    def getLanguageDescriptions(self) -> List[ghidra.program.model.lang.LanguageDescription]:
        """
        Returns a list of language descriptions provided by this provider
        """
        ...

    def hadLoadFailure(self) -> bool:
        """
        @return true if one of more languages or language description failed to load
         properly.
        """
        ...

    def hashCode(self) -> int: ...

    def isLanguageLoaded(self, languageId: ghidra.program.model.lang.LanguageID) -> bool:
        """
        Returns true if the given language has been successfully loaded
        @param languageId the name of the language to be retrieved
        @return true if the given language has been successfully loaded
        """
        ...

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
    def languageDescriptions(self) -> List[ghidra.program.model.lang.LanguageDescription]: ...
