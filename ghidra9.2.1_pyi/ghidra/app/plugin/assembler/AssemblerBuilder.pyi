import ghidra.app.plugin.assembler
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class AssemblerBuilder(object):
    """
    An interface to build an assembler for a given language
    """









    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAssembler(self, selector: ghidra.app.plugin.assembler.AssemblySelector) -> ghidra.app.plugin.assembler.Assembler:
        """
        Build an assembler with the given selector callback
        @param selector the selector callback
        @return the built assembler
        """
        ...

    @overload
    def getAssembler(self, selector: ghidra.app.plugin.assembler.AssemblySelector, program: ghidra.program.model.listing.Program) -> ghidra.app.plugin.assembler.Assembler:
        """
        Build an assembler with the given selector callback and program binding
        @param selector the selector callback
        @param program the bound program
        @return the built assembler
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Get the language for which this instance builds an assembler
        @return the language
        """
        ...

    def getLanguageID(self) -> ghidra.program.model.lang.LanguageID:
        """
        Get the ID of the language for which this instance builds an assembler
        @return the language ID
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
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def languageID(self) -> ghidra.program.model.lang.LanguageID: ...
