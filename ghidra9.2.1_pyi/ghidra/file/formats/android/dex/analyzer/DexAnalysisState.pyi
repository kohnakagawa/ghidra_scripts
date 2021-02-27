import ghidra.app.plugin.core.analysis
import ghidra.file.formats.android.dex.analyzer
import ghidra.file.formats.android.dex.format
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class DexAnalysisState(object, ghidra.app.plugin.core.analysis.AnalysisState):




    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.file.formats.android.dex.format.DexHeader): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEncodedMethod(self, __a0: ghidra.program.model.address.Address) -> ghidra.file.formats.android.dex.format.EncodedMethod: ...

    def getHeader(self) -> ghidra.file.formats.android.dex.format.DexHeader: ...

    @staticmethod
    def getState(__a0: ghidra.program.model.listing.Program) -> ghidra.file.formats.android.dex.analyzer.DexAnalysisState: ...

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

    @property
    def header(self) -> ghidra.file.formats.android.dex.format.DexHeader: ...
