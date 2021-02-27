import ghidra.test.processors.support
import java.lang


class PCodeTestCombinedTestResults(object):
    FILENAME: unicode = u'pcode_test_results'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTestResults(self, jUnitName: unicode, create: bool) -> ghidra.test.processors.support.PCodeTestResults: ...

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
