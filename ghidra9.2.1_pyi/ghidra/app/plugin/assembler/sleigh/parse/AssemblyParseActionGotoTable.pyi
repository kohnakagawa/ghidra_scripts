import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.parse
import ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable
import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang
import java.util


class AssemblyParseActionGotoTable(object):
    """
    The Action/Goto table for a LALR(1) parser

     This table is unconventional in that it permits a single cell to be populated by more than one
     action. Typically, such a situation would indicate an ambiguity, or the need for a longer
     look-ahead value. Because we do not presume to control the grammar (which was automatically
     derived from another source), the parsing algorithm will simply branch, eventually trying both
     options.
    """






    class Action(object, java.lang.Comparable):




        def __init__(self): ...



        @overload
        def compareTo(self, __a0: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

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






    class ReduceAction(ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action):




        def __init__(self, __a0: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction): ...



        @overload
        def compareTo(self, __a0: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

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






    class ShiftAction(ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action):




        def __init__(self, __a0: int): ...



        @overload
        def compareTo(self, __a0: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

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






    class AcceptAction(ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action):
        ACCEPT: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.AcceptAction = acc



        def __init__(self): ...



        @overload
        def compareTo(self, __a0: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

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






    class GotoAction(ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action):




        def __init__(self, __a0: int): ...



        @overload
        def compareTo(self, __a0: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

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



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def get(self, fromState: int, next: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol) -> java.util.Collection:
        """
        Get all entries in a given cell
        @param fromState the state (row) in the table
        @param next the symbol (column) in the table
        @return all action entries in the given cell
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getExpected(self, fromState: int) -> java.util.Collection:
        """
        Get the terminals that are expected, i.e., have entries for the given state
        @param fromState the state (row) in the table
        @return the collection of populated columns (terminals) for the given state
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, fromState: int, next: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol, action: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseActionGotoTable.Action) -> bool:
        """
        Add an action entry to the given cell
        @param fromState the state (row) in the table
        @param next the symbol (column) in the table
        @param action the entry to add to the cell
        @return true, if the given entry was not already present
        """
        ...

    def putAccept(self, fromState: int) -> bool:
        """
        Add an ACCEPT entry for the given state at the end of input
        @param fromState the state (row) in the table
        @return true, if the state does not already accept on end of input
        """
        ...

    def putGoto(self, fromState: int, next: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal, newState: int) -> bool:
        """
        Add a GOTO entry to the given cell
        @param fromState the state (row) in the table
        @param next the symbol (column) in the table
        @param newState the target state
        @return true, if the given entry was not already present
        """
        ...

    def putReduce(self, fromState: int, next: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal, prod: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction) -> bool:
        """
        Add a REDUCE (R<i>n</i>) entry to the given cell
        @param fromState the state (row) in the table
        @param next the symbol (column) in the table
        @param prod the production (having index <i>n</i>) associated with the reduction
        @return true, if the given entry was not already present
        """
        ...

    def putShift(self, fromState: int, next: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal, newState: int) -> bool:
        """
        Add a SHIFT (S<i>n</i>) entry to the given cell
        @param fromState the state (row) in the table
        @param next the symbol (column) in the table
        @param newState the state (<i>n</i>) after the shift is applied
        @return true, if the given entry was not already present
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
