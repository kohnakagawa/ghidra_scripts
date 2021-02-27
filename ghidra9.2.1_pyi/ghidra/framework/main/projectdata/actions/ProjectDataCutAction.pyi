import docking
import docking.action
import ghidra.framework.main.projectdata.actions
import ghidra.util
import java.beans
import java.lang
import java.util
import java.util.function
import javax.swing


class ProjectDataCutAction(ghidra.framework.main.projectdata.actions.ProjectDataCopyCutBaseAction):




    def __init__(self, owner: unicode, group: unicode): ...



    def actionPerformed(self, context: docking.ActionContext) -> None: ...

    def addPropertyChangeListener(self, listener: java.beans.PropertyChangeListener) -> None: ...

    def createButton(self) -> javax.swing.JButton: ...

    def createMenuItem(self, isPopup: bool) -> javax.swing.JMenuItem: ...

    def dispose(self) -> None:
        """
        Cleans up any resources used by the action.
        """
        ...

    def enabledWhen(self, predicate: java.util.function.Predicate) -> None:
        """
        Sets a predicate for dynamically determining the action's enabled state.  If this
         predicate is not set, the action's enable state must be controlled directly using the
         {@link DockingAction#setEnabled(boolean)} method. See
         {@link DockingActionIf#isEnabledForContext(ActionContext)}
        @param predicate the predicate that will be used to dynamically determine an action's
         enabled state.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def firePropertyChanged(self, propertyName: unicode, oldValue: object, newValue: object) -> None: ...

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

    def isEnabledForContext(self, actionContext: docking.ActionContext) -> bool: ...

    def isValidContext(self, context: docking.ActionContext) -> bool: ...

    def markHelpUnnecessary(self) -> None:
        """
        Signals the the help system that this action does not need a help entry.   Some actions
         are so obvious that they do not require help, such as an action that renames a file.
         <p>
         The method should be sparsely used, as most actions should provide help.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def popupWhen(self, predicate: java.util.function.Predicate) -> None:
        """
        Sets a predicate for dynamically determining if this action should be included in
         an impending pop-up menu.  If this predicate is not set, the action's will be included
         in an impending pop-up, if it is enabled. See
         {@link DockingActionIf#isAddToPopup(ActionContext)}
        @param predicate the predicate that will be used to dynamically determine an action's
         enabled state.
        """
        ...

    def removePropertyChangeListener(self, listener: java.beans.PropertyChangeListener) -> None: ...

    def setDescription(self, newDescription: unicode) -> None:
        """
        Sets the description to be used in the tooltip.
        @param newDescription the description to be set.
        """
        ...

    def setEnabled(self, newValue: bool) -> None: ...

    def setHelpLocation(self, location: ghidra.util.HelpLocation) -> None:
        """
        Set a specific Help location for this action.
         This will replace the default help location
        @param location the help location for the action.
        """
        ...

    def setKeyBindingData(self, newKeyBindingData: docking.action.KeyBindingData) -> None: ...

    def setMenuBarData(self, newMenuData: docking.action.MenuData) -> None:
        """
        Sets the {@link MenuData} to be used to put this action on the tool's menu bar
        @param newMenuData the MenuData to be used to put this action on the tool's menu bar
        """
        ...

    def setPopupMenuData(self, newMenuData: docking.action.MenuData) -> None:
        """
        Sets the {@link MenuData} to be used to put this action in the tool's popup menu
        @param newMenuData the MenuData to be used to put this action on the tool's popup menu
        """
        ...

    def setSupportsDefaultToolContext(self, newValue: bool) -> None: ...

    def setToolBarData(self, newToolBarData: docking.action.ToolBarData) -> None:
        """
        Sets the {@link ToolBarData} to be used to put this action on the tool's toolbar
        @param newToolBarData the ToolBarData to be used to put this action on the tool's toolbar
        """
        ...

    def setUnvalidatedKeyBindingData(self, newKeyBindingData: docking.action.KeyBindingData) -> None: ...

    def shouldAddToWindow(self, isMainWindow: bool, contextTypes: java.util.Set) -> bool:
        """
        Default behavior is to add to main window;
        """
        ...

    def supportsDefaultToolContext(self) -> bool: ...

    def toString(self) -> unicode: ...

    def validContextWhen(self, predicate: java.util.function.Predicate) -> None:
        """
        Sets a predicate for dynamically determining if this action is valid for the current
         {@link ActionContext}.  See {@link DockingActionIf#isValidContext(ActionContext)}
        @param predicate the predicate that will be used to dynamically determine an action's
         validity for a given {@link ActionContext}
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
