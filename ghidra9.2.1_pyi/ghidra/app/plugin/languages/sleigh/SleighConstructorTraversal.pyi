import ghidra.app.plugin.languages.sleigh
import java.lang


class SleighConstructorTraversal(object, ghidra.app.plugin.languages.sleigh.VisitorResults):
    """
    A class to traverse SLEIGH constructors in a language
    """

    CONTINUE: int = 0
    FINISHED: int = 1
    TERMINATE: int = 2



    def __init__(self, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage):
        """
        Prepare to traverse the constructors of a given SLEIGH language
        @param lang the language
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def traverse(self, visitor: ghidra.app.plugin.languages.sleigh.ConstructorEntryVisitor) -> int:
        """
        Traverse the constructors in the language
        @param visitor a callback for each constructor
        @return a value from {@link VisitorResults}
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
