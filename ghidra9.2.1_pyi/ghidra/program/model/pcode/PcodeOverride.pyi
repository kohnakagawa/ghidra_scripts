import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class PcodeOverride(object):








    def equals(self, __a0: object) -> bool: ...

    def getCallFixup(self, callDestAddr: ghidra.program.model.address.Address) -> ghidra.program.model.lang.InjectPayload:
        """
        Returns the call-fixup for a specified call destination.
         If the destination function has not be tagged or was tagged
         with an unknown CallFixup name this method will return null.
        @param callDestAddr call destination address.  This address is used to
         identify a function which may have been tagged with a CallFixup.
        @return call fixup object or null
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFallThroughOverride(self) -> ghidra.program.model.address.Address:
        """
        Get the fall-through override address which may have been
         applied to the current instruction.
        @return fall-through override address or null
        """
        ...

    def getFlowOverride(self) -> ghidra.program.model.listing.FlowOverride:
        """
        Get the flow override which may have been applied
         to the current instruction.
        @return flow override or null
        """
        ...

    def getInstructionStart(self) -> ghidra.program.model.address.Address:
        """
        @return current instruction address
        """
        ...

    def getOverridingReference(self, type: ghidra.program.model.symbol.RefType) -> ghidra.program.model.address.Address:
        """
        Get the primary overriding reference address of {@link RefType} {@code type} from
         the current instruction
        @param type type of reference
        @return call reference address or null
        """
        ...

    def getPrimaryCallReference(self) -> ghidra.program.model.address.Address:
        """
        Get the primary call reference address from the current instruction
        @return call reference address or null
        """
        ...

    def hasCallFixup(self, callDestAddr: ghidra.program.model.address.Address) -> bool:
        """
        Returns the call-fixup for a specified call destination.
        @param callDestAddr call destination address.  This address is used to
         identify a function which may have been tagged with a CallFixup.
        @return true if call destination function has been tagged with a call-fixup
        """
        ...

    def hasPotentialOverride(self) -> bool:
        """
        Returns a boolean indicating whether there are any primary overriding references at the current
         instruction
        @return are there primary overriding references
        """
        ...

    def hashCode(self) -> int: ...

    def isCallOtherCallOverrideRefApplied(self) -> bool:
        """
        Returns a boolean indicating whether a callother call override has been applied at the current
         instruction
        @return has callother call override been applied
        """
        ...

    def isCallOtherJumpOverrideApplied(self) -> bool:
        """
        Returns a boolean indicating whether a callother jump override has been applied at the current
         instruction
        @return has callother jump override been applied
        """
        ...

    def isCallOverrideRefApplied(self) -> bool:
        """
        Returns a boolean indicating whether a call override has been applied at the current instruction
        @return has call override been applied
        """
        ...

    def isJumpOverrideRefApplied(self) -> bool:
        """
        Returns a boolean indicating whether a jump override has been applied at the current instruction
        @return has jump override been applied
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCallOtherCallOverrideRefApplied(self) -> None:
        """
        Register that a callother call override has been applied at the current instruction
        """
        ...

    def setCallOtherJumpOverrideRefApplied(self) -> None:
        """
        Register that a callother jump override has been applied at the current instruction
        """
        ...

    def setCallOverrideRefApplied(self) -> None:
        """
        Register that a call override has been applied at the current instruction.
        """
        ...

    def setJumpOverrideRefApplied(self) -> None:
        """
        Register that a jump override has been applied at the current instruction
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
    def callOtherCallOverrideRefApplied(self) -> bool: ...

    @property
    def callOtherJumpOverrideApplied(self) -> bool: ...

    @property
    def callOverrideRefApplied(self) -> bool: ...

    @property
    def fallThroughOverride(self) -> ghidra.program.model.address.Address: ...

    @property
    def flowOverride(self) -> ghidra.program.model.listing.FlowOverride: ...

    @property
    def instructionStart(self) -> ghidra.program.model.address.Address: ...

    @property
    def jumpOverrideRefApplied(self) -> bool: ...

    @property
    def primaryCallReference(self) -> ghidra.program.model.address.Address: ...
