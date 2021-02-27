from typing import List
import docking
import docking.action
import docking.widgets.fieldpanel
import docking.widgets.fieldpanel.internal
import ghidra.app.decompiler.component
import ghidra.app.util.viewer.util
import ghidra.program.model.address
import ghidra.program.model.listing
import java.awt
import java.awt.dnd
import java.awt.event
import java.awt.im
import java.awt.image
import java.beans
import java.io
import java.lang
import java.util
import javax.accessibility
import javax.swing
import javax.swing.border
import javax.swing.event
import javax.swing.plaf


class DecompilerCodeComparisonPanel(ghidra.app.util.viewer.util.CodeComparisonPanel):
    """
    Panel that displays two decompilers for comparison
    """





    def __init__(self, owner: unicode, tool: ghidra.framework.plugintool.PluginTool):
        """
        Creates a comparison panel with two decompilers
        @param owner the owner of this panel
        @param tool the tool displaying this panel
        """
        ...



    def action(self, __a0: java.awt.Event, __a1: object) -> bool: ...

    @overload
    def add(self, __a0: java.awt.Component) -> java.awt.Component: ...

    @overload
    def add(self, __a0: java.awt.PopupMenu) -> None: ...

    @overload
    def add(self, __a0: java.awt.Component, __a1: int) -> java.awt.Component: ...

    @overload
    def add(self, __a0: unicode, __a1: java.awt.Component) -> java.awt.Component: ...

    @overload
    def add(self, __a0: java.awt.Component, __a1: object) -> None: ...

    @overload
    def add(self, __a0: java.awt.Component, __a1: object, __a2: int) -> None: ...

    def addAncestorListener(self, __a0: javax.swing.event.AncestorListener) -> None: ...

    def addComponentListener(self, __a0: java.awt.event.ComponentListener) -> None: ...

    def addContainerListener(self, __a0: java.awt.event.ContainerListener) -> None: ...

    def addDualDecompileResultsListener(self, listener: ghidra.app.decompiler.component.DualDecompileResultsListener) -> bool:
        """
        Adds the indicated listener to be notified when the decompile results have completed.
        @param listener the listener
        @return true if the listener was added.
        """
        ...

    def addFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def addHierarchyBoundsListener(self, __a0: java.awt.event.HierarchyBoundsListener) -> None: ...

    def addHierarchyListener(self, __a0: java.awt.event.HierarchyListener) -> None: ...

    def addInputMethodListener(self, __a0: java.awt.event.InputMethodListener) -> None: ...

    def addKeyListener(self, __a0: java.awt.event.KeyListener) -> None: ...

    def addMouseListener(self, __a0: java.awt.event.MouseListener) -> None: ...

    def addMouseMotionListener(self, __a0: java.awt.event.MouseMotionListener) -> None: ...

    def addMouseWheelListener(self, __a0: java.awt.event.MouseWheelListener) -> None: ...

    def addNotify(self) -> None: ...

    @overload
    def addPropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    @overload
    def addPropertyChangeListener(self, __a0: unicode, __a1: java.beans.PropertyChangeListener) -> None: ...

    def addVetoableChangeListener(self, __a0: java.beans.VetoableChangeListener) -> None: ...

    def applyComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def areFocusTraversalKeysSet(self, __a0: int) -> bool: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> int: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> int: ...

    def computeVisibleRect(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def contains(self, __a0: java.awt.Point) -> bool: ...

    @overload
    def contains(self, __a0: int, __a1: int) -> bool: ...

    def countComponents(self) -> int: ...

    @overload
    def createImage(self, __a0: java.awt.image.ImageProducer) -> java.awt.Image: ...

    @overload
    def createImage(self, __a0: int, __a1: int) -> java.awt.Image: ...

    def createToolTip(self) -> javax.swing.JToolTip: ...

    @overload
    def createVolatileImage(self, __a0: int, __a1: int) -> java.awt.image.VolatileImage: ...

    @overload
    def createVolatileImage(self, __a0: int, __a1: int, __a2: java.awt.ImageCapabilities) -> java.awt.image.VolatileImage: ...

    def deliverEvent(self, __a0: java.awt.Event) -> None: ...

    def disable(self) -> None: ...

    def dispatchEvent(self, __a0: java.awt.AWTEvent) -> None: ...

    def dispose(self) -> None: ...

    def doLayout(self) -> None: ...

    @overload
    def enable(self) -> None: ...

    @overload
    def enable(self, __a0: bool) -> None: ...

    def enableInputMethods(self, __a0: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def findComponentAt(self, __a0: java.awt.Point) -> java.awt.Component: ...

    @overload
    def findComponentAt(self, __a0: int, __a1: int) -> java.awt.Component: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: long, __a2: long) -> None: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: float, __a2: float) -> None: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: float, __a2: float) -> None: ...

    @overload
    def firePropertyChange(self, __a0: unicode, __a1: bool, __a2: bool) -> None: ...

    def focusGained(self, e: java.awt.event.FocusEvent) -> None: ...

    def focusLost(self, e: java.awt.event.FocusEvent) -> None: ...

    def getAccessibleContext(self) -> javax.accessibility.AccessibleContext: ...

    def getActionContext(self, provider: docking.ComponentProvider, event: java.awt.event.MouseEvent) -> docking.ActionContext: ...

    def getActionForKeyStroke(self, __a0: javax.swing.KeyStroke) -> java.awt.event.ActionListener: ...

    def getActionMap(self) -> javax.swing.ActionMap: ...

    def getActions(self) -> List[docking.action.DockingAction]: ...

    def getAlignmentX(self) -> float: ...

    def getAlignmentY(self) -> float: ...

    def getAncestorListeners(self) -> List[javax.swing.event.AncestorListener]: ...

    def getAutoscrolls(self) -> bool: ...

    def getBackground(self) -> java.awt.Color: ...

    def getBaseline(self, __a0: int, __a1: int) -> int: ...

    def getBaselineResizeBehavior(self) -> java.awt.Component.BaselineResizeBehavior: ...

    def getBorder(self) -> javax.swing.border.Border: ...

    @overload
    def getBounds(self) -> java.awt.Rectangle: ...

    @overload
    def getBounds(self, __a0: java.awt.Rectangle) -> java.awt.Rectangle: ...

    def getClass(self) -> java.lang.Class: ...

    def getClientProperty(self, __a0: object) -> object: ...

    def getColorModel(self) -> java.awt.image.ColorModel: ...

    @overload
    def getComponent(self) -> javax.swing.JComponent: ...

    @overload
    def getComponent(self, __a0: int) -> java.awt.Component: ...

    @overload
    def getComponentAt(self, __a0: java.awt.Point) -> java.awt.Component: ...

    @overload
    def getComponentAt(self, __a0: int, __a1: int) -> java.awt.Component: ...

    def getComponentCount(self) -> int: ...

    def getComponentListeners(self) -> List[java.awt.event.ComponentListener]: ...

    def getComponentOrientation(self) -> java.awt.ComponentOrientation: ...

    def getComponentPopupMenu(self) -> javax.swing.JPopupMenu: ...

    def getComponentZOrder(self, __a0: java.awt.Component) -> int: ...

    def getComponents(self) -> List[java.awt.Component]: ...

    def getConditionForKeyStroke(self, __a0: javax.swing.KeyStroke) -> int: ...

    def getContainerListeners(self) -> List[java.awt.event.ContainerListener]: ...

    def getCursor(self) -> java.awt.Cursor: ...

    def getDebugGraphicsOptions(self) -> int: ...

    @staticmethod
    def getDefaultLocale() -> java.util.Locale: ...

    def getDropTarget(self) -> java.awt.dnd.DropTarget: ...

    def getFocusCycleRootAncestor(self) -> java.awt.Container: ...

    def getFocusListeners(self) -> List[java.awt.event.FocusListener]: ...

    def getFocusTraversalKeys(self, __a0: int) -> java.util.Set: ...

    def getFocusTraversalKeysEnabled(self) -> bool: ...

    def getFocusTraversalPolicy(self) -> java.awt.FocusTraversalPolicy: ...

    def getFocusedDecompilerPanel(self) -> ghidra.app.decompiler.component.CDisplayPanel:
        """
        Gets the display panel from the left or right side that has or last had focus.
        @return the last C display panel with focus
        """
        ...

    def getFont(self) -> java.awt.Font: ...

    def getFontMetrics(self, __a0: java.awt.Font) -> java.awt.FontMetrics: ...

    def getForeground(self) -> java.awt.Color: ...

    def getGraphics(self) -> java.awt.Graphics: ...

    def getGraphicsConfiguration(self) -> java.awt.GraphicsConfiguration: ...

    def getHeight(self) -> int: ...

    def getHierarchyBoundsListeners(self) -> List[java.awt.event.HierarchyBoundsListener]: ...

    def getHierarchyListeners(self) -> List[java.awt.event.HierarchyListener]: ...

    def getIgnoreRepaint(self) -> bool: ...

    def getInheritsPopupMenu(self) -> bool: ...

    def getInputContext(self) -> java.awt.im.InputContext: ...

    @overload
    def getInputMap(self) -> javax.swing.InputMap: ...

    @overload
    def getInputMap(self, __a0: int) -> javax.swing.InputMap: ...

    def getInputMethodListeners(self) -> List[java.awt.event.InputMethodListener]: ...

    def getInputMethodRequests(self) -> java.awt.im.InputMethodRequests: ...

    def getInputVerifier(self) -> javax.swing.InputVerifier: ...

    @overload
    def getInsets(self) -> java.awt.Insets: ...

    @overload
    def getInsets(self, __a0: java.awt.Insets) -> java.awt.Insets: ...

    def getKeyListeners(self) -> List[java.awt.event.KeyListener]: ...

    def getLayout(self) -> java.awt.LayoutManager: ...

    def getLeftAddresses(self) -> ghidra.program.model.address.AddressSetView: ...

    def getLeftData(self) -> ghidra.program.model.listing.Data:
        """
        Gets the data loaded in the left side of this panel.
        @return the data or null
        """
        ...

    def getLeftDecompilerPanel(self) -> ghidra.app.decompiler.component.DecompilerPanel:
        """
        Gets the left side's decompiler panel.
        @return the left decompiler panel
        """
        ...

    def getLeftFieldPanel(self) -> docking.widgets.fieldpanel.FieldPanel: ...

    def getLeftFunction(self) -> ghidra.program.model.listing.Function:
        """
        Gets the function loaded in the left side of this panel.
        @return the function or null
        """
        ...

    def getLeftPanel(self) -> ghidra.app.decompiler.component.CDisplayPanel:
        """
        Gets the left side's C display panel.
        @return the left C display panel
        """
        ...

    def getLeftProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the program being viewed in the left side of this panel.
        @return the program or null
        """
        ...

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getLocale(self) -> java.util.Locale: ...

    @overload
    def getLocation(self) -> java.awt.Point: ...

    @overload
    def getLocation(self, __a0: java.awt.Point) -> java.awt.Point: ...

    def getLocationOnScreen(self) -> java.awt.Point: ...

    def getMaximumSize(self) -> java.awt.Dimension: ...

    def getMinimumSize(self) -> java.awt.Dimension: ...

    def getMouseListeners(self) -> List[java.awt.event.MouseListener]: ...

    def getMouseMotionListeners(self) -> List[java.awt.event.MouseMotionListener]: ...

    @overload
    def getMousePosition(self) -> java.awt.Point: ...

    @overload
    def getMousePosition(self, __a0: bool) -> java.awt.Point: ...

    def getMouseWheelListeners(self) -> List[java.awt.event.MouseWheelListener]: ...

    def getName(self) -> unicode: ...

    def getNextFocusableComponent(self) -> java.awt.Component: ...

    def getPanelThisSupersedes(self) -> java.lang.Class: ...

    def getParent(self) -> java.awt.Container: ...

    def getPopupLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    def getPreferredSize(self) -> java.awt.Dimension: ...

    @overload
    def getPropertyChangeListeners(self) -> List[java.beans.PropertyChangeListener]: ...

    @overload
    def getPropertyChangeListeners(self, __a0: unicode) -> List[java.beans.PropertyChangeListener]: ...

    def getRegisteredKeyStrokes(self) -> List[javax.swing.KeyStroke]: ...

    def getRightAddresses(self) -> ghidra.program.model.address.AddressSetView: ...

    def getRightData(self) -> ghidra.program.model.listing.Data:
        """
        Gets the data loaded in the right side of this panel.
        @return the data or null
        """
        ...

    def getRightDecompilerPanel(self) -> ghidra.app.decompiler.component.DecompilerPanel:
        """
        Gets the right side's decompiler panel.
        @return the right decompiler panel
        """
        ...

    def getRightFieldPanel(self) -> docking.widgets.fieldpanel.FieldPanel: ...

    def getRightFunction(self) -> ghidra.program.model.listing.Function:
        """
        Gets the function loaded in the right side of this panel.
        @return the function or null
        """
        ...

    def getRightPanel(self) -> ghidra.app.decompiler.component.CDisplayPanel:
        """
        Gets the right side's C display panel.
        @return the right C display panel
        """
        ...

    def getRightProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the program being viewed in the right side of this panel.
        @return the program or null
        """
        ...

    def getRootPane(self) -> javax.swing.JRootPane: ...

    def getShowTitles(self) -> bool: ...

    @overload
    def getSize(self) -> java.awt.Dimension: ...

    @overload
    def getSize(self, __a0: java.awt.Dimension) -> java.awt.Dimension: ...

    def getTitle(self) -> unicode: ...

    def getToolTipLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    @overload
    def getToolTipText(self) -> unicode: ...

    @overload
    def getToolTipText(self, __a0: java.awt.event.MouseEvent) -> unicode: ...

    def getToolkit(self) -> java.awt.Toolkit: ...

    def getTopLevelAncestor(self) -> java.awt.Container: ...

    def getTransferHandler(self) -> javax.swing.TransferHandler: ...

    def getTreeLock(self) -> object: ...

    def getUI(self) -> javax.swing.plaf.ComponentUI: ...

    def getUIClassID(self) -> unicode: ...

    def getVerifyInputWhenFocusTarget(self) -> bool: ...

    def getVetoableChangeListeners(self) -> List[java.beans.VetoableChangeListener]: ...

    def getVisibleRect(self) -> java.awt.Rectangle: ...

    def getWidth(self) -> int: ...

    def getX(self) -> int: ...

    def getY(self) -> int: ...

    def gotFocus(self, __a0: java.awt.Event, __a1: object) -> bool: ...

    def grabFocus(self) -> None: ...

    def handleEvent(self, __a0: java.awt.Event) -> bool: ...

    def hasFocus(self) -> bool: ...

    def hashCode(self) -> int: ...

    def hide(self) -> None: ...

    def imageUpdate(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: int, __a4: int, __a5: int) -> bool: ...

    def inside(self, __a0: int, __a1: int) -> bool: ...

    def invalidate(self) -> None: ...

    def isAncestorOf(self, __a0: java.awt.Component) -> bool: ...

    def isBackgroundSet(self) -> bool: ...

    def isCursorSet(self) -> bool: ...

    def isDisplayable(self) -> bool: ...

    def isDoubleBuffered(self) -> bool: ...

    def isEnabled(self) -> bool: ...

    @overload
    def isFocusCycleRoot(self) -> bool: ...

    @overload
    def isFocusCycleRoot(self, __a0: java.awt.Container) -> bool: ...

    def isFocusOwner(self) -> bool: ...

    def isFocusTraversable(self) -> bool: ...

    def isFocusTraversalPolicyProvider(self) -> bool: ...

    def isFocusTraversalPolicySet(self) -> bool: ...

    def isFocusable(self) -> bool: ...

    def isFontSet(self) -> bool: ...

    def isForegroundSet(self) -> bool: ...

    def isLightweight(self) -> bool: ...

    @staticmethod
    def isLightweightComponent(__a0: java.awt.Component) -> bool: ...

    def isManagingFocus(self) -> bool: ...

    def isMatchingConstantsExactly(self) -> bool: ...

    def isMaximumSizeSet(self) -> bool: ...

    def isMinimumSizeSet(self) -> bool: ...

    def isOpaque(self) -> bool: ...

    def isOptimizedDrawingEnabled(self) -> bool: ...

    def isPaintingForPrint(self) -> bool: ...

    def isPaintingTile(self) -> bool: ...

    def isPreferredSizeSet(self) -> bool: ...

    def isRequestFocusEnabled(self) -> bool: ...

    def isScrollingSynced(self) -> bool:
        """
        Determines if the layouts of the views are synchronized with respect to scrolling and
         location.
        @return true if scrolling is synchronized between the two views.
        """
        ...

    def isShowing(self) -> bool: ...

    def isValid(self) -> bool: ...

    def isValidateRoot(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def keyDown(self, __a0: java.awt.Event, __a1: int) -> bool: ...

    def keyUp(self, __a0: java.awt.Event, __a1: int) -> bool: ...

    def leftPanelHasFocus(self) -> bool: ...

    @overload
    def list(self) -> None: ...

    @overload
    def list(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def list(self, __a0: java.io.PrintWriter) -> None: ...

    @overload
    def list(self, __a0: java.io.PrintStream, __a1: int) -> None: ...

    @overload
    def list(self, __a0: java.io.PrintWriter, __a1: int) -> None: ...

    def loadAddresses(self, leftProgram: ghidra.program.model.listing.Program, rightProgram: ghidra.program.model.listing.Program, leftAddresses: ghidra.program.model.address.AddressSetView, rightAddresses: ghidra.program.model.address.AddressSetView) -> None: ...

    def loadData(self, leftData: ghidra.program.model.listing.Data, rightData: ghidra.program.model.listing.Data) -> None: ...

    def loadFunctions(self, leftFunction: ghidra.program.model.listing.Function, rightFunction: ghidra.program.model.listing.Function) -> None: ...

    def locate(self, __a0: int, __a1: int) -> java.awt.Component: ...

    def location(self) -> java.awt.Point: ...

    def lostFocus(self, __a0: java.awt.Event, __a1: object) -> bool: ...

    def mouseDown(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseDrag(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseEnter(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseExit(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseMove(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseUp(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def move(self, __a0: int, __a1: int) -> None: ...

    def nextFocus(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paint(self, __a0: java.awt.Graphics) -> None: ...

    def paintAll(self, __a0: java.awt.Graphics) -> None: ...

    def paintComponents(self, __a0: java.awt.Graphics) -> None: ...

    @overload
    def paintImmediately(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def paintImmediately(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def postEvent(self, __a0: java.awt.Event) -> bool: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> bool: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> bool: ...

    def print(self, __a0: java.awt.Graphics) -> None: ...

    def printAll(self, __a0: java.awt.Graphics) -> None: ...

    def printComponents(self, __a0: java.awt.Graphics) -> None: ...

    def programRestored(self, program: ghidra.program.model.listing.Program) -> None: ...

    def putClientProperty(self, __a0: object, __a1: object) -> None: ...

    def refreshLeftPanel(self) -> None:
        """
        Refreshes the left side of this panel.
        """
        ...

    def refreshRightPanel(self) -> None:
        """
        Refreshes the right side of this panel.
        """
        ...

    @overload
    def registerKeyboardAction(self, __a0: java.awt.event.ActionListener, __a1: javax.swing.KeyStroke, __a2: int) -> None: ...

    @overload
    def registerKeyboardAction(self, __a0: java.awt.event.ActionListener, __a1: unicode, __a2: javax.swing.KeyStroke, __a3: int) -> None: ...

    @overload
    def remove(self, __a0: int) -> None: ...

    @overload
    def remove(self, __a0: java.awt.Component) -> None: ...

    @overload
    def remove(self, __a0: java.awt.MenuComponent) -> None: ...

    def removeAll(self) -> None: ...

    def removeAncestorListener(self, __a0: javax.swing.event.AncestorListener) -> None: ...

    def removeComponentListener(self, __a0: java.awt.event.ComponentListener) -> None: ...

    def removeContainerListener(self, __a0: java.awt.event.ContainerListener) -> None: ...

    def removeDualDecompileResultsListener(self, listener: ghidra.app.decompiler.component.DualDecompileResultsListener) -> bool:
        """
        Removes the indicated listener from being notified about decompile results.
        @param listener the listener
        @return true if the listener was removed.
        """
        ...

    def removeFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def removeHierarchyBoundsListener(self, __a0: java.awt.event.HierarchyBoundsListener) -> None: ...

    def removeHierarchyListener(self, __a0: java.awt.event.HierarchyListener) -> None: ...

    def removeInputMethodListener(self, __a0: java.awt.event.InputMethodListener) -> None: ...

    def removeKeyListener(self, __a0: java.awt.event.KeyListener) -> None: ...

    def removeMouseListener(self, __a0: java.awt.event.MouseListener) -> None: ...

    def removeMouseMotionListener(self, __a0: java.awt.event.MouseMotionListener) -> None: ...

    def removeMouseWheelListener(self, __a0: java.awt.event.MouseWheelListener) -> None: ...

    def removeNotify(self) -> None: ...

    @overload
    def removePropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    @overload
    def removePropertyChangeListener(self, __a0: unicode, __a1: java.beans.PropertyChangeListener) -> None: ...

    def removeVetoableChangeListener(self, __a0: java.beans.VetoableChangeListener) -> None: ...

    @overload
    def repaint(self) -> None: ...

    @overload
    def repaint(self, __a0: long) -> None: ...

    @overload
    def repaint(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def repaint(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    @overload
    def repaint(self, __a0: long, __a1: int, __a2: int, __a3: int, __a4: int) -> None: ...

    def requestDefaultFocus(self) -> bool: ...

    @overload
    def requestFocus(self) -> None: ...

    @overload
    def requestFocus(self, __a0: bool) -> bool: ...

    @overload
    def requestFocus(self, __a0: java.awt.event.FocusEvent.Cause) -> None: ...

    @overload
    def requestFocusInWindow(self) -> bool: ...

    @overload
    def requestFocusInWindow(self, __a0: java.awt.event.FocusEvent.Cause) -> bool: ...

    def resetKeyboardActions(self) -> None: ...

    def reshape(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    @overload
    def resize(self, __a0: java.awt.Dimension) -> None: ...

    @overload
    def resize(self, __a0: int, __a1: int) -> None: ...

    def revalidate(self) -> None: ...

    def scrollRectToVisible(self, __a0: java.awt.Rectangle) -> None: ...

    def setActionMap(self, __a0: javax.swing.ActionMap) -> None: ...

    def setAlignmentX(self, __a0: float) -> None: ...

    def setAlignmentY(self, __a0: float) -> None: ...

    def setAutoscrolls(self, __a0: bool) -> None: ...

    def setBackground(self, __a0: java.awt.Color) -> None: ...

    def setBorder(self, __a0: javax.swing.border.Border) -> None: ...

    def setBottomComponent(self, comp: javax.swing.JComponent) -> None:
        """
        Sets the component displayed in the bottom of this panel.
        @param comp the component.
        """
        ...

    @overload
    def setBounds(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def setBounds(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def setComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def setComponentPopupMenu(self, __a0: javax.swing.JPopupMenu) -> None: ...

    def setComponentZOrder(self, __a0: java.awt.Component, __a1: int) -> None: ...

    def setCursor(self, __a0: java.awt.Cursor) -> None: ...

    def setDebugGraphicsOptions(self, __a0: int) -> None: ...

    @staticmethod
    def setDefaultLocale(__a0: java.util.Locale) -> None: ...

    def setDoubleBuffered(self, __a0: bool) -> None: ...

    def setDropTarget(self, __a0: java.awt.dnd.DropTarget) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    @overload
    def setFieldPanelCoordinator(self, fieldPanelCoordinator: ghidra.app.decompiler.component.DualDecompilerFieldPanelCoordinator) -> None:
        """
        Sets the coordinator for the two decompiler panels within this code comparison panel.
         It coordinates their scrolling and location synchronization.
        @param fieldPanelCoordinator the coordinator for the two decompiler panels
        """
        ...

    @overload
    def setFieldPanelCoordinator(self, __a0: docking.widgets.fieldpanel.internal.FieldPanelCoordinator) -> None: ...

    def setFocusCycleRoot(self, __a0: bool) -> None: ...

    def setFocusTraversalKeys(self, __a0: int, __a1: java.util.Set) -> None: ...

    def setFocusTraversalKeysEnabled(self, __a0: bool) -> None: ...

    def setFocusTraversalPolicy(self, __a0: java.awt.FocusTraversalPolicy) -> None: ...

    def setFocusTraversalPolicyProvider(self, __a0: bool) -> None: ...

    def setFocusable(self, __a0: bool) -> None: ...

    def setFont(self, __a0: java.awt.Font) -> None: ...

    def setForeground(self, __a0: java.awt.Color) -> None: ...

    def setHighlightControllers(self, leftHighlightController: ghidra.app.decompiler.component.ClangHighlightController, rightHighlightController: ghidra.app.decompiler.component.ClangHighlightController) -> None:
        """
        Sets the highlight controllers for both decompiler panels.
        @param leftHighlightController the left side's highlight controller
        @param rightHighlightController the right side's highlight controller
        """
        ...

    def setIgnoreRepaint(self, __a0: bool) -> None: ...

    def setInheritsPopupMenu(self, __a0: bool) -> None: ...

    def setInputMap(self, __a0: int, __a1: javax.swing.InputMap) -> None: ...

    def setInputVerifier(self, __a0: javax.swing.InputVerifier) -> None: ...

    def setLayout(self, __a0: java.awt.LayoutManager) -> None: ...

    def setLeftTitle(self, leftTitle: unicode) -> None:
        """
        Sets the title for the left side's decompiler.
        @param leftTitle the title
        """
        ...

    def setLocale(self, __a0: java.util.Locale) -> None: ...

    @overload
    def setLocation(self, __a0: java.awt.Point) -> None: ...

    @overload
    def setLocation(self, __a0: int, __a1: int) -> None: ...

    def setMaximumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMinimumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMixingCutoutShape(self, __a0: java.awt.Shape) -> None: ...

    def setMouseNavigationEnabled(self, enabled: bool) -> None:
        """
        Disable mouse navigation from within this dual decompiler panel.
        @param enabled false disables navigation
        """
        ...

    def setName(self, __a0: unicode) -> None: ...

    def setNextFocusableComponent(self, __a0: java.awt.Component) -> None: ...

    def setOpaque(self, __a0: bool) -> None: ...

    def setPreferredSize(self, __a0: java.awt.Dimension) -> None: ...

    def setRequestFocusEnabled(self, __a0: bool) -> None: ...

    def setRightTitle(self, rightTitle: unicode) -> None:
        """
        Sets the title for the right side's decompiler.
        @param rightTitle the title
        """
        ...

    def setScrollingSyncState(self, syncScrolling: bool) -> None:
        """
        Sets whether or not scrolling is synchronized.
        @param syncScrolling true means synchronize scrolling and location between the two views.
        """
        ...

    def setShowTitles(self, showTitles: bool) -> None: ...

    @overload
    def setSize(self, __a0: java.awt.Dimension) -> None: ...

    @overload
    def setSize(self, __a0: int, __a1: int) -> None: ...

    def setTitlePrefixes(self, leftTitlePrefix: unicode, rightTitlePrefix: unicode) -> None: ...

    def setToolTipText(self, __a0: unicode) -> None: ...

    def setTopComponent(self, comp: javax.swing.JComponent) -> None:
        """
        Sets the component displayed in the top of this panel.
        @param comp the component.
        """
        ...

    def setTransferHandler(self, __a0: javax.swing.TransferHandler) -> None: ...

    def setUI(self, __a0: javax.swing.plaf.PanelUI) -> None: ...

    def setVerifyInputWhenFocusTarget(self, __a0: bool) -> None: ...

    def setVisible(self, aFlag: bool) -> None: ...

    @overload
    def show(self) -> None: ...

    @overload
    def show(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    def transferFocus(self) -> None: ...

    def transferFocusBackward(self) -> None: ...

    def transferFocusDownCycle(self) -> None: ...

    def transferFocusUpCycle(self) -> None: ...

    def unregisterKeyboardAction(self, __a0: javax.swing.KeyStroke) -> None: ...

    def update(self, __a0: java.awt.Graphics) -> None: ...

    def updateActionEnablement(self) -> None: ...

    def updateUI(self) -> None: ...

    def validate(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def actions(self) -> List[docking.action.DockingAction]: ...

    @property
    def bottomComponent(self) -> None: ...  # No getter available.

    @bottomComponent.setter
    def bottomComponent(self, value: javax.swing.JComponent) -> None: ...

    @property
    def component(self) -> javax.swing.JComponent: ...

    @property
    def fieldPanelCoordinator(self) -> None: ...  # No getter available.

    @fieldPanelCoordinator.setter
    def fieldPanelCoordinator(self, value: ghidra.app.decompiler.component.DualDecompilerFieldPanelCoordinator) -> None: ...

    @property
    def focusedDecompilerPanel(self) -> ghidra.app.decompiler.component.CDisplayPanel: ...

    @property
    def leftAddresses(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def leftDecompilerPanel(self) -> ghidra.app.decompiler.component.DecompilerPanel: ...

    @property
    def leftFieldPanel(self) -> docking.widgets.fieldpanel.FieldPanel: ...

    @property
    def leftPanel(self) -> ghidra.app.decompiler.component.CDisplayPanel: ...

    @property
    def leftTitle(self) -> None: ...  # No getter available.

    @leftTitle.setter
    def leftTitle(self, value: unicode) -> None: ...

    @property
    def matchingConstantsExactly(self) -> bool: ...

    @property
    def mouseNavigationEnabled(self) -> None: ...  # No getter available.

    @mouseNavigationEnabled.setter
    def mouseNavigationEnabled(self, value: bool) -> None: ...

    @property
    def panelThisSupersedes(self) -> java.lang.Class: ...

    @property
    def rightAddresses(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def rightDecompilerPanel(self) -> ghidra.app.decompiler.component.DecompilerPanel: ...

    @property
    def rightFieldPanel(self) -> docking.widgets.fieldpanel.FieldPanel: ...

    @property
    def rightPanel(self) -> ghidra.app.decompiler.component.CDisplayPanel: ...

    @property
    def rightTitle(self) -> None: ...  # No getter available.

    @rightTitle.setter
    def rightTitle(self, value: unicode) -> None: ...

    @property
    def title(self) -> unicode: ...

    @property
    def topComponent(self) -> None: ...  # No getter available.

    @topComponent.setter
    def topComponent(self, value: javax.swing.JComponent) -> None: ...

    @property
    def visible(self) -> bool: ...

    @visible.setter
    def visible(self, value: bool) -> None: ...