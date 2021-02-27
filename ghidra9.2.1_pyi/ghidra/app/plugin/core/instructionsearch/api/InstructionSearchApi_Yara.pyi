from typing import List
import ghidra.app.plugin.core.instructionsearch
import ghidra.app.plugin.core.instructionsearch.model
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class InstructionSearchApi_Yara(ghidra.app.plugin.core.instructionsearch.InstructionSearchApi):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBinarySearchString(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange) -> unicode: ...

    @overload
    def getBinarySearchString(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange, __a2: ghidra.app.plugin.core.instructionsearch.model.MaskSettings) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getHexSearchString(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange) -> unicode: ...

    @overload
    def getHexSearchString(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange, __a2: ghidra.app.plugin.core.instructionsearch.model.MaskSettings) -> unicode: ...

    @overload
    def getYaraString(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange) -> unicode: ...

    @overload
    def getYaraString(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange, __a2: ghidra.app.plugin.core.instructionsearch.model.MaskSettings) -> unicode: ...

    def hashCode(self) -> int: ...

    @overload
    def loadInstructions(self, __a0: unicode, __a1: ghidra.framework.plugintool.PluginTool) -> None: ...

    @overload
    def loadInstructions(self, __a0: ghidra.program.model.address.AddressSet, __a1: ghidra.framework.plugintool.PluginTool) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def search(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange) -> List[object]: ...

    @overload
    def search(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressRange, __a2: ghidra.app.plugin.core.instructionsearch.model.MaskSettings) -> List[object]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
