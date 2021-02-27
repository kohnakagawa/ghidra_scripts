import ghidra.program.model.listing
import java.lang


class ParallelInstructionLanguageHelper(object):
    """
    ParallelInstructionLanguageHelper provides the ability via a language
     specified property to identify certain parallel instruction attributes.
     Implementations must define a public default constructor.

     The following assumptions exist for parallel packets/groups of instructions:

     All instructions in a packet/group which are not the last instruction in the
     packet/group must have a fall-through.

    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMnemonicPrefix(self, instr: ghidra.program.model.listing.Instruction) -> unicode:
        """
        Return the mnemonic prefix (i.e., || ) for the specified instriction.
        @param instr
        @return mnemonic prefix or null if not applicable
        """
        ...

    def hashCode(self) -> int: ...

    def isEndOfParallelInstructionGroup(self, instruction: ghidra.program.model.listing.Instruction) -> bool:
        """
        Determine if the specified instruction is the last instruction in a parallel
         instruction group.  The group is defined as a sequential set of instructions
         which are executed in parallel.  It is assumed that all terminal flows
         will only be present in the semantics of the last instruction in a parallel
         group.
         <p>
         This method is primarily intended to assist disassembly to keep parallel
         instruction packets/groups intact within a single InstructionBlock to
         facilitate the pcode crossbuild directive.  Such cases are expected to
         defer all flows to the last instruction in the packet and flows should never
         have a destination in the middle of a packet/group.  If pcode crossbuild's
         are never utilized this method may always return false.
        @param instruction
        @return true if instruction is last in a parallel group or if no other
         instruction is executed in parallel with the specified instruction.
        """
        ...

    def isParallelInstruction(self, instruction: ghidra.program.model.listing.Instruction) -> bool:
        """
        Determine if the specified instruction is executed in parallel with
         the instruction preceding it.
        @param instruction
        @return true if parallel else false
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
