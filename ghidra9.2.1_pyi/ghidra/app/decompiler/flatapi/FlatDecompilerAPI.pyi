import ghidra.app.decompiler
import ghidra.program.model.listing
import ghidra.util
import java.lang


class FlatDecompilerAPI(object, ghidra.util.Disposable):




    @overload
    def __init__(self):
        """
        Initializes without a provided FlatProgramAPI instance...this must be set before
         using the FlatDecompilerAPI!
        """
        ...

    @overload
    def __init__(self, flatProgramAPI: ghidra.program.flatapi.FlatProgramAPI):
        """
        Initializes with a provided FlatProgramAPI instance.
        @param flatProgramAPI the FlatProgramAPI instance.
        """
        ...



    @overload
    def decompile(self, function: ghidra.program.model.listing.Function) -> unicode:
        """
        Decompiles the specified function and returns a
         string containing the decompilation.
         This call does not impose a timeout.
        @param function the function to decompile
        @return a string containing the decompilation
        """
        ...

    @overload
    def decompile(self, function: ghidra.program.model.listing.Function, timeoutSecs: int) -> unicode:
        """
        Decompiles the specified function and returns a
         string containing the decompilation.
        @param function the function to decompile
        @param timeoutSecs maximum time allowed for decompile to complete.
        @return a string containing the decompilation
        """
        ...

    def dispose(self) -> None:
        """
        Disposes of the decompiler resources by calling currentDecompiler.dispose().
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDecompiler(self) -> ghidra.app.decompiler.DecompInterface:
        """
        Gets the actual decompiler (may be null if not initialized).
        @return the decompiler
        """
        ...

    def hashCode(self) -> int: ...

    def initialize(self) -> None:
        """
        Initializes the decompiler instance.
        """
        ...

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
    def decompiler(self) -> ghidra.app.decompiler.DecompInterface: ...
