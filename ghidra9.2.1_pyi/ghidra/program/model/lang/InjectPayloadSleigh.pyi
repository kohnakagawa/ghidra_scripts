from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.template
import ghidra.program.model.lang
import ghidra.program.model.lang.InjectPayload
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class InjectPayloadSleigh(object, ghidra.program.model.lang.InjectPayload):
    """
    InjectPayloadSleigh defines an InjectPayload of p-code which is defined via
     a String passed to the sleigh compiler
    """

    CALLFIXUP_TYPE: int = 1
    CALLMECHANISM_TYPE: int = 3
    CALLOTHERFIXUP_TYPE: int = 2
    EXECUTABLEPCODE_TYPE: int = 4



    def __init__(self, nm: unicode, tp: int, sourceName: unicode):
        """
        Provide basic form,  restoreXml fills in the rest
        @param nm must provide formal name
        @param tp must provide type
        @param sourceName
        """
        ...



    def clone(self) -> ghidra.program.model.lang.InjectPayloadSleigh: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    def getName(self) -> unicode: ...

    def getOutput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    def getParamShift(self) -> int: ...

    def getPcode(self, program: ghidra.program.model.listing.Program, con: ghidra.program.model.lang.InjectContext) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getSource(self) -> unicode: ...

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
    def template(self) -> None: ...  # No getter available.

    @template.setter
    def template(self, value: ghidra.app.plugin.processors.sleigh.template.ConstructTpl) -> None: ...

    @property
    def type(self) -> int: ...
