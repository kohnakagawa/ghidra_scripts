import docking
import docking.action
import docking.widgets.tree.support
import ghidra.framework.main
import ghidra.framework.model
import ghidra.util
import ghidra.util.task
import java.awt
import java.awt.event
import java.lang
import java.util
import javax.swing


class OpenVersionedFileDialog(ghidra.framework.main.DataTreeDialog):
    """
    Dialog to open a file that is versioned and allow a version to be
     opened.
    """





    def __init__(self, tool: ghidra.framework.plugintool.PluginTool, title: unicode, filter: ghidra.framework.model.DomainFileFilter):
        """
        Constructor
        @param tool tool where the file is being opened.
        @param title title to use
        @param filter filter used to control what is displayed in data tree.
        """
        ...



    def actionPerformed(self, e: java.awt.event.ActionEvent) -> None:
        """
        Action listener for the project combo box.
        @param e event generated when a selection is made in the combo box
        """
        ...

    def addAction(self, action: docking.action.DockingActionIf) -> None:
        """
        Add an action to this dialog.  Only actions with icons are added to the toolbar.
         Note, if you add an action to this dialog, do not also add the action to
         the tool, as this dialog will do that for you.
        @param action the action
        """
        ...

    def addOkActionListener(self, l: java.awt.event.ActionListener) -> None:
        """
        Add action listener that is called when the OK button is hit.
        @param l listener to add
        """
        ...

    def clearStatusText(self) -> None:
        """
        Clears the text from the dialog's status line.
        """
        ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findAndSelect(self, s: unicode) -> None: ...

    def getActionContext(self, event: java.awt.event.MouseEvent) -> docking.ActionContext: ...

    def getActions(self) -> java.util.Set: ...

    def getBackground(self) -> java.awt.Color:
        """
        Gets the background color of this component.
        @return The background color of this component.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getDefaultButton(self) -> javax.swing.JButton:
        """
        Returns the default button for the dialog.
        @return the button
        """
        ...

    def getDefaultSize(self) -> java.awt.Dimension: ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile:
        """
        Get the selected domain file.
        @return null if there was no domain file selected
        """
        ...

    def getDomainFolder(self) -> ghidra.framework.model.DomainFolder:
        """
        Get the selected folder.
        @return null if there was no domain folder selected
        """
        ...

    def getFocusComponent(self) -> java.awt.Component:
        """
        Returns the component that will receive focus when the dialog is shown
        @return the component
        """
        ...

    def getHelpLocatdion(self) -> ghidra.util.HelpLocation:
        """
        Returns the help location for this dialog
        @return the help location
        """
        ...

    def getIntialLocation(self) -> java.awt.Point:
        """
        Returns the initial location for the dialog or null if none was set
        @return the point
        """
        ...

    def getNameText(self) -> unicode:
        """
        Get the name from the name field.
        """
        ...

    def getPreferredSize(self) -> java.awt.Dimension:
        """
        Returns the preferred size of this component.
        @return the preferred size of this component.
        """
        ...

    def getRemberSize(self) -> bool:
        """
        Returns true if this dialog remembers its size from one invocation to the next.
        @return true if this dialog remembers its size from one invocation to the next.
        """
        ...

    def getRememberLocation(self) -> bool:
        """
        Returns true if this dialog remembers its location from one invocation to the next.
        @return true if this dialog remembers its location from one invocation to the next.
        """
        ...

    def getStatusText(self) -> unicode:
        """
        Returns the current status in the dialogs status line
        @return the status text
        """
        ...

    def getTitle(self) -> unicode:
        """
        Returns the title for this component
        @return the title
        """
        ...

    def getUseSharedLocation(self) -> bool:
        """
        Returns true if this dialog uses shared location and size information.
        @return true if this dialog uses shared location and size information.
        @see #setUseSharedLocation(boolean)
        """
        ...

    def getVersion(self) -> int:
        """
        Return the selected version number from the history panel.
        @return -1 if a version history was not selected
        """
        ...

    def getVersionedDomainObject(self, consumer: object, readOnly: bool) -> ghidra.framework.model.DomainObject:
        """
        Get the domain object for the selected version.
        @param consumer consumer
        @param readOnly true if the domain object should be opened read only,
         versus immutable
        @return null if a versioned file was not selected
        """
        ...

    def hashCode(self) -> int: ...

    def hideTaskMonitorComponent(self) -> None:
        """
        Will hide the progress panel if it was showing.
        @see #showTaskMonitorComponent(String, boolean, boolean)
        """
        ...

    def isModal(self) -> bool:
        """
        Returns true if this component should be displayed in a modal dialog
        @return true if this component should be displayed in a modal dialog
        """
        ...

    def isResizeable(self) -> bool: ...

    def isRunningTask(self) -> bool:
        """
        Returns true if this dialog is running a task.
        @return true if this dialog is running a task.
        """
        ...

    def isShowing(self) -> bool: ...

    def isTransient(self) -> bool:
        """
        Returns true if this dialog is intended to be shown and hidden relatively quickly.  This
         is used to determine if this dialog should be allowed to parent other components.   The
         default is false.
        @return true if this dialog is transient
        """
        ...

    def isVisible(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeAction(self, action: docking.action.DockingActionIf) -> None: ...

    def selectDomainFile(self, file: ghidra.framework.model.DomainFile) -> None:
        """
        Select the node that corresponds to the given domain file.
        """
        ...

    def selectRootDataFolder(self) -> None:
        """
        Select the root folder in the tree.
        """
        ...

    def setBackground(self, color: java.awt.Color) -> None:
        """
        Sets the background on this component.
        @param color The color to set.
        """
        ...

    def setCursor(self, cursor: java.awt.Cursor) -> None:
        """
        Sets the cursor on the root panel for the dialog component.
        @param cursor the cursor to use.
        """
        ...

    def setDefaultButton(self, button: javax.swing.JButton) -> None:
        """
        Sets the button to make "Default" when the dialog is shown.  If no default button is
         desired, then pass <code>null</code> as the <code>button</code> value.
        @param button the button to make default enabled.
        """
        ...

    def setDefaultSize(self, width: int, height: int) -> None: ...

    def setFocusComponent(self, focusComponent: java.awt.Component) -> None:
        """
        Sets the component that should be given focus when the dialog is activated.
         <p>
         Implementation Note:  If the given component is a JButton, then that component will be
         made the default button.
        @param focusComponent the component that should receive default focus.
        @see #setFocusComponent(Component)
        """
        ...

    def setHelpLocation(self, helpLocation: ghidra.util.HelpLocation) -> None:
        """
        Set the help Location for this dialog.
        @param helpLocation the helpLocation for this dialog.
        """
        ...

    def setInitialLocation(self, x: int, y: int) -> None:
        """
        Sets the initial location for the dialog
        @param x the x coordinate
        @param y the y coordinate
        """
        ...

    @overload
    def setMinimumSize(self, minSize: java.awt.Dimension) -> None:
        """
        Sets the minimum size of the dialog
        @param minSize the min size of the dialog
        """
        ...

    @overload
    def setMinimumSize(self, width: int, height: int) -> None: ...

    def setNameText(self, name: unicode) -> None: ...

    def setPreferredSize(self, width: int, height: int) -> None:
        """
        Sets the preferred size of the dialog.  Note that if you set the preferred size, the
         dialog will ignore any natural preferred size of your components.
        @param width the preferred width
        @param height the preferred height;
        """
        ...

    def setRememberLocation(self, rememberLocation: bool) -> None:
        """
        Sets this dialog to remember its location from one invocation to the next. The default is to
         remember location.
        @param rememberLocation true to remember, false otherwise.
        """
        ...

    def setRememberSize(self, rememberSize: bool) -> None:
        """
        Sets this dialog to remember its size from one invocation to the next. The default is to
         remember size.
        @param rememberSize true to remember, false otherwise.
        """
        ...

    def setResizable(self, resizeable: bool) -> None:
        """
        Sets the resizable property for the corresponding dialog.
        @param resizeable if false the user will not be able to resize the dialog.
        """
        ...

    def setSearchText(self, string: unicode) -> None: ...

    def setSelectedFolder(self, folder: ghidra.framework.model.DomainFolder) -> None: ...

    def setStatusJustification(self, justification: int) -> None:
        """
        Sets the horizontal position of the status label.
        @param justification One of the following constants
                   defined in <code>SwingConstants</code>:
                   <code>LEFT</code>,
                   <code>CENTER</code> (the default for image-only labels),
                   <code>RIGHT</code>,
        """
        ...

    @overload
    def setStatusText(self, text: unicode) -> None:
        """
        Sets the text in the dialog's status line using the default color
        @param text the text to display in the status line
        """
        ...

    @overload
    def setStatusText(self, message: unicode, type: ghidra.util.MessageType) -> None:
        """
        Sets the text in the dialog's status line using the specified message type to control
         the color.
        @param message the message
        @param type the message type
        """
        ...

    @overload
    def setStatusText(self, message: unicode, type: ghidra.util.MessageType, alert: bool) -> None: ...

    def setTitle(self, title: unicode) -> None:
        """
        Sets the title to be displayed in the dialogs title bar
        @param title the title
        """
        ...

    def setTransient(self, isTransient: bool) -> None:
        """
        Sets this dialog to be transient (see {@link #isTransient()}
        @param isTransient true for transient; false is the default
        """
        ...

    def setTreeSelectionMode(self, mode: int) -> None: ...

    def setUseSharedLocation(self, useSharedLocation: bool) -> None:
        """
        Specifies whether or not this dialog component should use the same remembered location (and
         size) no matter which window this dialog is launched from.  The default is not to use
         shared location and size, which means that there is a remembered location and size for this
         dialog for each window that has launched it (i.e. the window is the parent of the dialog).
        @param useSharedLocation true to share locations
        """
        ...

    def showComponent(self) -> None: ...

    def showTaskMonitorComponent(self, localTitle: unicode, hasProgress: bool, canCancel: bool) -> ghidra.util.task.TaskMonitor:
        """
        Shows the progress bar for this dialog.
        @param localTitle the name of the task
        @param hasProgress true if the progress bar should show progress; false to be indeterminate
        @param canCancel true if the task can be cancelled
        @return the {@link TaskMonitor} used by to communicate progress
        @see #hideTaskMonitorComponent()
        """
        ...

    def taskCancelled(self, task: ghidra.util.task.Task) -> None:
        """
        Notification that the task was canceled; the progress panel is
         removed.
        @param task task that was canceled
        """
        ...

    def taskCompleted(self, task: ghidra.util.task.Task) -> None:
        """
        Notification that the given task completed so that the progress
         panel can be removed.
        @param task task that completed
        """
        ...

    def toFront(self) -> None:
        """
        Moves the dialog associated with this provider to the front.
        """
        ...

    def toString(self) -> unicode: ...

    def valueChanged(self, e: docking.widgets.tree.support.GTreeSelectionEvent) -> None:
        """
        TreeSelectionListener method that is called whenever the value of the
         selection changes.
        @param e the event that characterizes the change.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def waitForCurrentTask(self) -> None:
        """
        Blocks the calling thread until the current task has completed; used
         by JUnit tests.
        """
        ...

    def wasCancelled(self) -> bool: ...

    @property
    def version(self) -> int: ...
