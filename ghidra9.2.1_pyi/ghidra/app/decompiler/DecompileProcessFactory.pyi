import ghidra.app.decompiler
import java.lang


class DecompileProcessFactory(object):
    """
    Factory that returns a DecompileProcess.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get() -> ghidra.app.decompiler.DecompileProcess: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def release(dp: ghidra.app.decompiler.DecompileProcess) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
