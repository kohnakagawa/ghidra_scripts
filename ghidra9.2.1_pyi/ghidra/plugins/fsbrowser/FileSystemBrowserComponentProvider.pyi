import docking
import docking.action
import ghidra.framework.plugintool
import ghidra.util
import java.awt.event
import java.lang
import javax.swing


class FileSystemBrowserComponentProvider(ghidra.framework.plugintool.ComponentProviderAdapter):
    """
    Plugin component provider for the FileSystemBrowserPlugin.

     An instance of this class is created for each file system browser window (w/tree).

     Visible to just this package.
    """





    @overload
    def __init__(self, tool: ghidra.framework.plugintool.PluginTool, name: unicode, owner: unicode):
        """
        Creates a new component provider with a default location of
         {@link docking.WindowPosition#WINDOW WindowPosition.WINDOW}.
        @param tool the plugin tool.
        @param name The providers name.  This is used to group similar providers into a tab within
                the same window.
        @param owner The owner of this provider, usually a plugin name.
        """
        ...

    @overload
    def __init__(self, tool: ghidra.framework.plugintool.PluginTool, name: unicode, owner: unicode, contextType: java.lang.Class):
        """
        Creates a new component provider with a default location of
         {@link docking.WindowPosition#WINDOW WindowPosition.WINDOW}.
        @param tool the plugin tool.
        @param name The providers name.  This is used to group similar providers into a tab within
                the same window.
        @param owner The owner of this provider, usually a plugin name
        @param contextType the type of context supported by this provider; may be null
        """
        ...



    def addLocalAction(self, action: docking.action.DockingActionIf) -> None:
        """
        Adds the given action to the system and associates it with this provider.
        @param action The action to add.
        """
        ...

    def addToTool(self) -> None:
        """
        Adds this provider to the tool in a new window that is not initially visible.  The provider
         will then show up in the "Windows" menu of the tool
        """
        ...

    def closeComponent(self) -> None:
        """
        This is the callback that will happen when the user presses the 'X' button of a provider.
         Transient providers will be removed from the tool completely.   Non-transient providers
         will merely be hidden.

         <P>Subclasses may override this method to prevent a provider from being closed; for
         example, if an editor has unsaved changes, then this method could prevent the close from
         happening.
        """
        ...

    def componentActivated(self) -> None:
        """
        Notifies the component provider that it is now the active provider
        """
        ...

    def componentDeactived(self) -> None:
        """
        Notifies the component provider that it is no longer the active provider
        """
        ...

    def componentHidden(self) -> None: ...

    def componentShown(self) -> None:
        """
        Notifies the provider that the component is being shown.
        """
        ...

    def contextChanged(self) -> None:
        """
        Kicks the tool to let it know the context for this provider has changed.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getActionContext(self, event: java.awt.event.MouseEvent) -> docking.ActionContext: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getContextType(self) -> java.lang.Class:
        """
        A signal used when installing actions.  Some actions are only added to a given window
         if there is a provider in that window that can work with that action.  Providers can return
         a context class from this method to control whether dependent actions get added.  Most
         providers return null for this method, which means they will not have any dependent
         actions added to windows other than the primary application window.
        @return a class representing the desired context type or null;
        """
        ...

    def getDefaultWindowPosition(self) -> docking.WindowPosition: ...

    def getHelpInfo(self) -> unicode: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation:
        """
        Returns the general HelpLocation for this provider.  Should return null only if no
         help documentation exists.
        @return the help location
        """
        ...

    def getHelpObject(self) -> object: ...

    def getIcon(self) -> javax.swing.Icon:
        """
        Returns the Icon associated with the component view
        @return the Icon associated with the component view
        """
        ...

    def getInstanceID(self) -> long:
        """
        A unique ID for this provider
        @return unique ID for this provider
        """
        ...

    def getIntraGroupPosition(self) -> docking.WindowPosition:
        """
        The position of this provider when being placed with other members of the same group.  As
         an example, assume this provider is being shown for the first time while there is another
         member of its {@link #getWindowGroup() window group} already visible.  Further, assume
         that this method will return {@link WindowPosition#STACK}.  This provider will then be
         stacked upon the already showing provider.
         <p>
         To determine where this provider should be initially shown,
         see {@link #getDefaultWindowPosition()}.
        @return The position of this provider when being placed with other members of the same group.
        """
        ...

    @staticmethod
    def getMappedName(oldOwner: unicode, oldName: unicode) -> unicode:
        """
        Returns any registered new provider owner for the oldName/oldOwner pair.
        @param oldOwner the old owner name
        @param oldName the old provider name
        @return the new provider owner for that oldOwner/oldName
        """
        ...

    @staticmethod
    def getMappedOwner(oldOwner: unicode, oldName: unicode) -> unicode:
        """
        Returns any registered new provider name for the oldName/oldOwner pair.
        @param oldOwner the old owner name
        @param oldName the old provider name
        @return the new provider name for that oldOwner/oldName
        """
        ...

    def getName(self) -> unicode: ...

    def getOwner(self) -> unicode:
        """
        Returns the owner of this provider (usually a plugin)
        @return the owner of this provider
        """
        ...

    def getSubTitle(self) -> unicode:
        """
        Returns the provider's current sub-title (Sub-titles don't show up
         in the window menu).
        @return the provider's current sub-title.
        """
        ...

    def getTabText(self) -> unicode:
        """
        Returns the optionally set text to display in the tab for a component provider.   The
         text returned from {@link #getTitle()} will be used by default.
        @return the optionally set text to display in the tab for a component provider.
        @see #setTabText(String)
        """
        ...

    def getTitle(self) -> unicode:
        """
        Returns the provider's current title.
        @return the provider's current title.
        """
        ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def getWindowGroup(self) -> unicode:
        """
        Returns an optional group designator that, if non-null, the docking window manager uses to
         determine the initial location of the new component relative to any existing instances
         of this component Provider.
         <p>
         The docking window manager will use {@link #getIntraGroupPosition() Intra-group Position}
         to decide where to place this provider inside of the already open instances of the
         same group.  The default position is 'stack', which results in the new instance being
         stacked with other instances of this provider that have the same group unless that instance is
         the active provider or is currently stacked with the active provider. (This is to prevent
         new windows from covering the active window).
        @return the window group
        """
        ...

    def getWindowSubMenuName(self) -> unicode:
        """
        Returns the name of a cascading sub-menu name to use when when showing this provider in the
         "Window" menu. If the group name is null, the item will appear in the top-level menu.
        @return the menu group for this provider or null if this provider should appear in the
         top-level menu.
        """
        ...

    def hashCode(self) -> int: ...

    def isActive(self) -> bool:
        """
        Convenience method to indicate if this provider is the active provider (has focus)
        @return true if this provider is active.
        """
        ...

    def isFocusedProvider(self) -> bool:
        """
        Returns true if this provider has focus
        @return true if this provider has focus
        """
        ...

    def isInTool(self) -> bool: ...

    def isSnapshot(self) -> bool:
        """
        A special marker that indicates this provider is a snapshot of a primary provider,
         somewhat like a picture of the primary provider.
        @return true if a snapshot
        """
        ...

    def isTransient(self) -> bool:
        """
        Returns true if this component goes away during a user session (most providers remain in
         the tool all session long, visible or not)
        @return true if transient
        """
        ...

    def isVisible(self) -> bool:
        """
        Convenience method to indicate if this provider is showing.
        @return true if this provider is showing.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def registerProviderNameOwnerChange(oldName: unicode, oldOwner: unicode, newName: unicode, newOwner: unicode) -> None:
        """
        Register a name and/or owner change to a provider so that old tools can restore those
         provider windows to their old position and size. Note you must supply all four
         arguments. If the name or owner did not change, use the name or owner that did not change
         for both the old and new values.

         <p>Note: when you make use of this method, please signal when it is safe to remove
         its usage.
        @param oldName the old name of the provider.
        @param oldOwner the old owner of the provider.
        @param newName the new name of the provider. If the name did not change, use the old name here.
        @param newOwner the new owner of the provider. If the owner did not change, use the old owner here.
        """
        ...

    def removeFromTool(self) -> None:
        """
        Removes this provider from the tool.
        """
        ...

    def requestFocus(self) -> None: ...

    def setHelpLocation(self, helpLocation: ghidra.util.HelpLocation) -> None: ...

    def setIntraGroupPosition(self, position: docking.WindowPosition) -> None:
        """
        See {@link #getIntraGroupPosition()}.
        @param position the new position
        """
        ...

    def setSubTitle(self, subTitle: unicode) -> None:
        """
        Sets the provider's sub-title (Sub-titles don't show up
         in the window menu).
        @param subTitle the sub-title string to use.
        """
        ...

    def setTabText(self, tabText: unicode) -> None:
        """
        Sets the text to be displayed on tabs when provider is stacked with other providers.
        @param tabText the tab text.
        """
        ...

    def setTitle(self, title: unicode) -> None:
        """
        Sets the provider's title.
        @param title the title string to use.
        """
        ...

    def setVisible(self, visible: bool) -> None:
        """
        Convenience method to show or hide this provider.
        @param visible True shows the provider; false hides the provider
        """
        ...

    def toFront(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
