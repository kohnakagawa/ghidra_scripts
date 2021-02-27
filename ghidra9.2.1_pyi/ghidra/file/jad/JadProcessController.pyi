from typing import List
import ghidra.app.util.importer
import ghidra.file.jad
import ghidra.util.task
import java.lang


class JadProcessController(object):





    class DisposeState(java.lang.Enum):
        DISPOSED_ON_CANCEL: ghidra.file.jad.JadProcessController.DisposeState = DISPOSED_ON_CANCEL
        DISPOSED_ON_TIMEOUT: ghidra.file.jad.JadProcessController.DisposeState = DISPOSED_ON_TIMEOUT
        ENDED_HAPPY: ghidra.file.jad.JadProcessController.DisposeState = ENDED_HAPPY
        NOT_DISPOSED: ghidra.file.jad.JadProcessController.DisposeState = NOT_DISPOSED







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
        def valueOf(__a0: unicode) -> ghidra.file.jad.JadProcessController.DisposeState: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.file.jad.JadProcessController.DisposeState]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.file.jad.JadProcessWrapper, __a1: unicode): ...



    def decompile(self, __a0: int, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMessages(self) -> ghidra.app.util.importer.MessageLog: ...

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
    def messages(self) -> ghidra.app.util.importer.MessageLog: ...
