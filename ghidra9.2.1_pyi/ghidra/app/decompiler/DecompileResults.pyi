import ghidra.app.decompiler
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class DecompileResults(object):
    """
    Class for getting at the various structures returned
     by the decompiler.  Depending on how the DecompInterface
     was called, you can get C code (with markup), the
     function' syntax tree, the prototype, etc.

     To check if the decompileFunction call completed normally
     use the decompileCompleted method.  If this returns false,
     the getErrorMessage method may contain a useful error
     message.  Its also possible that getErrorMessage will
     return warning messages, even if decompileFunction did
     complete.

     To get the resulting C code, marked up with XML in terms
     of the lines and tokens, use the getCCodeMarkup method.

     To get the resulting C code just as a straight String,
     use the getDecompiledFunction method which returns a
     DecompiledFunction.  Off of this, you can use the getC
     method to get the raw C code as a String or use the
     getSignature method to get the functions prototype as
     a String.

     To get the syntax tree use the getHighFunction method.
    """





    def __init__(self, f: ghidra.program.model.listing.Function, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, d: ghidra.program.model.pcode.PcodeDataTypeManager, e: unicode, raw: java.io.InputStream, processState: ghidra.app.decompiler.DecompileProcess.DisposeState): ...



    def decompileCompleted(self) -> bool:
        """
        Returns true if the decompilation producing these
         results completed without aborting.  If it was
         aborted, there will be no real results in this
         object, and an error message should be available via
         getErrorMessage.
        @return true if the decompilation completed.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def failedToStart(self) -> bool:
        """
        If the action producing this set of decompiler results
         didn't complete, this method can be used to determine
         if the decompiler executable was not found or failed to start properly.
        @return true if the decompiler executable was not found.
        """
        ...

    def getCCodeMarkup(self) -> ghidra.app.decompiler.ClangTokenGroup:
        """
        Get the marked up C code associated with these
         decompilation results. If there was an error, or
         code generation was turned off, retur null
        @return the resulting root of C markup
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDecompiledFunction(self) -> ghidra.app.decompiler.DecompiledFunction:
        """
        Converts the C code results into an unadorned string.
         The returned object contains both the whole function
         and just the prototype as separate strings containing
         raw C code
        @return a DecompiledFunction object
        """
        ...

    def getErrorMessage(self) -> unicode:
        """
        Return any error message associated with the
         decompilation producing these results.  Generally,
         there will only be an error if the decompilation was
         aborted for some reason, but there could conceivably
         be warnings obtainable via this method, even if the
         decompilation did complete.
        @return any error message associated with these results
        """
        ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getHighFunction(self) -> ghidra.program.model.pcode.HighFunction:
        """
        Get the high-level function structure associated
         with these decompilation results, or null if there
         was an error during decompilation
        @return the resulting HighFunction object
        """
        ...

    def getHighParamID(self) -> ghidra.program.model.pcode.HighParamID:
        """
        Get the high-level function structure associated
         with these decompilation results, or null if there
         was an error during decompilation
        @return the resulting HighParamID object
        """
        ...

    def hashCode(self) -> int: ...

    def isCancelled(self) -> bool:
        """
        If the action producing this set of decompiler results
         didn't complete, this method can be used to determine
         if the action was explicitly cancelled (as opposed
         to an error, a timeout, or a crash).
        @return true if these results were explicitly cancelled
        """
        ...

    def isTimedOut(self) -> bool:
        """
        If the action producing this set of decompiler results
         didn't complete, this method can be used to determine
         if the action was halted because its timer expired
         (as opposed to an error, a crash, or being explicitly
         cancelled).
        @return true if the timer cancelled these results
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
    def CCodeMarkup(self) -> ghidra.app.decompiler.ClangTokenGroup: ...

    @property
    def cancelled(self) -> bool: ...

    @property
    def decompiledFunction(self) -> ghidra.app.decompiler.DecompiledFunction: ...

    @property
    def errorMessage(self) -> unicode: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def highFunction(self) -> ghidra.program.model.pcode.HighFunction: ...

    @property
    def highParamID(self) -> ghidra.program.model.pcode.HighParamID: ...

    @property
    def timedOut(self) -> bool: ...
