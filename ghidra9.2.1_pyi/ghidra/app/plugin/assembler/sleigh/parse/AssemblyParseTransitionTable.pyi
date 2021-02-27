import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang
import java.util.function


class AssemblyParseTransitionTable(object):
    """
    The transition table defining an LR(0) parsing machine
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def forEach(self, consumer: java.util.function.Consumer) -> None:
        """
        Traverse every entry in the table, invoking {@link Consumer#accept(Object)} on each
        @param consumer the callback
        """
        ...

    def get(self, fromState: int, next: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol) -> int:
        """
        Get an entry from the state machine
        @param fromState the source state
        @param next the symbol that has been matched
        @return the destination state
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, fromState: int, next: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol, newState: int) -> int:
        """
        Put an entry into the state machine
        @param fromState the source state
        @param next the symbol that is matched
        @param newState the destination state
        @return the previous value for newState

         NOTE: Generally, if this return non-null, something is probably wrong with your LR(0)
               machine generator
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
