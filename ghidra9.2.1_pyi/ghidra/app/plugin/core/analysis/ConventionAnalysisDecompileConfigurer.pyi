import ghidra.app.decompiler
import ghidra.app.decompiler.parallel
import java.lang


class ConventionAnalysisDecompileConfigurer(object, ghidra.app.decompiler.parallel.DecompileConfigurer):








    def configure(self, __a0: ghidra.app.decompiler.DecompInterface) -> None: ...

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
