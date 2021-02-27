from typing import List
import ghidra.app.util.viewer.field
import ghidra.program.model.listing
import java.lang


class FunctionUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getCallingConventionSignatureOffset(__a0: ghidra.program.model.listing.Function) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFunctionNameStringInfo(__a0: ghidra.program.model.listing.Function, __a1: unicode) -> ghidra.app.util.viewer.field.FieldStringInfo: ...

    @staticmethod
    def getFunctionParameterStringInfos(__a0: ghidra.program.model.listing.Function, __a1: unicode) -> List[ghidra.app.util.viewer.field.FieldStringInfo]: ...

    @staticmethod
    def getFunctionReturnTypeStringInfo(__a0: ghidra.program.model.listing.Function, __a1: unicode) -> ghidra.app.util.viewer.field.FieldStringInfo: ...

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
