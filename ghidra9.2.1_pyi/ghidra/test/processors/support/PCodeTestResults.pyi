import java.lang
import java.util


class PCodeTestResults(object):
    TAG_NAME: unicode



    def __init__(self, root: org.jdom.Element): ...



    def equals(self, __a0: object) -> bool: ...

    def getCallOtherResult(self, groupName: unicode, testName: unicode) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getFailResult(self, groupName: unicode, testName: unicode) -> int: ...

    def getGroupTestNames(self) -> java.util.Collection:
        """
        @return collection of group/testNames in the form {@code "<groupName>.<testName>"}
        """
        ...

    def getJUnitName(self) -> unicode: ...

    def getNumberOfTests(self) -> int: ...

    def getPassResult(self, groupName: unicode, testName: unicode) -> int: ...

    def getTime(self) -> unicode: ...

    def getTotalAsserts(self, groupName: unicode, testName: unicode) -> int: ...

    def hadSevereFailure(self, groupName: unicode, testName: unicode) -> bool: ...

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
    def JUnitName(self) -> unicode: ...

    @property
    def groupTestNames(self) -> java.util.Collection: ...

    @property
    def numberOfTests(self) -> int: ...

    @property
    def time(self) -> unicode: ...