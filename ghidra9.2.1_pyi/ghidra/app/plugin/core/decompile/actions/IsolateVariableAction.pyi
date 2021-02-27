import docking
import docking.action
import ghidra.app.decompiler
import ghidra.app.plugin.core.decompile.actions
import ghidra.framework.plugintool
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.util
import java.beans
import java.lang
import java.util
import java.util.function
import javax.swing


class IsolateVariableAction(ghidra.app.plugin.core.decompile.actions.AbstractDecompilerAction):




    def __init__(self): ...



    def actionPerformed(self, __a0: docking.ActionContext) -> None: ...

    def addPropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    def chooseDataType(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.program.model.listing.Program, __a2: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType: ...

    def createButton(self) -> javax.swing.JButton: ...

    def createMenuItem(self, __a0: bool) -> javax.swing.JMenuItem: ...

    def dispose(self) -> None: ...

    def enabledWhen(self, __a0: java.util.function.Predicate) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findHighSymbolFromToken(__a0: ghidra.app.decompiler.ClangToken, __a1: ghidra.program.model.pcode.HighFunction) -> ghidra.program.model.pcode.HighSymbol: ...

    def firePropertyChanged(self, __a0: unicode, __a1: object, __a2: object) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultKeyBindingData(self) -> docking.action.KeyBindingData: ...

    def getDescription(self) -> unicode: ...

    def getFullName(self) -> unicode: ...

    def getHelpInfo(self) -> unicode: ...

    def getHelpObject(self) -> object: ...

    def getInceptionInformation(self) -> unicode: ...

    def getKeyBinding(self) -> javax.swing.KeyStroke: ...

    def getKeyBindingData(self) -> docking.action.KeyBindingData: ...

    def getKeyBindingType(self) -> docking.action.KeyBindingType: ...

    def getMenuBarData(self) -> docking.action.MenuData: ...

    def getName(self) -> unicode: ...

    def getOwner(self) -> unicode: ...

    def getOwnerDescription(self) -> unicode: ...

    def getPopupMenuData(self) -> docking.action.MenuData: ...

    @staticmethod
    def getStructDataType(__a0: ghidra.app.decompiler.ClangToken) -> ghidra.program.model.data.Structure: ...

    def getToolBarData(self) -> docking.action.ToolBarData: ...

    def hashCode(self) -> int: ...

    def isAddToPopup(self, __a0: docking.ActionContext) -> bool: ...

    def isEnabled(self) -> bool: ...

    def isEnabledForContext(self, __a0: docking.ActionContext) -> bool: ...

    def isValidContext(self, __a0: docking.ActionContext) -> bool: ...

    def markHelpUnnecessary(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def popupWhen(self, __a0: java.util.function.Predicate) -> None: ...

    def removePropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    def setDescription(self, __a0: unicode) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    def setHelpLocation(self, __a0: ghidra.util.HelpLocation) -> None: ...

    def setKeyBindingData(self, __a0: docking.action.KeyBindingData) -> None: ...

    def setMenuBarData(self, __a0: docking.action.MenuData) -> None: ...

    def setPopupMenuData(self, __a0: docking.action.MenuData) -> None: ...

    def setSupportsDefaultToolContext(self, __a0: bool) -> None: ...

    def setToolBarData(self, __a0: docking.action.ToolBarData) -> None: ...

    def setUnvalidatedKeyBindingData(self, __a0: docking.action.KeyBindingData) -> None: ...

    def shouldAddToWindow(self, __a0: bool, __a1: java.util.Set) -> bool: ...

    def supportsDefaultToolContext(self) -> bool: ...

    def toString(self) -> unicode: ...

    def validContextWhen(self, __a0: java.util.function.Predicate) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
