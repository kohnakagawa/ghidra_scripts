from typing import List
import ghidra.program.model.lang
import java.lang


class SleighLanguageProvider(object, ghidra.program.model.lang.LanguageProvider):
    """
    Searches resources for spec files and provides LanguageDescriptions for these
     specifications
    """

    LANGUAGE_DIR_NAME: unicode = u'languages'



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, ldefsFile: generic.jar.ResourceFile): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLanguage(self, languageId: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.Language: ...

    def getLanguageDescriptions(self) -> List[ghidra.program.model.lang.LanguageDescription]: ...

    def hadLoadFailure(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isLanguageLoaded(self, languageId: ghidra.program.model.lang.LanguageID) -> bool: ...

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
