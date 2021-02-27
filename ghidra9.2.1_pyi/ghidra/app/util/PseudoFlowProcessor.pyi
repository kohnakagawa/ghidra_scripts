import ghidra.app.util
import java.lang


class PseudoFlowProcessor(object):
    """
    Defines methods for flow as if the code were actually being disassembled.
    """









    def equals(self, __a0: object) -> bool: ...

    def followFlows(self, instr: ghidra.app.util.PseudoInstruction) -> bool:
        """
        Return true if the flows should be followed from this instruction
        @param instr instruction to test
        @return false if flows should not be followed
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process(self, instr: ghidra.app.util.PseudoInstruction) -> bool:
        """
        Process this instruction; return false if instr terminates.
        @param instr instruction to check
        @return false when the processing should stop
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
