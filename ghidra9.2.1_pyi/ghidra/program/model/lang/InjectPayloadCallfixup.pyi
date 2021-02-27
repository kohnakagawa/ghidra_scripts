from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.template
import ghidra.program.model.lang
import ghidra.program.model.lang.InjectPayload
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class InjectPayloadCallfixup(ghidra.program.model.lang.InjectPayloadSleigh):




    def __init__(self, sourceName: unicode): ...



    def clone(self) -> ghidra.program.model.lang.InjectPayloadSleigh: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    def getName(self) -> unicode: ...

    def getOutput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    def getParamShift(self) -> int: ...

    def getPcode(self, program: ghidra.program.model.listing.Program, con: ghidra.program.model.lang.InjectContext) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getSource(self) -> unicode: ...

    def getTargets(self) -> List[unicode]: ...

    def getType(self) -> int: ...

    def hashCode(self) -> int: ...

    def inject(self, context: ghidra.program.model.lang.InjectContext, emit: ghidra.app.plugin.processors.sleigh.PcodeEmit) -> None: ...

    def isFallThru(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def setTemplate(self, ctl: ghidra.app.plugin.processors.sleigh.template.ConstructTpl) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def targets(self) -> List[object]: ...
