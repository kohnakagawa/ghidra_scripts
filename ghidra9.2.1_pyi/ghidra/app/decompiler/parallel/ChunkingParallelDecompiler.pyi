from typing import List
import java.lang


class ChunkingParallelDecompiler(object):
    """
    A class that simplifies some the concurrent datastructure setup required for decompiling
     functions.  This class is meant to be used when you wish to decompile functions in groups
     (or chunks) rather than decompiling all functions at once.
    """









    def decompileFunctions(self, __a0: List[object]) -> List[object]: ...

    def dispose(self) -> None: ...

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
