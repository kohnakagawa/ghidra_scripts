import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.symbol
import java.lang


class CodeBlockReferenceImpl(object, ghidra.program.model.block.CodeBlockReference):
    """
    CodeBlockReferenceImpl implements a CodeBlockReference.

      A CodeBlockReference represents the flow from one source block
     to a destination block, including information about how
     flow occurs between the two blocks (JUMP, CALL, etc..).

      The reference is the address in the destination
     block that is actually flowed to by some instruction in the source block.

      The referent is the address of the instruction in
     the source block that flows to the destination block.

    """





    def __init__(self, source: ghidra.program.model.block.CodeBlock, destination: ghidra.program.model.block.CodeBlock, flowType: ghidra.program.model.symbol.FlowType, reference: ghidra.program.model.address.Address, referent: ghidra.program.model.address.Address):
        """
        Constructor for a CodeBlockReferenceImpl
        @param source source block for this flow
        @param destination destination block for this flow
        @param flowType how we flow
        @param reference reference address in destination block
        @param referent address of instruction in source block that flows to destination block.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.block.CodeBlockReference#getDestinationAddress()
        """
        ...

    def getDestinationBlock(self) -> ghidra.program.model.block.CodeBlock:
        """
        @see ghidra.program.model.block.CodeBlockReference#getDestinationBlock()
        """
        ...

    def getFlowType(self) -> ghidra.program.model.symbol.FlowType:
        """
        @see ghidra.program.model.block.CodeBlockReference#getFlowType()
        """
        ...

    def getReference(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.block.CodeBlockReference#getReference()
        """
        ...

    def getReferent(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.block.CodeBlockReference#getReferent()
        """
        ...

    def getSourceAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.block.CodeBlockReference#getSourceAddress()
        """
        ...

    def getSourceBlock(self) -> ghidra.program.model.block.CodeBlock:
        """
        @see ghidra.program.model.block.CodeBlockReference#getSourceBlock()
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
