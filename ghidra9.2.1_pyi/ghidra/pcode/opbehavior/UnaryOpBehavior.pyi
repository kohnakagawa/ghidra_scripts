import ghidra.pcode.opbehavior
import java.lang


class UnaryOpBehavior(ghidra.pcode.opbehavior.OpBehavior):








    def equals(self, __a0: object) -> bool: ...

    @overload
    def evaluateUnary(self, sizeout: int, sizein: int, unsignedIn1: long) -> long:
        """
        Evaluate the unary operation using long data
        @param sizeout intended output size (bytes)
        @param sizein in1 size (bytes)
        @param unsignedIn1 unsigned input 1
        @return operation result.  NOTE: if the operation overflows bits may be
         set beyond the specified sizeout.  Even though results should be treated
         as unsigned it may be returned as a signed long value.  It is expected that the
         returned result always be properly truncated by the caller since the evaluation
         may not - this is done to conserve emulation cycles.
        @see Utils#longToBytes(long, int, boolean)
        @see Utils#bytesToLong(byte[], int, boolean)
        """
        ...

    @overload
    def evaluateUnary(self, sizeout: int, sizein: int, unsignedIn1: long) -> long:
        """
        Evaluate the unary operation using long data
        @param sizeout intended output size (bytes)
        @param sizein in1 size (bytes)
        @param unsignedIn1 unsigned input 1
        @return operation result.  NOTE: if the operation overflows bits may be
         set beyond the specified sizeout.  Even though results should be treated
         as unsigned it may be returned as a signed long value.  It is expected that the
         returned result always be properly truncated by the caller since the evaluation
         may not - this is done to conserve emulation cycles.
        @see Utils#longToBytes(long, int, boolean)
        @see Utils#bytesToLong(byte[], int, boolean)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getOpCode(self) -> int: ...

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
