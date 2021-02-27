from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.symbol
import ghidra.app.plugin.processors.sleigh.template
import ghidra.xml
import java.lang
import java.util


class Constructor(object, java.lang.Comparable):
    """
    The primary sleigh concept representing a semantic action
     taking operands (semantic values) as input
     producing a semantic value as output
     matching a particular pattern
     printing in a certain way
    """





    def __init__(self): ...



    def applyContext(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker, debug: ghidra.app.plugin.processors.sleigh.SleighDebugLogger) -> None:
        """
        Apply any operations on context for this Constructor to a
         particular InstructionContext
        @param walker the parser walker
        @param debug the debug logger
        @throws MemoryAccessException if the context failed to be applied.
        """
        ...

    @overload
    def compareTo(self, that: ghidra.app.plugin.processors.sleigh.Constructor) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextChanges(self) -> List[ghidra.app.plugin.processors.sleigh.ContextChange]: ...

    def getFlowthruIndex(self) -> int: ...

    def getId(self) -> int: ...

    def getLineno(self) -> int: ...

    def getMinimumLength(self) -> int: ...

    def getNamedTempl(self, secnum: int) -> ghidra.app.plugin.processors.sleigh.template.ConstructTpl:
        """
        Retrieve a named p-code template section
        @param secnum is the id of the section to return
        @return the named section (or null)
        """
        ...

    def getNumOperands(self) -> int: ...

    def getOperand(self, i: int) -> ghidra.app.plugin.processors.sleigh.symbol.OperandSymbol: ...

    def getOpsPrintOrder(self) -> List[int]:
        """
        Return the indices of the operands in an array
         in the order they are printed (after the first white space)
        @return array of operand indices
        """
        ...

    def getParent(self) -> ghidra.app.plugin.processors.sleigh.symbol.SubtableSymbol: ...

    def getPrintPieces(self) -> List[unicode]: ...

    def getTempl(self) -> ghidra.app.plugin.processors.sleigh.template.ConstructTpl: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> unicode: ...

    def printBody(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> unicode: ...

    def printList(self, __a0: ghidra.app.plugin.processors.sleigh.ParserWalker, __a1: java.util.ArrayList) -> None: ...

    def printMnemonic(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> unicode: ...

    def printSeparator(self, separatorIndex: int) -> unicode: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, sleigh: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> None: ...

    def setId(self, val: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def contextChanges(self) -> List[object]: ...

    @property
    def flowthruIndex(self) -> int: ...

    @property
    def id(self) -> int: ...

    @id.setter
    def id(self, value: int) -> None: ...

    @property
    def lineno(self) -> int: ...

    @property
    def minimumLength(self) -> int: ...

    @property
    def numOperands(self) -> int: ...

    @property
    def opsPrintOrder(self) -> List[int]: ...

    @property
    def parent(self) -> ghidra.app.plugin.processors.sleigh.symbol.SubtableSymbol: ...

    @property
    def printPieces(self) -> List[object]: ...

    @property
    def templ(self) -> ghidra.app.plugin.processors.sleigh.template.ConstructTpl: ...
