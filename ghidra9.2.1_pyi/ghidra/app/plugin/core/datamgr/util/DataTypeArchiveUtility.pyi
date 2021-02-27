from typing import List
import generic.jar
import ghidra.program.model.listing
import java.lang


class DataTypeArchiveUtility(object):
    GHIDRA_ARCHIVES: java.util.Map = {u'mac_osx.gdt': /Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/Base/data/typeinfo/mac_10.9/mac_osx.gdt, u'generic_clib.gdt': /Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/Base/data/typeinfo/generic/generic_clib.gdt, u'windows_vs12_32.gdt': /Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/Base/data/typeinfo/win32/windows_vs12_32.gdt, u'windows_vs12_64.gdt': /Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/Base/data/typeinfo/win32/windows_vs12_64.gdt, u'generic_clib_64.gdt': /Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/Base/data/typeinfo/generic/generic_clib_64.gdt, u'EmuTesting.gdt': /Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/Base/data/pcodetest/EmuTesting.gdt}







    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findArchiveFile(__a0: unicode) -> generic.jar.ResourceFile: ...

    @staticmethod
    def getArchiveList(__a0: ghidra.program.model.listing.Program) -> List[object]: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getRemappedArchiveName(__a0: unicode) -> unicode: ...

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
