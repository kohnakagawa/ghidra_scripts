import java.lang
import java.util
import java.util.function


class DecompilerConcurrentQ(object):




    @overload
    def __init__(self, __a0: generic.concurrent.QCallback, __a1: ghidra.util.task.TaskMonitor): ...

    @overload
    def __init__(self, __a0: generic.concurrent.QCallback, __a1: unicode, __a2: ghidra.util.task.TaskMonitor): ...



    def add(self, __a0: object) -> None: ...

    @overload
    def addAll(self, __a0: java.util.Collection) -> None: ...

    @overload
    def addAll(self, __a0: java.util.Iterator) -> None: ...

    @overload
    def dispose(self) -> None: ...

    @overload
    def dispose(self, __a0: long) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process(self, __a0: java.util.Iterator, __a1: java.util.function.Consumer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def waitForResults(self) -> java.util.Collection: ...

    def waitUntilDone(self) -> None: ...
