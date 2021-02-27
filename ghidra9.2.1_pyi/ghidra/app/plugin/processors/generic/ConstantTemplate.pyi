import ghidra.app.plugin.processors.generic
import java.io
import java.lang
import java.util


class ConstantTemplate(object, java.io.Serializable):
    HANDLE: int = 2
    JUMP_CODESPACE: int = 5
    JUMP_NEXT: int = 4
    JUMP_START: int = 3
    REAL: int = 1



    @overload
    def __init__(self, val: long): ...

    @overload
    def __init__(self, t: int): ...

    @overload
    def __init__(self, o: ghidra.app.plugin.processors.generic.Operand, sel1: int):
        """
        Constructor ConstantTemplate.
        @param o the operand
        @param sel1 the first selection
        """
        ...

    @overload
    def __init__(self, o: ghidra.app.plugin.processors.generic.Operand, sel1: int, sel2: int): ...



    def equals(self, o: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def operand(self) -> ghidra.app.plugin.processors.generic.Operand: ...

    @overload
    def resolve(self, position: ghidra.app.plugin.processors.generic.Position, off: int) -> long:
        """
        Method resolve.
        @param position the position of the constant to resolve
        @param off the offset of the constant
        @return long
        """
        ...

    @overload
    def resolve(self, handles: java.util.HashMap, position: ghidra.app.plugin.processors.generic.Position, off: int) -> long:
        """
        @param handles optional map of handles to be used for resolving
        @see #resolve(Position, int)
        @return long
        """
        ...

    def select1(self) -> int: ...

    def select2(self) -> int: ...

    def toString(self) -> unicode: ...

    def type(self) -> int: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
