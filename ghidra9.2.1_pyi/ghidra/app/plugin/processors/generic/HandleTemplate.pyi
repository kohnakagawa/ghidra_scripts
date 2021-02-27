import ghidra.app.plugin.processors.generic
import java.io
import java.lang
import java.util


class HandleTemplate(object, java.io.Serializable):




    def __init__(self, sp: ghidra.app.plugin.processors.generic.ConstantTemplate, p: ghidra.app.plugin.processors.generic.VarnodeTemplate, sz: ghidra.app.plugin.processors.generic.ConstantTemplate): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def resolve(self, position: ghidra.app.plugin.processors.generic.Position, off: int) -> ghidra.app.plugin.processors.generic.Handle:
        """
        @param position
        @param off
        @return
        """
        ...

    @overload
    def resolve(self, handles: java.util.HashMap, position: ghidra.app.plugin.processors.generic.Position, off: int) -> ghidra.app.plugin.processors.generic.Handle:
        """
        Method resolve.
        @param handles
        @return HandleTemplate
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
