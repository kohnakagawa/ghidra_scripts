from typing import List
import ghidra.test.processors.support
import java.lang


class PCodeTestGroup(object, java.lang.Comparable):
    """
    PCodeTestGroup identifies a test group function and its corresponding
     PCodeTestGroupControlBlock.
    """

    FUNCTION_NAME_PREFIX: unicode = u'main_'
    controlBlock: ghidra.test.processors.support.PCodeTestGroupControlBlock
    functionEntryPtr: ghidra.program.model.address.Address
    mainTestControlBlock: ghidra.test.processors.support.PCodeTestControlBlock
    testGroupName: unicode







    @overload
    def compareTo(self, o: ghidra.test.processors.support.PCodeTestGroup) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTestFailures(self) -> List[unicode]:
        """
        @return list of recorded emulation test failures
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
    def testFailures(self) -> List[object]: ...
