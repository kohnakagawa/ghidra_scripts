import ghidra.app.plugin.assembler
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class Assemblers(object):
    """
    The primary class for obtaining an Assembler for a Ghidra-supported language.

     The general flow is: First, obtain an assembler for a language or program. Second, call its
     Assembler#assemble(Address, String...) and related methods to perform assembly. More
     advanced uses pass a AssemblySelector to control certain aspects of assembly instruction
     selection, and to obtain advanced diagnostics, like detailed errors and code completion.




    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def getAssembler(lang: ghidra.program.model.lang.Language) -> ghidra.app.plugin.assembler.Assembler:
        """
        Get an assembler for the given language.
        @see #getAssembler(Language, AssemblySelector)
        @param lang the language
        @return a suitable assembler
        """
        ...

    @overload
    @staticmethod
    def getAssembler(program: ghidra.program.model.listing.Program) -> ghidra.app.plugin.assembler.Assembler:
        """
        Get an assembler for the given program.
        @see #getAssembler(Program, AssemblySelector)
        @param program the program
        @return a suitable assembler
        """
        ...

    @overload
    @staticmethod
    def getAssembler(lang: ghidra.program.model.lang.Language, selector: ghidra.app.plugin.assembler.AssemblySelector) -> ghidra.app.plugin.assembler.Assembler:
        """
        Get an assembler for the given language.

         Provides a suitable assembler for the given language. Only calls to its
         Assembler#assembleLine() method are valid. If this is the first time a language has been
         requested, this function may take some time to build the assembler. Otherwise, it returns a
         cached assembler.
        @param selector a method to select a single result from many
        @param lang the language for which an assembler is requested
        @return the assembler for the given language
        """
        ...

    @overload
    @staticmethod
    def getAssembler(program: ghidra.program.model.listing.Program, selector: ghidra.app.plugin.assembler.AssemblySelector) -> ghidra.app.plugin.assembler.Assembler:
        """
        Get an assembler for the given program.

         Provides an assembler suitable for the program's language, and bound to the program. Calls
         to its Assembler#assemble() function will cause modifications to the bound program. If this
         is the first time an assembler for the program's language has been requested, this function
         may take some time to build the assembler.
        @param selector a method to select a single result from many
        @param program the program for which an assembler is requested
        @return the assembler bound to the given program
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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
