import java.lang


class RtlPair(object):
    scope: ghidra.pcodeCPort.slghsymbol.SymbolScope
    section: ghidra.pcodeCPort.semantics.ConstructTpl



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: ghidra.pcodeCPort.semantics.ConstructTpl, __a1: ghidra.pcodeCPort.slghsymbol.SymbolScope): ...



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
