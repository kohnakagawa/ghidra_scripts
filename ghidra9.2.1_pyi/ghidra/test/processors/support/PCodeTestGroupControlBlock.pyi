import ghidra.program.model.address
import ghidra.test.processors.support
import ghidra.test.processors.support.PCodeTestAbstractControlBlock
import java.lang


class PCodeTestGroupControlBlock(ghidra.test.processors.support.PCodeTestAbstractControlBlock):
    """
    PCodeTestGroupControlBlock corresponds to each test group contained within
     a binary test file and identified by the GROUP_CONTROL_BLOCK_MAGIC 64-bit character
     field value at the start of the data structure.
    """

    mainTestControlBlock: ghidra.test.processors.support.PCodeTestControlBlock







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getFunctionInfo(self, functionIndex: int) -> ghidra.test.processors.support.PCodeTestAbstractControlBlock.FunctionInfo: ...

    @overload
    def getFunctionInfo(self, functionName: unicode) -> ghidra.test.processors.support.PCodeTestAbstractControlBlock.FunctionInfo: ...

    def getInfoStructureAddress(self) -> ghidra.program.model.address.Address: ...

    def getNumberFunctions(self) -> int: ...

    def getTestGroupMainAddress(self) -> ghidra.program.model.address.Address: ...

    def getTestGroupName(self) -> unicode: ...

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
    def testGroupMainAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def testGroupName(self) -> unicode: ...
