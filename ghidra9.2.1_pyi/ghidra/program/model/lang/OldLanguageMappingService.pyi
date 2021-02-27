import ghidra.program.model.lang
import java.lang


class OldLanguageMappingService(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def lookupMagicString(magicString: unicode, languageReplacementOK: bool) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        """
        Check for a mapping of an old language-name magicString to a LanguageID/CompilerSpec pair.
         If returnLanguageReplacement is false, the returned LanguageID/CompilerSpec pair may no
         longer exist and may require use of an OldLanguage and translation process.
        @param magicString old language name magic string
        @param languageReplacementOK if true the LanguageID/CompilerSpec pair corresponding to the
         latest language implementation will be returned if found, otherwise the a deprecated LanguageID/CompilerSpec pair
         may be returned.  This parameter should be false if there is a sensitivity to the language implementation
         (e.g., instruction prototypes, etc.)
        @return LanguageID/CompilerSpec pair or null if entry not found.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def processXmlLanguageString(languageString: unicode) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        """
        Parse the language string from an XML language name into the most appropriate LanguageID/CompilerSpec pair.
         The language name may either be an old name (i.e., magicString) or a new {@code <language-id>:<compiler-spec-id>} string.
         If an old language name magic-string is provided, its replacement language will be returned if known.
         The returned pair may or may not be available based upon available language implementations.
        @param languageString old or new language string
        @return LanguageID/CompilerSpec pair or null if no old name mapping could be found.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
