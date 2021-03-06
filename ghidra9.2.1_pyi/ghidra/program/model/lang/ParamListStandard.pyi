from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.lang.ParamList
import ghidra.program.model.listing
import ghidra.xml
import java.lang
import java.util


class ParamListStandard(object, ghidra.program.model.lang.ParamList):
    """
    Standard analysis for parameter lists
    """





    def __init__(self): ...



    def assignMap(self, __a0: ghidra.program.model.listing.Program, __a1: List[ghidra.program.model.data.DataType], __a2: bool, __a3: java.util.ArrayList, __a4: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPotentialRegisterStorage(self, prog: ghidra.program.model.listing.Program) -> List[ghidra.program.model.listing.VariableStorage]: ...

    def getStackParameterAlignment(self) -> int: ...

    def getStackParameterOffset(self) -> long: ...

    def hashCode(self) -> int: ...

    def isThisBeforeRetPointer(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def possibleParamWithSlot(self, loc: ghidra.program.model.address.Address, size: int, res: ghidra.program.model.lang.ParamList.WithSlotRec) -> bool: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, cspec: ghidra.program.model.lang.CompilerSpec, normalstack: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def stackParameterAlignment(self) -> int: ...

    @property
    def stackParameterOffset(self) -> long: ...

    @property
    def thisBeforeRetPointer(self) -> bool: ...
