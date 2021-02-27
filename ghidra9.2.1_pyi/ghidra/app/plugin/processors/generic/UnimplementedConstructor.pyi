import ghidra.app.plugin.processors.generic
import java.lang
import java.util


class UnimplementedConstructor(ghidra.app.plugin.processors.generic.ConstructorPcodeTemplate):
    """
    Template for a constructor which is officially "unimplemented" as opposed to a
     constructor which does nothing (like a NOP). Any instruction which is "unimplemented"
     in this way will have its disassembly printed correctly but will be treated as an
     instruction which does nothing (and falls through) for any analysis that needs
     control-flow information or semantics. Actually anything that tries to get semantic
     information (via the getPcode call) will cause an exception to be thrown, as opposed
     to a NOP instruction which would return an empty pcode op array. The caller can then
     catch the exception and treat the instruction as special, or it can ignore the exception
     in which case the instruction behaves exactly like a NOP.
    """





    def __init__(self): ...



    def addPcodeOpTemplate(self, opT: object) -> None: ...

    def delaySlotDepth(self) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlowFlags(self) -> int: ...

    def getPcode(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int, __a3: java.util.ArrayList) -> ghidra.app.plugin.processors.generic.Handle: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optimize(self) -> None:
        """
        The default pcode generated for a constructor is typically
         not very efficient.  For example, for an add instruction,
         we might generate something like

         tmp1 = LOAD register_space register1
         tmp2 = LOAD register_space register2
         tmp3 = ADD tmp1 tmp2
                STORE register_space register3 tmp3

         This routine marks opcodes and varnodes as potentially omitable,
         which allows us to generate much simpler pcode whenever there
         are no dynamic references involved.  In the case above we would
         replace the 4 pcode ops above with a single pcode op:

         register3 = ADD register1 register2
        """
        ...

    def result(self) -> ghidra.app.plugin.processors.generic.HandleTemplate: ...

    def toString(self) -> unicode: ...

    def trimToSize(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
