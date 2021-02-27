import ghidra.program.model.lang
import java.lang


class LanguageCompilerSpecPair(object, java.lang.Comparable):
    """
    Represents an opinion's processor language and compiler.
    """

    compilerSpecID: ghidra.program.model.lang.CompilerSpecID
    languageID: ghidra.program.model.lang.LanguageID



    @overload
    def __init__(self, languageID: unicode, compilerSpecID: unicode):
        """
        Creates a new language and compiler pair.
        @param languageID The language ID string (x86:LE:32:default, 8051:BE:16:default, etc).
        @param compilerSpecID The compiler spec ID string (gcc, borlandcpp, etc).
        @throws IllegalArgumentException if the language or compiler ID strings are null or empty.
        """
        ...

    @overload
    def __init__(self, languageID: ghidra.program.model.lang.LanguageID, compilerSpecID: ghidra.program.model.lang.CompilerSpecID):
        """
        Creates a new language and compiler pair.
        @param languageID The language ID.
        @param compilerSpecID The compiler spec ID.
        @throws IllegalArgumentException if the language or compiler ID is null.
        """
        ...



    @overload
    def compareTo(self, o: ghidra.program.model.lang.LanguageCompilerSpecPair) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec:
        """
        Gets the {@link CompilerSpec} for this object's {@link CompilerSpecID}.
        @return The {@link CompilerSpec} for this object's {@link CompilerSpecID}.
        @throws LanguageNotFoundException if no {@link Language} could be found for this
           object's {@link LanguageID}.
        @throws CompilerSpecNotFoundException if no {@link CompilerSpec} could be found for this
           object's {@link CompilerSpecID}.
        """
        ...

    @overload
    def getCompilerSpec(self, languageService: ghidra.program.model.lang.LanguageService) -> ghidra.program.model.lang.CompilerSpec:
        """
        Gets the {@link CompilerSpec} for this object's {@link CompilerSpecID}, using the given
         language service to do the lookup.
        @param languageService The language service to use for compiler lookup.
        @return The {@link CompilerSpec} for this object's {@link CompilerSpecID}, using the given
           language service to do the lookup.
        @throws LanguageNotFoundException if no {@link Language} could be found for this
           object's {@link LanguageID} using the given language service.
        @throws CompilerSpecNotFoundException if no {@link CompilerSpec} could be found for this
           object's {@link CompilerSpecID} using the given language service.
        """
        ...

    @overload
    def getCompilerSpecDescription(self) -> ghidra.program.model.lang.CompilerSpecDescription:
        """
        Gets the {@link CompilerSpecDescription} for this object's {@link CompilerSpecID}.
        @return The {@link CompilerSpecDescription} for this object's {@link CompilerSpecID}.
        @throws LanguageNotFoundException if no {@link LanguageDescription} could be found for this
           object's {@link LanguageID}.
        @throws CompilerSpecNotFoundException if no {@link CompilerSpecDescription} could be found
           for this object's {@link CompilerSpecID}.
        """
        ...

    @overload
    def getCompilerSpecDescription(self, languageService: ghidra.program.model.lang.LanguageService) -> ghidra.program.model.lang.CompilerSpecDescription:
        """
        Gets the {@link CompilerSpecDescription} for this object's {@link CompilerSpecID}.
        @param languageService The language service to use for description lookup.
        @return The {@link CompilerSpecDescription} for this object's {@link CompilerSpecID}.
        @throws LanguageNotFoundException if no {@link LanguageDescription} could be found for this
           object's {@link LanguageID}.
        @throws CompilerSpecNotFoundException if no {@link CompilerSpecDescription} could be found
           for this object's {@link CompilerSpecID} using the given language service.
        """
        ...

    @overload
    def getLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Gets the {@link Language} for this object's {@link LanguageID}.
        @return The {@link Language} for this object's {@link LanguageID}.
        @throws LanguageNotFoundException if no {@link Language} could be found for this
           object's {@link LanguageID}.
        """
        ...

    @overload
    def getLanguage(self, languageService: ghidra.program.model.lang.LanguageService) -> ghidra.program.model.lang.Language:
        """
        Gets the {@link Language} for this object's {@link LanguageID}, using the given language
         service to do the lookup.
        @param languageService The language service to use for language lookup.
        @return The {@link Language} for this object's {@link LanguageID}, using the given language
           service to do the lookup.
        @throws LanguageNotFoundException if no {@link Language} could be found for this
           object's {@link LanguageID} using the given language service.
        """
        ...

    @overload
    def getLanguageDescription(self) -> ghidra.program.model.lang.LanguageDescription:
        """
        Gets the {@link LanguageDescription} for this object's {@link LanguageID}.
        @return The {@link LanguageDescription} for this object's {@link LanguageID}.
        @throws LanguageNotFoundException if no {@link LanguageDescription} could be found for this
           object's {@link LanguageID}.
        """
        ...

    @overload
    def getLanguageDescription(self, languageService: ghidra.program.model.lang.LanguageService) -> ghidra.program.model.lang.LanguageDescription:
        """
        Gets the {@link LanguageDescription} for this object's {@link LanguageID}.
        @param languageService The language service to use for description lookup.
        @return The {@link LanguageDescription} for this object's {@link LanguageID}.
        @throws LanguageNotFoundException if no {@link LanguageDescription} could be found for this
           object's {@link LanguageID} using the given language service.
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
    def compilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    @property
    def compilerSpecDescription(self) -> ghidra.program.model.lang.CompilerSpecDescription: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def languageDescription(self) -> ghidra.program.model.lang.LanguageDescription: ...
