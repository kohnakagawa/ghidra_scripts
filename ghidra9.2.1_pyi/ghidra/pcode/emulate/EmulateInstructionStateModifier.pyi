from typing import List
import ghidra.pcode.emulate
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.pcode
import java.lang


class EmulateInstructionStateModifier(object):
    """
    EmulateInstructionStateModifier defines a language specific
     handler to assist emulation with adjusting the current execution state,
     providing support for custom pcodeop's (i.e., CALLOTHER).
     The implementation of this interface must provide a public constructor which
     takes a single Emulate argument.
    """









    def equals(self, __a0: object) -> bool: ...

    def executeCallOther(self, op: ghidra.program.model.pcode.PcodeOp) -> bool:
        """
        Execute a CALLOTHER op
        @param op
        @return true if corresponding pcodeop was registered and emulation support is
         performed, or false if corresponding pcodeop is not supported by this class.
        @throws LowlevelError
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def initialExecuteCallback(self, emulate: ghidra.pcode.emulate.Emulate, current_address: ghidra.program.model.address.Address, contextRegisterValue: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Emulation callback immediately before the first instruction is executed.
         This callback permits any language specific initializations to be performed.
        @param emulate
        @param current_address intial execute address
        @param contextRegisterValue initial context value or null if not applicable or unknown
        @throws LowlevelError
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def postExecuteCallback(self, emulate: ghidra.pcode.emulate.Emulate, lastExecuteAddress: ghidra.program.model.address.Address, lastExecutePcode: List[ghidra.program.model.pcode.PcodeOp], lastPcodeIndex: int, currentAddress: ghidra.program.model.address.Address) -> None:
        """
        Emulation callback immediately following execution of the lastExecuteAddress.
         One use of this callback is to modify the flowing/future context state.
        @param emulate
        @param lastExecuteAddress
        @param lastExecutePcode
        @param lastPcodeIndex pcode index of last op or -1 if no pcode or fall-through occurred.
        @param currentAddress
        @throws LowlevelError
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
