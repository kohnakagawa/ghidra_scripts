import ghidra.app.util.bin.format.coff
import java.lang


class CoffSymbolSpecial(object):
    DOT_BB: unicode = u'.bb'
    DOT_BF: unicode = u'.bf'
    DOT_BSS: unicode = u'.bss'
    DOT_DATA: unicode = u'.data'
    DOT_EB: unicode = u'.eb'
    DOT_EDATA: unicode = u'edata'
    DOT_EF: unicode = u'.ef'
    DOT_END: unicode = u'end'
    DOT_EOS: unicode = u'.eos'
    DOT_ETEXT: unicode = u'etext'
    DOT_FILE: unicode = u'.file'
    DOT_NFAKE: unicode = u'.nfake'
    DOT_TARGET: unicode = u'.target'
    DOT_TEXT: unicode = u'.text'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getStorageClass(self, specialSymbol: ghidra.app.util.bin.format.coff.CoffSymbol) -> int: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isSpecial(symbol: ghidra.app.util.bin.format.coff.CoffSymbol) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
