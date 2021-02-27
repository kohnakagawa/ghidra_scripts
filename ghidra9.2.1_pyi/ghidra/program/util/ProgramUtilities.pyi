from typing import Iterator
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util
import java.lang


class ProgramUtilities(object):
    """
    General utility class that provides convenience methods
     to deal with Program objects.
    """









    @staticmethod
    def addTrackedProgram(program: ghidra.program.model.listing.Program) -> None:
        """
        Programs will only be stored during testing and are maintained as weak references.
        @param program The program that is being tracked (all programs during testing.
        """
        ...

    @staticmethod
    def convertFunctionWrappedExternalPointer(functionSymbol: ghidra.program.model.symbol.Symbol) -> None:
        """
        Convert old function wrapped external pointers.  Migrate function to
         external function.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getByteCodeString(cu: ghidra.program.model.listing.CodeUnit) -> unicode:
        """
        Get the bytes associated with the specified code unit cu
         formatted as a string.  Bytes will be returned as 2-digit hex
         separated with a space.  Any undefined bytes will be represented by "??".
        @param cu code unit
        @return formatted byte string
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDataConverter(program: ghidra.program.model.listing.Program) -> ghidra.util.DataConverter: ...

    @staticmethod
    def getSystemPrograms() -> Iterator[ghidra.program.model.listing.Program]:
        """
        Returns an iterator for all of the {@link Program} objects in the system, which is all
         created programs in any state that have not been garbage collected.
         <p>
         <b>Note:</b>The Iterator is backed by an unmodifiable set, so any attempts to modify the
         Iterator will throw an {@link UnsupportedOperationException}.
        @return an iterator for all of the programs in the system
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseAddress(program: ghidra.program.model.listing.Program, addressString: unicode) -> ghidra.program.model.address.Address: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
