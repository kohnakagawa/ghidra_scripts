import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.program.util
import java.lang


class ContextEvaluator(object):
    """
    ContextEvaluator provides a callback mechanism for the SymbolicPropogator as code is evaluated.
    """









    def allowAccess(self, context: ghidra.program.util.VarnodeContext, addr: ghidra.program.model.address.Address) -> bool:
        """
        Evaluate the address and check if the access to the value in the memory location to be read
         The address is read-only and is not close to this address.
        @param context current program context
        @param addr Address of memory where location is attempting to be read
        @return true if the access should be allowed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def evaluateConstant(self, context: ghidra.program.util.VarnodeContext, instr: ghidra.program.model.listing.Instruction, pcodeop: int, constant: ghidra.program.model.address.Address, size: int, refType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.address.Address:
        """
        Evaluate a potential constant to be used as an address or an interesting constant that
         should have a reference created for it.  Computed values that are not know to be used as an address will
         be passed to this function.  For example a value passed to a function, or a stored constant value.
        @param context current program context
        @param instr instruction on which this reference was detected
        @param pcodeop the PcodeOp operation that is causing this potential constant
        @param constant constant value (in constant.getOffset() )
        @param size size of constant value in bytes
        @param refType reference type (flow, data/read/write)
        @return the original address unchanged if it should be a reference
                 null if the constant reference should not be created
                 a new address if the value should be a different address or address space
                     Using something like instr.getProgram().getAddressFactory().getDefaultAddressSpace();
        """
        ...

    def evaluateContext(self, context: ghidra.program.util.VarnodeContext, instr: ghidra.program.model.listing.Instruction) -> bool:
        """
        Evaluate the current instruction given the final context for the instruction
        @param context describes current state of registers
        @param instr instruction whose context has been applied
        @return true if evaluation should stop, false to continue evaluation
        """
        ...

    def evaluateContextBefore(self, context: ghidra.program.util.VarnodeContext, instr: ghidra.program.model.listing.Instruction) -> bool:
        """
        Evaluate the current instruction given the context before the instruction is evaluated
        @param context describes current state of registers
        @param instr instruction whose context has not yet been applied
        @return true if evaluation should stop
        """
        ...

    def evaluateDestination(self, context: ghidra.program.util.VarnodeContext, instruction: ghidra.program.model.listing.Instruction) -> bool:
        """
        Evaluate the instruction for an unknown destination
        @param context current register context
        @param instruction instruction that has an unknown destination
        @return true if the evaluation should stop, false to continue evaluation
        """
        ...

    def evaluateReference(self, context: ghidra.program.util.VarnodeContext, instr: ghidra.program.model.listing.Instruction, pcodeop: int, address: ghidra.program.model.address.Address, size: int, refType: ghidra.program.model.symbol.RefType) -> bool:
        """
        Evaluate the reference that has been found on this instruction. Computed values that are used as an
         address will be passed to this function.  For example a value passed to a function, or a stored
         constant value.
        @param context current program context
        @param instr instruction on which this reference was detected
        @param pcodeop the PcodeOp operation that is causing this reference
        @param address address being referenced
        @param size size of the item being referenced (only non-zero if load or store of data)
        @param refType reference type (flow, data/read/write)
        @return false if the reference should be ignored (or has been taken care of by this routine)
        """
        ...

    def evaluateSymbolicReference(self, context: ghidra.program.util.VarnodeContext, instr: ghidra.program.model.listing.Instruction, address: ghidra.program.model.address.Address) -> bool:
        """
        Evaluate the reference that has been found on this instruction that points into an unknown space that
         has been designated as tracked.
        @param context current program context
        @param instr instruction on which this reference was detected
        @param address address being referenced
        @return false if the reference should be ignored (or has been taken care of by this routine)
                 true to allow the reference to be created
        """
        ...

    def followFalseConditionalBranches(self) -> bool:
        """
        Follow all branches, even if the condition evaluates to false, indicating it shouldn't be followed.
        @return true if false evaluated conditional branches should be followed.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def unknownValue(self, context: ghidra.program.util.VarnodeContext, instruction: ghidra.program.model.listing.Instruction, node: ghidra.program.model.pcode.Varnode) -> long:
        """
        Called when a value is needed for a register that is unknown
        @param context current register context
        @param instruction instruction that has an unknown destination
        @param node varnode for the register being accessed to obtain a value
        @return null if the varnode should not have an assumed value.
                 a long value if the varnode such as a Global Register should have an assumed constant
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
