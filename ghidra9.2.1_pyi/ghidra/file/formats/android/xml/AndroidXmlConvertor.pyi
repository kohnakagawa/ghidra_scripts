import ghidra.util.task
import java.io
import java.lang


class AndroidXmlConvertor(object):
    ANDROID_BINARY_XML_MAGIC: List[int] = array('b', [3, 0, 8, 0])
    ANDROID_BINARY_XML_MAGIC_LEN: int = 4



    def __init__(self): ...



    @staticmethod
    def convert(__a0: java.io.InputStream, __a1: java.io.PrintWriter, __a2: ghidra.util.task.TaskMonitor) -> None: ...

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
