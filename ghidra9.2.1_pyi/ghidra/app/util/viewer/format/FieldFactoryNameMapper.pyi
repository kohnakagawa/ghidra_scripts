from typing import List
import ghidra.app.util.viewer.field
import java.lang


class FieldFactoryNameMapper(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFactoryPrototype(fieldName: unicode, prototypeFactories: List[ghidra.app.util.viewer.field.FieldFactory]) -> ghidra.app.util.viewer.field.FieldFactory: ...

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
