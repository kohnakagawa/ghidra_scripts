import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import java.lang


class InstructionContext(object):
    """
    InstructionContext is utilized by a shared instruction prototype to
     access all relevant instruction data and context-register storage needed during
     instruction parse and semantic pcode generation.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the instruction address that this context corresponds to.
        @return instruction address
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMemBuffer(self) -> ghidra.program.model.mem.MemBuffer:
        """
        Get the read-only memory buffer containing the instruction bytes.  Its position will
         correspond to the instruction address.
        @return instruction memory buffer
        """
        ...

    @overload
    def getParserContext(self) -> ghidra.program.model.lang.ParserContext:
        """
        Get the instruction parser context for the instruction which corresponds to this
         context object.
        @return the instruction parser context for the instruction which corresponds to this
         context object.
        @throws MemoryAccessException if memory error occurred while resolving instruction
         details.
        """
        ...

    @overload
    def getParserContext(self, instructionAddress: ghidra.program.model.address.Address) -> ghidra.program.model.lang.ParserContext:
        """
        Get the instruction parser context which corresponds to the specified instruction
         address.  This may be obtained via either caching or by parsing the instruction
         at the specified address.  The returned ParserContext may be cast to the prototype's
         implementation without checking.  This method will throw an UnknownContextException
         if a compatible ParserContext is not found at the specified address.
        @return the instruction parser context at the specified instruction address
        @throws UnknownContextException if the instruction at the specified address
         was not previously parsed or attempting to instantiate context resulted in an
         exception.
        @throws MemoryAccessException if memory error occurred while resolving instruction
         details.
        """
        ...

    def getProcessorContext(self) -> ghidra.program.model.lang.ProcessorContextView:
        """
        Get the read-only processor context containing the context-register state
         state at the corresponding instruction.  This is primarily used during the
         parse phase to provide the initial context-register state.
        @return the read-only processor context
        """
        ...

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

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def memBuffer(self) -> ghidra.program.model.mem.MemBuffer: ...

    @property
    def parserContext(self) -> ghidra.program.model.lang.ParserContext: ...

    @property
    def processorContext(self) -> ghidra.program.model.lang.ProcessorContextView: ...
