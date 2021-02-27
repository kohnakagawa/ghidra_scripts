from typing import List
import docking.widgets.tree
import docking.widgets.tree.internal
import docking.widgets.tree.support
import docking.widgets.tree.tasks
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
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
import javax.swing.tree


class SymbolGTree(docking.widgets.tree.GTree):




    def __init__(self, __a0: docking.widgets.tree.GTreeNode, __a1: ghidra.app.plugin.core.symboltree.SymbolTreePlugin): ...



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

    def addFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def addGTModelListener(self, __a0: javax.swing.event.TreeModelListener) -> None: ...

    def addGTreeSelectionListener(self, __a0: docking.widgets.tree.support.GTreeSelectionListener) -> None: ...

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

    def addSelectionPath(self, __a0: javax.swing.tree.TreePath) -> None: ...

    def addTreeExpansionListener(self, __a0: javax.swing.event.TreeExpansionListener) -> None: ...

    def addVetoableChangeListener(self, __a0: java.beans.VetoableChangeListener) -> None: ...

    def applyComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def areFocusTraversalKeysSet(self, __a0: int) -> bool: ...

    def cancelWork(self) -> None: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> int: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> int: ...

    def clearFilter(self) -> None: ...

    def clearSelectionPaths(self) -> None: ...

    def clearSizeCache(self) -> None: ...

    def collapseAll(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

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

    def expandAll(self) -> None: ...

    @overload
    def expandPath(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    @overload
    def expandPath(self, __a0: javax.swing.tree.TreePath) -> None: ...

    @overload
    def expandPaths(self, __a0: List[javax.swing.tree.TreePath]) -> None: ...

    @overload
    def expandPaths(self, __a0: List[object]) -> None: ...

    def expandTree(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def expandedStateRestored(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def filterChanged(self) -> None: ...

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

    def getAccessibleContext(self) -> javax.accessibility.AccessibleContext: ...

    def getActionForKeyStroke(self, __a0: javax.swing.KeyStroke) -> java.awt.event.ActionListener: ...

    def getActionMap(self) -> javax.swing.ActionMap: ...

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

    def getCellEditor(self) -> javax.swing.CellEditor: ...

    def getCellRenderer(self) -> docking.widgets.tree.support.GTreeRenderer: ...

    def getClass(self) -> java.lang.Class: ...

    def getClientProperty(self, __a0: object) -> object: ...

    def getColorModel(self) -> java.awt.image.ColorModel: ...

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

    def getDragNDropHandler(self) -> docking.widgets.tree.support.GTreeDragNDropHandler: ...

    def getDropTarget(self) -> java.awt.dnd.DropTarget: ...

    @overload
    def getExpandedPaths(self) -> List[object]: ...

    @overload
    def getExpandedPaths(self, __a0: docking.widgets.tree.GTreeNode) -> List[object]: ...

    def getFilter(self) -> docking.widgets.tree.support.GTreeFilter: ...

    def getFilterField(self) -> java.awt.Component: ...

    def getFilterProvider(self) -> docking.widgets.tree.GTreeFilterProvider: ...

    def getFilterText(self) -> unicode: ...

    def getFocusCycleRootAncestor(self) -> java.awt.Container: ...

    def getFocusListeners(self) -> List[java.awt.event.FocusListener]: ...

    def getFocusTraversalKeys(self, __a0: int) -> java.util.Set: ...

    def getFocusTraversalKeysEnabled(self) -> bool: ...

    def getFocusTraversalPolicy(self) -> java.awt.FocusTraversalPolicy: ...

    def getFont(self) -> java.awt.Font: ...

    def getFontMetrics(self, __a0: java.awt.Font) -> java.awt.FontMetrics: ...

    def getForeground(self) -> java.awt.Color: ...

    def getGTSelectionModel(self) -> docking.widgets.tree.internal.GTreeSelectionModel: ...

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

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getLocale(self) -> java.util.Locale: ...

    @overload
    def getLocation(self) -> java.awt.Point: ...

    @overload
    def getLocation(self, __a0: java.awt.Point) -> java.awt.Point: ...

    def getLocationOnScreen(self) -> java.awt.Point: ...

    def getMaximumSize(self) -> java.awt.Dimension: ...

    def getMinimumSize(self) -> java.awt.Dimension: ...

    def getModel(self) -> docking.widgets.tree.internal.GTreeModel: ...

    def getModelNodeForPath(self, __a0: javax.swing.tree.TreePath) -> docking.widgets.tree.GTreeNode: ...

    def getModelRoot(self) -> docking.widgets.tree.GTreeNode: ...

    def getMouseListeners(self) -> List[java.awt.event.MouseListener]: ...

    def getMouseMotionListeners(self) -> List[java.awt.event.MouseMotionListener]: ...

    @overload
    def getMousePosition(self) -> java.awt.Point: ...

    @overload
    def getMousePosition(self, __a0: bool) -> java.awt.Point: ...

    def getMouseWheelListeners(self) -> List[java.awt.event.MouseWheelListener]: ...

    def getName(self) -> unicode: ...

    def getNextFocusableComponent(self) -> java.awt.Component: ...

    def getNodeForLocation(self, __a0: int, __a1: int) -> docking.widgets.tree.GTreeNode: ...

    def getParent(self) -> java.awt.Container: ...

    def getPathBounds(self, __a0: javax.swing.tree.TreePath) -> java.awt.Rectangle: ...

    def getPathForLocation(self, __a0: int, __a1: int) -> javax.swing.tree.TreePath: ...

    def getPathForRow(self, __a0: int) -> javax.swing.tree.TreePath: ...

    def getPopupLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    def getPreferredSize(self) -> java.awt.Dimension: ...

    @overload
    def getPropertyChangeListeners(self) -> List[java.beans.PropertyChangeListener]: ...

    @overload
    def getPropertyChangeListeners(self, __a0: unicode) -> List[java.beans.PropertyChangeListener]: ...

    def getRegisteredKeyStrokes(self) -> List[javax.swing.KeyStroke]: ...

    def getRootPane(self) -> javax.swing.JRootPane: ...

    def getRowCount(self) -> int: ...

    def getRowForPath(self, __a0: javax.swing.tree.TreePath) -> int: ...

    def getSelectionModel(self) -> javax.swing.tree.TreeSelectionModel: ...

    def getSelectionPath(self) -> javax.swing.tree.TreePath: ...

    def getSelectionPaths(self) -> List[javax.swing.tree.TreePath]: ...

    @overload
    def getSize(self) -> java.awt.Dimension: ...

    @overload
    def getSize(self, __a0: java.awt.Dimension) -> java.awt.Dimension: ...

    def getToolTipLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    @overload
    def getToolTipText(self) -> unicode: ...

    @overload
    def getToolTipText(self, __a0: java.awt.event.MouseEvent) -> unicode: ...

    def getToolkit(self) -> java.awt.Toolkit: ...

    def getTopLevelAncestor(self) -> java.awt.Container: ...

    def getTransferHandler(self) -> javax.swing.TransferHandler: ...

    def getTreeLock(self) -> object: ...

    @overload
    def getTreeState(self) -> docking.widgets.tree.GTreeState: ...

    @overload
    def getTreeState(self, __a0: docking.widgets.tree.GTreeNode) -> docking.widgets.tree.GTreeState: ...

    def getUI(self) -> javax.swing.plaf.ComponentUI: ...

    def getUIClassID(self) -> unicode: ...

    def getVerifyInputWhenFocusTarget(self) -> bool: ...

    def getVetoableChangeListeners(self) -> List[java.beans.VetoableChangeListener]: ...

    def getViewNodeForPath(self, __a0: javax.swing.tree.TreePath) -> docking.widgets.tree.GTreeNode: ...

    def getViewPosition(self) -> java.awt.Point: ...

    def getViewRect(self) -> java.awt.Rectangle: ...

    def getViewRoot(self) -> docking.widgets.tree.GTreeNode: ...

    def getVisibleRect(self) -> java.awt.Rectangle: ...

    def getWidth(self) -> int: ...

    def getX(self) -> int: ...

    def getY(self) -> int: ...

    def gotFocus(self, __a0: java.awt.Event, __a1: object) -> bool: ...

    def grabFocus(self) -> None: ...

    def handleEvent(self, __a0: java.awt.Event) -> bool: ...

    def hasFilterText(self) -> bool: ...

    def hasFocus(self) -> bool: ...

    def hashCode(self) -> int: ...

    def hide(self) -> None: ...

    def imageUpdate(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: int, __a4: int, __a5: int) -> bool: ...

    def inside(self, __a0: int, __a1: int) -> bool: ...

    def invalidate(self) -> None: ...

    def isAncestorOf(self, __a0: java.awt.Component) -> bool: ...

    def isBackgroundSet(self) -> bool: ...

    def isBusy(self) -> bool: ...

    def isCollapsed(self, __a0: javax.swing.tree.TreePath) -> bool: ...

    def isCursorSet(self) -> bool: ...

    def isDisplayable(self) -> bool: ...

    def isDisposed(self) -> bool: ...

    def isDoubleBuffered(self) -> bool: ...

    def isEditing(self) -> bool: ...

    def isEnabled(self) -> bool: ...

    def isExpanded(self, __a0: javax.swing.tree.TreePath) -> bool: ...

    def isFiltered(self) -> bool: ...

    def isFilteringEnabled(self) -> bool: ...

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

    def isMaximumSizeSet(self) -> bool: ...

    def isMinimumSizeSet(self) -> bool: ...

    def isMyJTree(self, __a0: javax.swing.JTree) -> bool: ...

    def isOpaque(self) -> bool: ...

    def isOptimizedDrawingEnabled(self) -> bool: ...

    def isPaintingForPrint(self) -> bool: ...

    def isPaintingTile(self) -> bool: ...

    def isPathEditable(self, __a0: javax.swing.tree.TreePath) -> bool: ...

    def isPathSelected(self, __a0: javax.swing.tree.TreePath) -> bool: ...

    def isPreferredSizeSet(self) -> bool: ...

    def isRequestFocusEnabled(self) -> bool: ...

    def isRootAllowedToCollapse(self) -> bool: ...

    def isRootVisible(self) -> bool: ...

    def isShowing(self) -> bool: ...

    def isValid(self) -> bool: ...

    def isValidateRoot(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def keyDown(self, __a0: java.awt.Event, __a1: int) -> bool: ...

    def keyUp(self, __a0: java.awt.Event, __a1: int) -> bool: ...

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

    @staticmethod
    def printEvent(__a0: java.io.PrintWriter, __a1: unicode, __a2: javax.swing.event.TreeModelEvent) -> None: ...

    def putClientProperty(self, __a0: object, __a1: object) -> None: ...

    @overload
    def refilterLater(self) -> None: ...

    @overload
    def refilterLater(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def refilterNow(self) -> None: ...

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

    def removeFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def removeGTModelListener(self, __a0: javax.swing.event.TreeModelListener) -> None: ...

    def removeGTreeSelectionListener(self, __a0: docking.widgets.tree.support.GTreeSelectionListener) -> None: ...

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

    def removeTreeExpansionListener(self, __a0: javax.swing.event.TreeExpansionListener) -> None: ...

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

    def restoreTreeState(self, __a0: docking.widgets.tree.GTreeState) -> None: ...

    def revalidate(self) -> None: ...

    def runBulkTask(self, __a0: docking.widgets.tree.tasks.GTreeBulkTask) -> None: ...

    @overload
    def runTask(self, __a0: docking.widgets.tree.GTreeTask) -> None: ...

    @overload
    def runTask(self, __a0: ghidra.util.task.MonitoredRunnable) -> None: ...

    def scrollPathToVisible(self, __a0: javax.swing.tree.TreePath) -> None: ...

    def scrollRectToVisible(self, __a0: java.awt.Rectangle) -> None: ...

    def setActionMap(self, __a0: javax.swing.ActionMap) -> None: ...

    def setActiveDropTargetNode(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def setAlignmentX(self, __a0: float) -> None: ...

    def setAlignmentY(self, __a0: float) -> None: ...

    def setAutoscrolls(self, __a0: bool) -> None: ...

    def setBackground(self, __a0: java.awt.Color) -> None: ...

    def setBorder(self, __a0: javax.swing.border.Border) -> None: ...

    @overload
    def setBounds(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def setBounds(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def setBusy(self, __a0: bool) -> None: ...

    def setCellEditor(self, __a0: javax.swing.tree.TreeCellEditor) -> None: ...

    def setCellRenderer(self, __a0: docking.widgets.tree.support.GTreeRenderer) -> None: ...

    def setComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def setComponentPopupMenu(self, __a0: javax.swing.JPopupMenu) -> None: ...

    def setComponentZOrder(self, __a0: java.awt.Component, __a1: int) -> None: ...

    def setCursor(self, __a0: java.awt.Cursor) -> None: ...

    def setDataTransformer(self, __a0: ghidra.util.FilterTransformer) -> None: ...

    def setDebugGraphicsOptions(self, __a0: int) -> None: ...

    @staticmethod
    def setDefaultLocale(__a0: java.util.Locale) -> None: ...

    def setDoubleBuffered(self, __a0: bool) -> None: ...

    def setDragNDropHandler(self, __a0: docking.widgets.tree.support.GTreeDragNDropHandler) -> None: ...

    def setDropTarget(self, __a0: java.awt.dnd.DropTarget) -> None: ...

    def setEditable(self, __a0: bool) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    def setEventsEnabled(self, __a0: bool) -> None: ...

    def setFilterFieldEnabled(self, __a0: bool) -> None: ...

    def setFilterProvider(self, __a0: docking.widgets.tree.GTreeFilterProvider) -> None: ...

    def setFilterText(self, __a0: unicode) -> None: ...

    def setFilterVisible(self, __a0: bool) -> None: ...

    def setFilteringEnabled(self, __a0: bool) -> None: ...

    def setFocusCycleRoot(self, __a0: bool) -> None: ...

    def setFocusTraversalKeys(self, __a0: int, __a1: java.util.Set) -> None: ...

    def setFocusTraversalKeysEnabled(self, __a0: bool) -> None: ...

    def setFocusTraversalPolicy(self, __a0: java.awt.FocusTraversalPolicy) -> None: ...

    def setFocusTraversalPolicyProvider(self, __a0: bool) -> None: ...

    def setFocusable(self, __a0: bool) -> None: ...

    def setFont(self, __a0: java.awt.Font) -> None: ...

    def setForeground(self, __a0: java.awt.Color) -> None: ...

    def setHorizontalScrollPolicy(self, __a0: int) -> None: ...

    def setIgnoreRepaint(self, __a0: bool) -> None: ...

    def setInheritsPopupMenu(self, __a0: bool) -> None: ...

    def setInputMap(self, __a0: int, __a1: javax.swing.InputMap) -> None: ...

    def setInputVerifier(self, __a0: javax.swing.InputVerifier) -> None: ...

    def setLayout(self, __a0: java.awt.LayoutManager) -> None: ...

    def setLocale(self, __a0: java.util.Locale) -> None: ...

    @overload
    def setLocation(self, __a0: java.awt.Point) -> None: ...

    @overload
    def setLocation(self, __a0: int, __a1: int) -> None: ...

    def setMaximumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMinimumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMixingCutoutShape(self, __a0: java.awt.Shape) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setNextFocusableComponent(self, __a0: java.awt.Component) -> None: ...

    def setNodeEditable(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def setOpaque(self, __a0: bool) -> None: ...

    def setPaintHandlesForLeafNodes(self, __a0: bool) -> None: ...

    def setPreferredSize(self, __a0: java.awt.Dimension) -> None: ...

    def setProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def setRequestFocusEnabled(self, __a0: bool) -> None: ...

    def setRootNode(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def setRootNodeAllowedToCollapse(self, __a0: bool) -> None: ...

    def setRootVisible(self, __a0: bool) -> None: ...

    def setRowHeight(self, __a0: int) -> None: ...

    def setScrollableUnitIncrement(self, __a0: int) -> None: ...

    def setSelectedNode(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def setSelectedNodeByNamePath(self, __a0: List[unicode]) -> None: ...

    def setSelectedNodeByPathName(self, __a0: javax.swing.tree.TreePath) -> None: ...

    @overload
    def setSelectedNodes(self, __a0: List[docking.widgets.tree.GTreeNode]) -> None: ...

    @overload
    def setSelectedNodes(self, __a0: java.util.Collection) -> None: ...

    def setSelectionModel(self, __a0: docking.widgets.tree.internal.GTreeSelectionModel) -> None: ...

    def setSelectionPath(self, __a0: javax.swing.tree.TreePath) -> None: ...

    @overload
    def setSelectionPaths(self, __a0: List[javax.swing.tree.TreePath]) -> None: ...

    @overload
    def setSelectionPaths(self, __a0: List[object]) -> None: ...

    @overload
    def setSelectionPaths(self, __a0: List[javax.swing.tree.TreePath], __a1: docking.widgets.tree.support.GTreeSelectionEvent.EventOrigin) -> None: ...

    def setSeletedNodeByName(self, __a0: docking.widgets.tree.GTreeNode, __a1: unicode) -> None: ...

    def setShowsRootHandles(self, __a0: bool) -> None: ...

    @overload
    def setSize(self, __a0: java.awt.Dimension) -> None: ...

    @overload
    def setSize(self, __a0: int, __a1: int) -> None: ...

    def setToolTipText(self, __a0: unicode) -> None: ...

    def setTransferHandler(self, __a0: javax.swing.TransferHandler) -> None: ...

    def setUI(self, __a0: javax.swing.plaf.PanelUI) -> None: ...

    def setVerifyInputWhenFocusTarget(self, __a0: bool) -> None: ...

    def setViewPosition(self, __a0: java.awt.Point) -> None: ...

    def setVisible(self, __a0: bool) -> None: ...

    @overload
    def show(self) -> None: ...

    @overload
    def show(self, __a0: bool) -> None: ...

    def startEditing(self, __a0: docking.widgets.tree.GTreeNode, __a1: unicode) -> None: ...

    def stopEditing(self) -> None: ...

    def toString(self) -> unicode: ...

    def transferFocus(self) -> None: ...

    def transferFocusBackward(self) -> None: ...

    def transferFocusDownCycle(self) -> None: ...

    def transferFocusUpCycle(self) -> None: ...

    def unregisterKeyboardAction(self, __a0: javax.swing.KeyStroke) -> None: ...

    def update(self, __a0: java.awt.Graphics) -> None: ...

    def updateUI(self) -> None: ...

    def validate(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def nodeEditable(self) -> None: ...  # No getter available.

    @nodeEditable.setter
    def nodeEditable(self, value: docking.widgets.tree.GTreeNode) -> None: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.model.listing.Program) -> None: ...
