from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.lang.ParamList
import ghidra.program.model.listing
import ghidra.xml
import java.lang
import java.util


class ParamList(object):
    """
    A group of ParamEntry that form a complete set for passing parameters (in one direction)
    """






    class WithSlotRec(object):




        def __init__(self): ...



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







    def assignMap(self, __a0: ghidra.program.model.listing.Program, __a1: List[ghidra.program.model.data.DataType], __a2: bool, __a3: java.util.ArrayList, __a4: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPotentialRegisterStorage(self, prog: ghidra.program.model.listing.Program) -> List[ghidra.program.model.listing.VariableStorage]:
        """
        Get a list of all parameter storage locations consisting of a single register
        @return
        """
        ...

    def getStackParameterAlignment(self) -> int:
        """
        Return the amount of alignment used for parameters passed on the stack, or -1 if there are no stack params
        @return the alignment
        """
        ...

    def getStackParameterOffset(self) -> long:
        """
        Find the boundary offset that separates parameters on the stack from other local variables
         This is usually the address of the first stack parameter, but if the stack grows positive, this is
         the first address AFTER the parameters on the stack
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def isThisBeforeRetPointer(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def possibleParamWithSlot(self, loc: ghidra.program.model.address.Address, size: int, res: ghidra.program.model.lang.ParamList.WithSlotRec) -> bool:
        """
        Determine if a particular address range is a possible parameter, and if so what slot(s) it occupies
        @param loc is the starting address of the range
        @param size is the size of the range in bytes
        @param res holds the resulting slot and slotsize
        @return true if the range is a possible parameter
        """
        ...

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
