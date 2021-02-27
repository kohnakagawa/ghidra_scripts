import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.symbol
import java.lang


class CodeBlockReference(object):
    """
    A CodeBlockReference represents the flow from one CodeBlock to another. Flow
     consists of:

     The source and destination CodeBlocks
     The Type of flow (JMP, CALL, Fallthrough, etc...
     The referent - the instruction's address in the source block that causes
     the flow
     The reference - the address in the destination block that is flowed to.


    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the Destination Block address.
         The destination address should only occur in one block.
        @return the Destination Block address
        """
        ...

    def getDestinationBlock(self) -> ghidra.program.model.block.CodeBlock:
        """
        Returns the Destination CodeBlock.
        @return the Destination CodeBlock
        """
        ...

    def getFlowType(self) -> ghidra.program.model.symbol.FlowType:
        """
        Returns the type of flow from the Source to the Destination CodeBlock.
        @return the type of flow
        """
        ...

    def getReference(self) -> ghidra.program.model.address.Address:
        """
        Returns the address in the Destination block that is referenced by the Source block.
        @return the address in the Destination block that is referenced by the Source block
        """
        ...

    def getReferent(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the instruction in the Source Block that refers to the Destination block.
        @return the address of the instruction in the Source Block that refers to the Destination block
        """
        ...

    def getSourceAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the Source Block address.
         The source address should only occur in one block.
        @return the Source Block address
        """
        ...

    def getSourceBlock(self) -> ghidra.program.model.block.CodeBlock:
        """
        Returns the Source CodeBlock.
        @return the Source CodeBlock
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
    def destinationAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def destinationBlock(self) -> ghidra.program.model.block.CodeBlock: ...

    @property
    def flowType(self) -> ghidra.program.model.symbol.FlowType: ...

    @property
    def reference(self) -> ghidra.program.model.address.Address: ...

    @property
    def referent(self) -> ghidra.program.model.address.Address: ...

    @property
    def sourceAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def sourceBlock(self) -> ghidra.program.model.block.CodeBlock: ...
