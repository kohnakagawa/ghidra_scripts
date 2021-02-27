import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import java.lang
import java.util


class SimpleDiffUtility(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def expandAddressSetToIncludeFullDelaySlots(program: ghidra.program.model.listing.Program, originalSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSetView:
        """
        Expand a specified address set to include complete delay slotted instructions
         which may be included at the start or end of each range within the specified
         address set.
        @param program program
        @param originalSet original address set
        @return expanded address set
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCompatibleAddress(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.address.Address:
        """
        Convert an address from the specified program to a comparable address in the
         specified otherProgram.
        @param program program which contains the specified address instance
        @param addr address in program
        @param otherProgram other program
        @return address for otherProgram or null if no such address exists.
        """
        ...

    @staticmethod
    def getCompatibleAddressSpace(addrSpace: ghidra.program.model.address.AddressSpace, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSpace: ...

    @staticmethod
    def getCompatibleVariableStorage(program: ghidra.program.model.listing.Program, storage: ghidra.program.model.listing.VariableStorage, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.VariableStorage:
        """
        Convert a variable storage object from the specified program to a comparable variable storage
         object in the specified otherProgram.  Certain variable storage (UNIQUE/HASH-based) will
         always produce a null return object.
        @param program program which contains the specified address instance
        @param storage variable storage in program
        @param otherProgram other program
        @return storage for otherProgram or null if storage can not be mapped to other program
        """
        ...

    @staticmethod
    def getCompatibleVarnode(program: ghidra.program.model.listing.Program, varnode: ghidra.program.model.pcode.Varnode, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.pcode.Varnode:
        """
        Convert a varnode from the specified program to a comparable varnode in the
         specified otherProgram.  Certain varnode addresses spaces (UNIQUE, HASH) will
         always produce a null return varnode.
        @param program program which contains the specified address instance
        @param varnode varnode in program
        @param otherProgram other program
        @return varnode for otherProgram or null if varnode can not be mapped to other program
        """
        ...

    @staticmethod
    def getEndOfDelaySlots(instr: ghidra.program.model.listing.Instruction) -> ghidra.program.model.address.Address:
        """
        If the specified instruction is contained within a delay slot, or has delay slots,
         the maximum address of the last delay slot instruction will be returned.
         If a normal instruction is specified the instructions maximum address is returned.
        @param instr
        @return maximum address of instruction or its last delay slot
        """
        ...

    @staticmethod
    def getMatchingExternalLocation(program: ghidra.program.model.listing.Program, externalLocation: ghidra.program.model.symbol.ExternalLocation, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Given an external location for a specified program, get the corresponding external location,
         which has the same name and path,  from the specified otherProgram.<br>
         Note: The type of the returned external location may be different than the type of the
         original external location.
        @param program program which contains the specified external location instance
        @param externalLocation external location to look for
        @param otherProgram other program
        @return corresponding external location for otherProgram or null if no such external location exists.
        """
        ...

    @staticmethod
    def getMatchingExternalSymbol(program: ghidra.program.model.listing.Program, symbol: ghidra.program.model.symbol.Symbol, otherProgram: ghidra.program.model.listing.Program, otherRestrictedSymbolIds: java.util.Set) -> ghidra.program.model.symbol.Symbol:
        """
        Given an external symbol for a specified program, get the corresponding symbol,
         which has the same name and path,  from the specified otherProgram.<br>
         Note: The type of the returned symbol may be different than the type of the symbol
        @param program program which contains the specified symbol instance
        @param symbol symbol to look for
        @param otherProgram other program
        @param otherRestrictedSymbolIds an optional set of symbol ID's from the other program
         which will be treated as the exclusive set of candidate symbols to consider.
        @return corresponding external symbol for otherProgram or null if no such symbol exists.
        """
        ...

    @staticmethod
    def getStartOfDelaySlots(instr: ghidra.program.model.listing.Instruction) -> ghidra.program.model.address.Address: ...

    @staticmethod
    def getSymbol(symbol: ghidra.program.model.symbol.Symbol, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Symbol:
        """
        Given a symbol for a specified program, get the corresponding symbol from the
         specified otherProgram.
        @param symbol symbol to look for
        @param otherProgram other program
        @return corresponding symbol for otherProgram or null if no such symbol exists.
        """
        ...

    @staticmethod
    def getVariableSymbol(symbol: ghidra.program.model.symbol.Symbol, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Symbol:
        """
        Find the variable symbol in otherProgram which corresponds to the specified varSym.
        @param symbol variable symbol
        @param otherProgram other program
        @return the variable symbol or null
        """
        ...

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
