import ghidra.app.decompiler
import java.lang


class DecompileConfigurer(object):
    """
    A callback interface that will be given a newly created DecompInterface to
     configure.
    """









    def configure(self, decompiler: ghidra.app.decompiler.DecompInterface) -> None:
        """
        Configure the given decompiler
        @param decompiler the decompiler to configure
        """
        ...

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
