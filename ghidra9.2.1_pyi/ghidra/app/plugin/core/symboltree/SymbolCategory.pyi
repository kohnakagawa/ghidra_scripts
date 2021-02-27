import ghidra.program.model.symbol
import java.lang


class SymbolCategory(object):
    CLASS_CATEGORY: ghidra.app.plugin.core.symboltree.SymbolCategory = Classes
    EXPORTS_CATEGORY: ghidra.app.plugin.core.symboltree.SymbolCategory = Exports
    FUNCTION_CATEGORY: ghidra.app.plugin.core.symboltree.SymbolCategory = Functions
    IMPORTS_CATEGORY: ghidra.app.plugin.core.symboltree.SymbolCategory = Imports
    LABEL_CATEGORY: ghidra.app.plugin.core.symboltree.SymbolCategory = Labels
    NAMESPACE_CATEGORY: ghidra.app.plugin.core.symboltree.SymbolCategory = Namespaces
    ROOT_CATEGORY: ghidra.app.plugin.core.symboltree.SymbolCategory = Global







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getSymbolType(self) -> ghidra.program.model.symbol.SymbolType: ...

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
    def name(self) -> unicode: ...

    @property
    def symbolType(self) -> ghidra.program.model.symbol.SymbolType: ...
