from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class InjectPayloadDexRange(object, ghidra.program.model.lang.InjectPayload):
    CALLFIXUP_TYPE: int = 1
    CALLMECHANISM_TYPE: int = 3
    CALLOTHERFIXUP_TYPE: int = 2
    EXECUTABLEPCODE_TYPE: int = 4



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    def getName(self) -> unicode: ...

    def getOutput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    def getParamShift(self) -> int: ...

    def getPcode(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.lang.InjectContext) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getSource(self) -> unicode: ...

    def getType(self) -> int: ...

    def hashCode(self) -> int: ...

    def inject(self, __a0: ghidra.program.model.lang.InjectContext, __a1: ghidra.app.plugin.processors.sleigh.PcodeEmit) -> None: ...

    def isFallThru(self) -> bool: ...

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
    def fallThru(self) -> bool: ...

    @property
    def input(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def output(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    @property
    def paramShift(self) -> int: ...

    @property
    def source(self) -> unicode: ...

    @property
    def type(self) -> int: ...
