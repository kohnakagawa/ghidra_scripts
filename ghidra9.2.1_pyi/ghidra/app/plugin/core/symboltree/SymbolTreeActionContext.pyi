from typing import List
import docking
import ghidra.app.context
import ghidra.app.plugin.core.symboltree
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.awt
import java.awt.event
import java.lang
import javax.swing.tree


class SymbolTreeActionContext(ghidra.app.context.ProgramSymbolActionContext):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponentProvider(self) -> docking.ComponentProvider: ...

    def getContextObject(self) -> object: ...

    def getFirstSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getGlobalContext(self) -> docking.ActionContext: ...

    def getMouseEvent(self) -> java.awt.event.MouseEvent: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getSelectedPath(self) -> javax.swing.tree.TreePath: ...

    def getSelectedSymbolTreePaths(self) -> List[javax.swing.tree.TreePath]: ...

    def getSourceComponent(self) -> java.awt.Component: ...

    def getSourceObject(self) -> object: ...

    def getSymbolCount(self) -> int: ...

    def getSymbolTree(self) -> ghidra.app.plugin.core.symboltree.SymbolGTree: ...

    def getSymbolTreeProvider(self) -> ghidra.app.plugin.core.symboltree.SymbolTreeProvider: ...

    def getSymbols(self) -> java.lang.Iterable: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextObject(self, __a0: object) -> docking.ActionContext: ...

    def setMouseEvent(self, __a0: java.awt.event.MouseEvent) -> docking.ActionContext: ...

    def setSourceObject(self, __a0: object) -> docking.ActionContext: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def selectedPath(self) -> javax.swing.tree.TreePath: ...

    @property
    def selectedSymbolTreePaths(self) -> List[javax.swing.tree.TreePath]: ...

    @property
    def symbolTree(self) -> ghidra.app.plugin.core.symboltree.SymbolGTree: ...

    @property
    def symbolTreeProvider(self) -> ghidra.app.plugin.core.symboltree.SymbolTreeProvider: ...
