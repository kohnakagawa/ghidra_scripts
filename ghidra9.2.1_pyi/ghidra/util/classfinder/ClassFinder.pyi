import java.lang


class ClassFinder(object):
    """
    Finds extension classes in the classpath
    """





    def __init__(self, __a0: List[object], __a1: ghidra.util.task.TaskMonitor): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isClassOfInterest(c: java.lang.Class) -> bool:
        """
        Checks to see if the given class is an extension point of interest.
        @param c The class to check.
        @return True if the given class is an extension point of interest; otherwise, false.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
