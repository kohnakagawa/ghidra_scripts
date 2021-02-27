from typing import List
import ghidra.app.plugin.processors.sleigh.template
import ghidra.program.model.address
import ghidra.xml
import java.lang


class ConstructTpl(object):
    """
    Placeholder for what resolves to a list of PcodeOps and
     a FixedHandle. It represents the semantic action of a constructor
     and its return value for a particular InstructionContext
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNumLabels(self) -> int: ...

    def getOpVec(self) -> List[ghidra.app.plugin.processors.sleigh.template.OpTpl]: ...

    def getResult(self) -> ghidra.app.plugin.processors.sleigh.template.HandleTpl: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, factory: ghidra.program.model.address.AddressFactory) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def numLabels(self) -> int: ...

    @property
    def opVec(self) -> List[ghidra.app.plugin.processors.sleigh.template.OpTpl]: ...

    @property
    def result(self) -> ghidra.app.plugin.processors.sleigh.template.HandleTpl: ...
