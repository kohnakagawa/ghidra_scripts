from typing import List
import ghidra.app.decompiler
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class DecompilerLocation(ghidra.program.util.ProgramLocation):




    @overload
    def __init__(self):
        """
        Default constructor required for restoring a program location from XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, functionEntryPoint: ghidra.program.model.address.Address, results: ghidra.app.decompiler.DecompileResults, token: ghidra.app.decompiler.ClangToken, lineNumber: int, charPos: int): ...



    @overload
    def compareTo(self, other: ghidra.program.util.ProgramLocation) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address associated with this location.

         <p>
         Note: this may not be the same as the byte address. For example, in a {@link CodeUnit code
         unit} location this may be the minimum address of the code unit that contains the byte
         address.
        """
        ...

    def getByteAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the byte level address associated with this location.
        """
        ...

    def getCharOffset(self) -> int:
        """
        Returns the character offset in the display item at the (row,col)
        @return the character offset in the display item at the (row,col)
        """
        ...

    def getCharPos(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self) -> int:
        """
        Returns the column index of the display piece represented by this location. For most
         locations, there is only one display item per row, in which case this value will be 0.
        """
        ...

    def getComponentPath(self) -> List[int]:
        """
        Returns the componentPath for the {@link CodeUnit code unit}. Null will be returned if the
         object is an {@link Instruction} or a top-level {@link Data} object.
        """
        ...

    def getDecompile(self) -> ghidra.app.decompiler.DecompileResults:
        """
        Results from the decompilation
        @return C-AST, DFG, and CFG object. null if there are no results attached to this location
        """
        ...

    def getFunctionEntryPoint(self) -> ghidra.program.model.address.Address: ...

    def getLineNumber(self) -> int: ...

    @staticmethod
    def getLocation(program: ghidra.program.model.listing.Program, saveState: ghidra.framework.options.SaveState) -> ghidra.program.util.ProgramLocation:
        """
        Get the program location for the given program and save state object.
        @param program the program for the location
        @param saveState the state to restore
        @return the restored program location
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program associated with this location.
        """
        ...

    def getRefAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the "referred to" address if the location is over an address in some field.
        """
        ...

    def getRow(self) -> int:
        """
        Returns the row within the program location.
        @return the row within the program location.
        """
        ...

    def getToken(self) -> ghidra.app.decompiler.ClangToken:
        """
        C text token at the current cursor location
        @return token at this location, could be null if there are no decompiler results
        """
        ...

    def getTokenName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isValid(self, testProgram: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if this location represents a valid location in the given program
        @param testProgram the program to test if this location is valid.
        @return true if this location represents a valid location in the given program
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreState(self, program1: ghidra.program.model.listing.Program, obj: ghidra.framework.options.SaveState) -> None: ...

    def saveState(self, saveState: ghidra.framework.options.SaveState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def charPos(self) -> int: ...

    @property
    def decompile(self) -> ghidra.app.decompiler.DecompileResults: ...

    @property
    def functionEntryPoint(self) -> ghidra.program.model.address.Address: ...

    @property
    def lineNumber(self) -> int: ...

    @property
    def token(self) -> ghidra.app.decompiler.ClangToken: ...

    @property
    def tokenName(self) -> unicode: ...
