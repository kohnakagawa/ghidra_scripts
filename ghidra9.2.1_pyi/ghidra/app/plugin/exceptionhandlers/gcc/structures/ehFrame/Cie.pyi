import ghidra.app.plugin.exceptionhandlers.gcc
import ghidra.program.model.address
import java.lang


class Cie(ghidra.app.plugin.exceptionhandlers.gcc.GccAnalysisClass):




    @overload
    def __init__(self, __a0: ghidra.util.task.TaskMonitor, __a1: ghidra.program.model.listing.Program): ...

    @overload
    def __init__(self, __a0: ghidra.util.task.TaskMonitor, __a1: ghidra.program.model.listing.Program, __a2: bool): ...



    def create(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getAugmentationString(self) -> unicode: ...

    def getCieId(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeAlignment(self) -> int: ...

    def getDataAlignment(self) -> int: ...

    def getFDEDecoder(self) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDecoder: ...

    def getFDEEncoding(self) -> int: ...

    def getLSDADecoder(self) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDecoder: ...

    def getLSDAEncoding(self) -> int: ...

    def getNextAddress(self) -> ghidra.program.model.address.Address: ...

    def getReturnAddressRegisterColumn(self) -> int: ...

    def getSegmentSize(self) -> int: ...

    def hashCode(self) -> int: ...

    def isEndOfFrame(self) -> bool: ...

    def isInDebugFrame(self) -> bool: ...

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
    def FDEDecoder(self) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDecoder: ...

    @property
    def FDEEncoding(self) -> int: ...

    @property
    def LSDADecoder(self) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDecoder: ...

    @property
    def LSDAEncoding(self) -> int: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def augmentationString(self) -> unicode: ...

    @property
    def cieId(self) -> int: ...

    @property
    def codeAlignment(self) -> int: ...

    @property
    def dataAlignment(self) -> int: ...

    @property
    def endOfFrame(self) -> bool: ...

    @property
    def inDebugFrame(self) -> bool: ...

    @property
    def nextAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def returnAddressRegisterColumn(self) -> int: ...

    @property
    def segmentSize(self) -> int: ...