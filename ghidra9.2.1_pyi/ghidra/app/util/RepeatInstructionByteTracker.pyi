import ghidra.app.util
import ghidra.program.model.address
import java.lang


class RepeatInstructionByteTracker(object):
    """
    RepeatInstructionByteTracker provides pseudo-disassemblers the ability to track
     repeated bytes during disassembly of a block of instructions.
    """





    def __init__(self, repeatPatternLimit: int, repeatPatternLimitIgnoredRegion: ghidra.program.model.address.AddressSetView):
        """
        Constructor.
        @param repeatPatternLimit maximum number of instructions containing the same repeated
         byte values.  A value less than or equal to 0 will disable counting.
        @param repeatPatternLimitIgnoredRegion optional set of addresses where check is not
         performed or null for check to be performed everywhere.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def exceedsRepeatBytePattern(self, inst: ghidra.app.util.PseudoInstruction) -> bool:
        """
        Check the next instruction within a block of instructions.
        @param inst next instruction
        @return true if repeat limit has been exceeded, else false.
         If the repeat limit has been set &lt;= 0 false will be returned.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reset(self) -> None:
        """
        Reset internal counter.  This should be performed before disassembling
         a new block of instructions.
        """
        ...

    def setRepeatPatternLimit(self, maxInstructions: int) -> None:
        """
        Set the maximum number of instructions in a single run which contain the same byte values.
        @param maxInstructions limit on the number of consecutive instructions with the same
         byte values.  A non-positive value (&lt;= 0) will disable the
         {@link #exceedsRepeatBytePattern(PseudoInstruction)} checking.
        """
        ...

    def setRepeatPatternLimitIgnored(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Set the region over which the repeat pattern limit will be ignored.
        @param set region over which the repeat pattern limit will be ignored
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
    def repeatPatternLimit(self) -> None: ...  # No getter available.

    @repeatPatternLimit.setter
    def repeatPatternLimit(self, value: int) -> None: ...

    @property
    def repeatPatternLimitIgnored(self) -> None: ...  # No getter available.

    @repeatPatternLimitIgnored.setter
    def repeatPatternLimitIgnored(self, value: ghidra.program.model.address.AddressSetView) -> None: ...
