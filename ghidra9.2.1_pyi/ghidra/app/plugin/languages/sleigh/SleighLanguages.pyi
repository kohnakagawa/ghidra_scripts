import ghidra.app.plugin.languages.sleigh
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.symbol
import java.lang


class SleighLanguages(object):
    """
    A collection of utility functions for traversing constructors and Pcode operations of SLEIGH
     languages
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def traverseAllPcodeOps(lang: ghidra.app.plugin.processors.sleigh.SleighLanguage, visitor: ghidra.app.plugin.languages.sleigh.PcodeOpEntryVisitor) -> int:
        """
        Traverse the Pcode operations of a given SLEIGH language

         During traversal, if a "NOP" constructor, i.e., one having no Pcode operations, is
         encountered, the callback is still invoked at least once, with a null Pcode operation. This
         is so NOP constructors are not overlooked by this traversal.
        @param lang the language
        @param visitor a callback for each Pcode operation visited
        @return a value from {@link VisitorResults}
        """
        ...

    @overload
    @staticmethod
    def traverseConstructors(lang: ghidra.app.plugin.processors.sleigh.SleighLanguage, visitor: ghidra.app.plugin.languages.sleigh.ConstructorEntryVisitor) -> int:
        """
        Traverse the constructors of a given SLEIGH language
        @param lang the language
        @param visitor a callback for each constructor visited
        @return a value from {@link VisitorResults}
        """
        ...

    @overload
    @staticmethod
    def traverseConstructors(subtable: ghidra.app.plugin.processors.sleigh.symbol.SubtableSymbol, visitor: ghidra.app.plugin.languages.sleigh.SubtableEntryVisitor) -> int:
        """
        Traverse the constructors of a given table
        @param subtable the table
        @param visitor a callback for each constructor visited
        @return a value from {@link VisitorResults}
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
