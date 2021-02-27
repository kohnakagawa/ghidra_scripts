from typing import List
import ghidra.pcode.emulate
import ghidra.program.model.pcode
import java.lang


class OpBehaviorOther(object):








    def equals(self, __a0: object) -> bool: ...

    def evaluate(self, emu: ghidra.pcode.emulate.Emulate, out: ghidra.program.model.pcode.Varnode, inputs: List[ghidra.program.model.pcode.Varnode]) -> None:
        """
        Evaluate the CALLOTHER op which corresponds to this behavior.
        @param emu emulator which contains associated memory state
        @param out output varnode or null if no assignment has been
         made.  Implementation is responsible for updating memory
         state appropriately.
        @param inputs input varnodes passed as parameters to this
         pcodeop.  The inputs[0] value corresponds to the index value of this
         pcodeop and can generally be ignored.  The inputs[1] value
         corresponds to the first (leftmost) parameter passed to
         this pcodeop within the language implementation.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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
