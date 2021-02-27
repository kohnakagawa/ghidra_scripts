import ghidra.program.model.address
import ghidra.test.processors.support
import ghidra.test.processors.support.PCodeTestAbstractControlBlock
import java.lang


class PCodeTestAbstractControlBlock(object):
    """
    PCodeTestAbstractControlBlock data is models the general capabilities
     of the TestInfo data structure which is used for different puposes as handled
     by extensions of this class.
    """






    class FunctionInfo(object, java.lang.Comparable):
        functionAddr: ghidra.program.model.address.Address
        functionName: unicode
        numberOfAsserts: int







        @overload
        def compareTo(self, __a0: ghidra.test.processors.support.PCodeTestAbstractControlBlock.FunctionInfo) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

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







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getFunctionInfo(self, functionIndex: int) -> ghidra.test.processors.support.PCodeTestAbstractControlBlock.FunctionInfo: ...

    @overload
    def getFunctionInfo(self, functionName: unicode) -> ghidra.test.processors.support.PCodeTestAbstractControlBlock.FunctionInfo: ...

    def getInfoStructureAddress(self) -> ghidra.program.model.address.Address: ...

    def getNumberFunctions(self) -> int: ...

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
    def infoStructureAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def numberFunctions(self) -> int: ...
