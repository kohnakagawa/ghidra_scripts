import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.parse
import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang
import java.util


class AssemblyParseStateItem(object, java.lang.Comparable):
    """
    An item in the state of an LR(0) parser

     An item is a production with a dot indicating a position while parsing
    """





    @overload
    def __init__(self, prod: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction):
        """
        Construct a new item starting at the far left of the given production
        @param prod the production
        """
        ...

    @overload
    def __init__(self, prod: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction, pos: int):
        """
        Construct a new item starting immediately before the symbol at the given position in the
         given production
        @param prod the production
        @param pos the position of the dot
        """
        ...



    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseStateItem) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def completed(self) -> bool:
        """
        Check if this item is completed

         The item is completed if all symbols have been matched, i.e., the dot is at the far right of
         the production.
        @return true iff the item is completed
        """
        ...

    def equals(self, that: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClosure(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar) -> java.util.Collection:
        """
        "Fill" one step out to close a state containing this item

         To compute the full closure, you must continue stepping out until no new items are generated
        @param grammar the grammar containing the production
        @return a subset of items in the closure of a state containing this item
        """
        ...

    def getNext(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol:
        """
        Get the symbol immediately to the right of the dot

         This is the symbol which must be matched to advance the dot.
        @return the symbol, or null if the item is completed, i.e., the dot is at the far right
        """
        ...

    def getPos(self) -> int:
        """
        Get the position of the dot

         The position is the number of symbols to the left of the dot.
        @return
        """
        ...

    def getProduction(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction:
        """
        Get the production associated with this item
        @return the production
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def read(self) -> ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseStateItem:
        """
        Advance the dot by one position, producing a new item
        @return the new item
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def next(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol: ...

    @property
    def pos(self) -> int: ...

    @property
    def production(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction: ...
