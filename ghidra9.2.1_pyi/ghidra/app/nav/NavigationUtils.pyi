from typing import List
import ghidra.app.nav
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class NavigationUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getActiveNavigatable() -> ghidra.app.nav.Navigatable: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getExternalLinkageAddresses(program: ghidra.program.model.listing.Program, externalAddr: ghidra.program.model.address.Address) -> List[ghidra.program.model.address.Address]:
        """
        Locate all possible linkage addresses which correspond to the specified external address.
         This will correspond to either a generic reference type (DATA or EXTERNAL_REF) on a pointer
         or a thunk to the external location.  Both pointers and thunk contructs are utilized to
         perform dynamic linking between programs and external libraries they reference.  These
         linkage locations facilitate the function calls into any dynamically
         linked external program (i.e., library).
        @param program
        @param externalAddr external location address
        @return array of possible linkage addresses found
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setSelection(tool: ghidra.framework.plugintool.PluginTool, navigatable: ghidra.app.nav.Navigatable, selection: ghidra.program.util.ProgramSelection) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
