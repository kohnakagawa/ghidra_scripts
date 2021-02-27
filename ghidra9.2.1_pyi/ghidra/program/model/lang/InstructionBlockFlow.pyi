from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.lang.InstructionBlockFlow
import java.lang


class InstructionBlockFlow(object, java.lang.Comparable):





    class Type(java.lang.Enum):
        BRANCH: ghidra.program.model.lang.InstructionBlockFlow.Type = BRANCH
        CALL: ghidra.program.model.lang.InstructionBlockFlow.Type = CALL
        CALL_FALLTHROUGH: ghidra.program.model.lang.InstructionBlockFlow.Type = CALL_FALLTHROUGH
        PRIORITY: ghidra.program.model.lang.InstructionBlockFlow.Type = PRIORITY







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.program.model.lang.InstructionBlockFlow.Type: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.lang.InstructionBlockFlow.Type]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, address: ghidra.program.model.address.Address, flowFrom: ghidra.program.model.address.Address, type: ghidra.program.model.lang.InstructionBlockFlow.Type): ...



    @overload
    def compareTo(self, o: ghidra.program.model.lang.InstructionBlockFlow) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the flow destination address
        @return flow destination address
        """
        ...

    def getFlowFromAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the flow from address
        @return flow from address (may be null)
        """
        ...

    def getType(self) -> ghidra.program.model.lang.InstructionBlockFlow.Type:
        """
        @return flow type
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
    def flowFromAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def type(self) -> ghidra.program.model.lang.InstructionBlockFlow.Type: ...
