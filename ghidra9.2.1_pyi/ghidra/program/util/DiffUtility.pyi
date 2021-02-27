import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.program.util
import java.lang
import java.util


class DiffUtility(ghidra.program.util.SimpleDiffUtility):
    """
    The DiffUtility class provides static methods for getting and
     creating an object in one program based on an object from another program.
    """





    def __init__(self): ...



    @staticmethod
    def compare(program1: ghidra.program.model.listing.Program, addr1: ghidra.program.model.address.Address, program2: ghidra.program.model.listing.Program, addr2: ghidra.program.model.address.Address) -> int:
        """
        Compare any two addresses from two different programs.
        @param program1
        @param addr1
        @param program2
        @param addr2
        @return
        """
        ...

    @staticmethod
    def createExtLocation(program: ghidra.program.model.listing.Program, extLoc: ghidra.program.model.symbol.ExternalLocation, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Create equivalent external location in otherProgram.
        @param program program containing extLoc
        @param extLoc existing external location to be copied
        @param otherProgram target program
        @return new external location
        @throws InvalidInputException
        """
        ...

    @staticmethod
    def createNamespace(program: ghidra.program.model.listing.Program, namespace: ghidra.program.model.symbol.Namespace, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Namespace:
        """
        Given a namespace, create the corresponding namespace in the
         specified otherProgram. If a corresponding namespace already exists, it is returned.
         The return namespace body may be different.
        @param program program which contains the specified namespace instance
        @param namespace namespace to look for
        @param otherProgram other program
        @return corresponding namespace for otherProgram or null if no such namespace exists.
        @throws InvalidInputException if the namespace's name or path is not valid.
        @throws DuplicateNameException if the namespace's name or path cannot be created
         due to a conflict with another namespace or symbol.
        """
        ...

    @staticmethod
    def createReference(program: ghidra.program.model.listing.Program, ref: ghidra.program.model.symbol.Reference, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Reference:
        """
        Given a reference for a specified program, create a comparable reference in the
         specified otherProgram if possible. An open transaction on otherProgram must exist.
        @param program program which contains the specified reference instance
        @param ref reference to be added
        @param otherProgram other program
        @return new reference for otherProgram or null if unable to create reference.
        """
        ...

    @staticmethod
    def createVariable(program: ghidra.program.model.listing.Program, var: ghidra.program.model.listing.Variable, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.Variable:
        """
        Given a variable for a specified program, create a comparable variable in the
         specified otherProgram if possible. An open transaction on otherProgram must exist.
        @param program program which contains the specified variable instance
        @param var variable to be added from program to otherProgram.
        @param otherProgram other program
        @return new variable for otherProgram or null if unable to create variable.
        @throws DuplicateNameException if another variable already exists with
         the same name as var in the resulting function.
        @throws InvalidInputException if data type is not a fixed length or variable name is invalid, etc.
        @throws VariableSizeException if data type size is too large based upon storage constraints.
        """
        ...

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
    def getCodeUnitSet(addrSet: ghidra.program.model.address.AddressSetView, program: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSet:
        """
        Creates an address set that contains the entire code units within the
          program's listing that are part of the address set that is passed in.
         <br>Note: This method will not remove any addresses from the address set even
         if they are not part of code units in the program's listing.
        @param addrSet The original address set that may contain portions of
         code units.
        @param program the program which has the code units.
        @return the address set that contains addresses for whole code units.
        """
        ...

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
    def getCompatibleAddressRange(range: ghidra.program.model.address.AddressRange, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressRange:
        """
        Convert an address range from one program to a compatible address range in the
         specified otherProgram.  Only memory addresses will be considered.
         If the entire range cannot be converted then null is returned.
        @param range address range to convert
        @param otherProgram target program which corresponds to the returned address range.
        @return translated address range or null if a compatible range could not be
         determined in the other program.
        """
        ...

    @staticmethod
    def getCompatibleAddressSet(set: ghidra.program.model.address.AddressSetView, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSet:
        """
        Convert an address-set from one program to a compatible address-set in the
         specified otherProgram.  Those regions which can not be mapped will be eliminated
         from the new address-set.  Only memory addresses will be considered.
        @param set address-set corresponding to program
        @param otherProgram target program which corresponds to the returned address set.
        @return translated address-set
        """
        ...

    @staticmethod
    def getCompatibleAddressSpace(addrSpace: ghidra.program.model.address.AddressSpace, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSpace: ...

    @staticmethod
    def getCompatibleMemoryAddress(memoryAddress: ghidra.program.model.address.Address, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.address.Address:
        """
        Determines the memory address in the other program that is compatible with the
         specified address.
        @param memoryAddress the memory address to be converted
        @param otherProgram target program which corresponds to the returned address.
        @return the memory address derived from the other program or null if one cannot
         be determined.
        """
        ...

    @staticmethod
    def getCompatibleProgramLocation(program: ghidra.program.model.listing.Program, location: ghidra.program.util.ProgramLocation, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.util.ProgramLocation: ...

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
    def getFunction(function: ghidra.program.model.listing.Function, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.Function:
        """
        Given a function, get the corresponding function from the
         specified otherProgram.  Function matchup is done based upon
         function entry point only.  The function bodies may be different.
        @param function function to look for
        @param otherProgram other program
        @return corresponding function for otherProgram or null if no such function exists.
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
    def getNamespace(namespace: ghidra.program.model.symbol.Namespace, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Namespace:
        """
        Given a namespace, get the corresponding namespace from the
         specified otherProgram.  The return namespace body may be different.
        @param namespace namespace to look for
        @param otherProgram other program
        @return corresponding namespace for otherProgram or null if no such namespace exists.
        """
        ...

    @staticmethod
    def getNonCompatibleAddressSet(set: ghidra.program.model.address.AddressSetView, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSet:
        """
        Reduce an address-set from one program to the set of addresses that are incompatible with
         the specified otherProgram.
        @param set address-set corresponding to one program
        @param otherProgram the addresses are incompatible with this other program.
        @return incompatible address-set
        """
        ...

    @overload
    @staticmethod
    def getReference(p2ToP1Translator: ghidra.program.util.AddressTranslator, p2Ref: ghidra.program.model.symbol.Reference) -> ghidra.program.model.symbol.Reference:
        """
        @param p2ToP1Translator
        @param p2Ref
        @return
        """
        ...

    @overload
    @staticmethod
    def getReference(program: ghidra.program.model.listing.Program, ref: ghidra.program.model.symbol.Reference, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Reference:
        """
        Given a reference for a specified program, get the corresponding reference from the
         specified otherProgram.  A Non-memory reference is considered a suitable reference
         for returning if its destination address is from the same address space (i.e., stack,
         register, etc.)
        @param program program which contains the specified reference instance
        @param ref reference to look for
        @param otherProgram other program
        @return corresponding reference for otherProgram or null if no such reference exists.
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

    @overload
    @staticmethod
    def getUserToAddressString(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns a string representation of the specified address.
        @param program the program containing the address
        @param address the address
        @return the address as a meaningful string for the user.
        """
        ...

    @overload
    @staticmethod
    def getUserToAddressString(program: ghidra.program.model.listing.Program, ref: ghidra.program.model.symbol.Reference) -> unicode:
        """
        Returns the string representation of the specified reference's "to" address.
        @param program the program containing the reference
        @param ref the reference
        @return the "to" address for the reference as a meaningful address for the user.
        """
        ...

    @staticmethod
    def getUserToSymbolString(program: ghidra.program.model.listing.Program, ref: ghidra.program.model.symbol.Reference) -> unicode:
        """
        Returns the string representation of the specified reference's "to" symbol.
        @param program the program containing the reference
        @param ref the reference
        @return the "to" symbol for the reference as a meaningful string for the user.
         The empty string, "", is returned if the reference isn't to a symbol.
        """
        ...

    @overload
    @staticmethod
    def getVariable(var: ghidra.program.model.listing.Variable, otherFunction: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Variable:
        """
        Given a variable, get the corresponding variable from the
         specified otherFunction.
        @param var variable to look for
        @param otherFunction other function
        @return corresponding variable for otherFunction or null if no such variable exists.
        """
        ...

    @overload
    @staticmethod
    def getVariable(program: ghidra.program.model.listing.Program, var: ghidra.program.model.listing.Variable, otherProgram: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.Variable:
        """
        Given a variable for a specified program, get the corresponding variable from the
         specified otherProgram.
        @param program program which contains the specified variable instance
        @param var variable to look for
        @param otherProgram other program
        @return corresponding variable for otherProgram or null if no such variable exists.
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

    @overload
    @staticmethod
    def toSignedHexString(value: long) -> unicode:
        """
        Returns the signed hex string representing the long value.
         Positive values are represented beginning with 0x. (i.e. value of 12 would be 0xc)
         Negative values are represented beginning with -0x. (i.e. value of -12 would be -0xc)
        @param value the value
        @return the signed hex string
        """
        ...

    @overload
    @staticmethod
    def toSignedHexString(value: int) -> unicode:
        """
        Returns the signed hex string representing the int value.
         Positive values are represented beginning with 0x. (i.e. value of 12 would be 0xc)
         Negative values are represented beginning with -0x. (i.e. value of -12 would be -0xc)
        @param value the value
        @return the signed hex string
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def variableStorageMatches(var1: ghidra.program.model.listing.Variable, var2: ghidra.program.model.listing.Variable) -> bool:
        """
        Determine if the specified variables have exactly the same storage.  This method
         should not be used with caution if both arguments are parameters which use dynamically
         mapped storage.
        @param var1
        @param var2
        @return true if variables have matching storage, else false
        """
        ...

    @staticmethod
    def variableStorageOverlaps(var1: ghidra.program.model.listing.Variable, var2: ghidra.program.model.listing.Variable) -> bool:
        """
        Determine if the specified variables have overlapping storage.
         Variable storage check includes dynamically mapped storage for parameters.  This method
         should not be used with caution if both arguments are parameters which use dynamically
         mapped storage.
        @param var1
        @param var2
        @return true if variables overlap, else false
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
