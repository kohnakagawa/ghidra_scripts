import ghidra.program.model.lang
import ghidra.program.util
import java.lang


class LanguageTranslatorFactory(object):
    """
    LanguageTranslatorFactory manages all language translators within Ghidra.
     Language translators support either a version translation for a single language, or a
     language transition from one language to another.  The following types of translators
     are supported:

     Simple translators are established based upon a translator XML specification file (*.trans).
     Explicit translators are class implementations of the LanguageTranslator interface.
     The abstract LanguageTranslatorAdapter has been supplied for this purpose so that
     default mappings can be used if needed.  Such custom translator classes should not be
     created within the 'ghidra.program.util' package since they will be ignored by the factory.
     Default translators can be instantiated for languages whose address spaces map to one-another.
     Such default translations may be lossy with register mappings and could result in lost register
     variables and references.

    """

    LANGUAGE_TRANSLATOR_FILE_EXT: unicode = u'.trans'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getLanguageTranslator(self, languageName: ghidra.program.model.lang.LanguageID, majorVersion: int) -> ghidra.program.util.LanguageTranslator:
        """
        Returns a language translation for a language version which is no longer supported.
        @param languageName old unsupported language name
        @param majorVersion language major version within program
        @return language translator if one can be determined, otherwise null is returned.
        """
        ...

    @overload
    def getLanguageTranslator(self, fromLanguage: ghidra.program.model.lang.Language, toLanguage: ghidra.program.model.lang.Language) -> ghidra.program.util.LanguageTranslator:
        """
        Returns a language translator for the transition from an oldLanguage to a newLanguage.
         The toLanguage may be a different language or a newer version of fromLanguage.
        @param fromLanguage old language
        @param toLanguage new language
        @return language translator if transition is supported, otherwise null is returned.
        """
        ...

    @staticmethod
    def getLanguageTranslatorFactory() -> ghidra.program.util.LanguageTranslatorFactory:
        """
        Returns the single instance of the OldLanguageFactory.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def registerLanguageTranslatorFactoryMinion(minion: ghidra.program.util.LanguageTranslatorFactoryMinion) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
