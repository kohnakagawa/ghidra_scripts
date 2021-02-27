import docking
import docking.action
import ghidra.app.plugin.core.functioncompare.actions
import ghidra.util
import java.beans
import java.lang
import java.util
import java.util.function
import javax.swing


class ApplyFunctionSignatureAction(ghidra.app.plugin.core.functioncompare.actions.AbstractApplyFunctionSignatureAction):
    """
    Action that applies the signature of the function in the currently active side of a listing
     code comparison panel to the function in the other side of the panel.
    """





    def __init__(self, owner: unicode):
        """
        Constructor for the action that applies a function signature from one side of a dual
         listing panel to the other.
        @param owner the owner of this action.
        """
        ...



    def actionPerformed(self, __a0: docking.ActionContext) -> None: ...

    def addPropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    def createButton(self) -> javax.swing.JButton: ...

    def createMenuItem(self, __a0: bool) -> javax.swing.JMenuItem: ...

    def dispose(self) -> None: ...

    def enabledWhen(self, __a0: java.util.function.Predicate) -> None: ...

    def equals(self, __a0: object) -> bool: ...

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

    def getToolBarData(self) -> docking.action.ToolBarData: ...

    def hashCode(self) -> int: ...

    def isAddToPopup(self, context: docking.ActionContext) -> bool: ...

    def isEnabled(self) -> bool: ...

    def isEnabledForContext(self, context: docking.ActionContext) -> bool: ...

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
