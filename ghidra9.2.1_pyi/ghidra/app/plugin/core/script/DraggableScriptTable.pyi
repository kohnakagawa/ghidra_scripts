from typing import List
import docking
import docking.actions
import docking.dnd
import docking.widgets.table
import ghidra.app.nav
import ghidra.app.services
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.table
import java.awt
import java.awt.datatransfer
import java.awt.dnd
import java.awt.event
import java.awt.im
import java.awt.image
import java.awt.print
import java.beans
import java.io
import java.lang
import java.text
import java.util
import javax.accessibility
import javax.print
import javax.print.attribute
import javax.swing
import javax.swing.border
import javax.swing.event
import javax.swing.plaf
import javax.swing.table


class DraggableScriptTable(ghidra.util.table.GhidraTable, docking.dnd.Draggable):




    def __init__(self, __a0: ghidra.app.plugin.core.script.GhidraScriptComponentProvider, __a1: javax.swing.table.TableModel): ...



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

    def addColumn(self, __a0: javax.swing.table.TableColumn) -> None: ...

    def addColumnSelectionInterval(self, __a0: int, __a1: int) -> None: ...

    def addComponentListener(self, __a0: java.awt.event.ComponentListener) -> None: ...

    def addContainerListener(self, __a0: java.awt.event.ContainerListener) -> None: ...

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

    def addRowSelectionInterval(self, __a0: int, __a1: int) -> None: ...

    def addVetoableChangeListener(self, __a0: java.beans.VetoableChangeListener) -> None: ...

    def applyComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def areActionsEnabled(self) -> bool: ...

    def areFocusTraversalKeysSet(self, __a0: int) -> bool: ...

    def changeSelection(self, __a0: int, __a1: int, __a2: bool, __a3: bool) -> None: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> int: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> int: ...

    def clearSelection(self) -> None: ...

    def columnAdded(self, __a0: javax.swing.event.TableColumnModelEvent) -> None: ...

    def columnAtPoint(self, __a0: java.awt.Point) -> int: ...

    def columnMarginChanged(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

    def columnMoved(self, __a0: javax.swing.event.TableColumnModelEvent) -> None: ...

    def columnRemoved(self, __a0: javax.swing.event.TableColumnModelEvent) -> None: ...

    def columnSelectionChanged(self, __a0: javax.swing.event.ListSelectionEvent) -> None: ...

    def computeVisibleRect(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def contains(self, __a0: java.awt.Point) -> bool: ...

    @overload
    def contains(self, __a0: int, __a1: int) -> bool: ...

    def convertColumnIndexToModel(self, __a0: int) -> int: ...

    def convertColumnIndexToView(self, __a0: int) -> int: ...

    def convertRowIndexToModel(self, __a0: int) -> int: ...

    def convertRowIndexToView(self, __a0: int) -> int: ...

    def countComponents(self) -> int: ...

    def createDefaultColumnsFromModel(self) -> None: ...

    @overload
    def createImage(self, __a0: java.awt.image.ImageProducer) -> java.awt.Image: ...

    @overload
    def createImage(self, __a0: int, __a1: int) -> java.awt.Image: ...

    @staticmethod
    def createScrollPaneForTable(__a0: javax.swing.JTable) -> javax.swing.JScrollPane: ...

    @staticmethod
    def createSharedActions(__a0: docking.Tool, __a1: docking.actions.ToolActions, __a2: unicode) -> None: ...

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

    def dragCanceled(self, __a0: java.awt.dnd.DragSourceDropEvent) -> None: ...

    @overload
    def editCellAt(self, __a0: int, __a1: int) -> bool: ...

    @overload
    def editCellAt(self, __a0: int, __a1: int, __a2: java.util.EventObject) -> bool: ...

    def editingCanceled(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

    def editingStopped(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

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

    def getAccessibleContext(self) -> javax.accessibility.AccessibleContext: ...

    def getActionForKeyStroke(self, __a0: javax.swing.KeyStroke) -> java.awt.event.ActionListener: ...

    def getActionMap(self) -> javax.swing.ActionMap: ...

    def getAlignmentX(self) -> float: ...

    def getAlignmentY(self) -> float: ...

    def getAncestorListeners(self) -> List[javax.swing.event.AncestorListener]: ...

    def getAutoCreateColumnsFromModel(self) -> bool: ...

    def getAutoCreateRowSorter(self) -> bool: ...

    def getAutoResizeMode(self) -> int: ...

    def getAutoscrolls(self) -> bool: ...

    def getBackground(self) -> java.awt.Color: ...

    def getBaseline(self, __a0: int, __a1: int) -> int: ...

    def getBaselineResizeBehavior(self) -> java.awt.Component.BaselineResizeBehavior: ...

    def getBorder(self) -> javax.swing.border.Border: ...

    @overload
    def getBounds(self) -> java.awt.Rectangle: ...

    @overload
    def getBounds(self, __a0: java.awt.Rectangle) -> java.awt.Rectangle: ...

    @overload
    def getCellEditor(self) -> javax.swing.table.TableCellEditor: ...

    @overload
    def getCellEditor(self, __a0: int, __a1: int) -> javax.swing.table.TableCellEditor: ...

    def getCellRect(self, __a0: int, __a1: int, __a2: bool) -> java.awt.Rectangle: ...

    def getCellRenderer(self, __a0: int, __a1: int) -> javax.swing.table.TableCellRenderer: ...

    def getCellRendererOverride(self, __a0: int, __a1: int) -> javax.swing.table.TableCellRenderer: ...

    def getCellSelectionEnabled(self) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClientProperty(self, __a0: object) -> object: ...

    def getColorModel(self) -> java.awt.image.ColorModel: ...

    def getColumn(self, __a0: object) -> javax.swing.table.TableColumn: ...

    def getColumnClass(self, __a0: int) -> java.lang.Class: ...

    def getColumnCount(self) -> int: ...

    def getColumnModel(self) -> javax.swing.table.TableColumnModel: ...

    def getColumnName(self, __a0: int) -> unicode: ...

    def getColumnSelectionAllowed(self) -> bool: ...

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

    def getConfigurableColumnTableModel(self) -> docking.widgets.table.ConfigurableColumnTableModel: ...

    def getContainerListeners(self) -> List[java.awt.event.ContainerListener]: ...

    def getCursor(self) -> java.awt.Cursor: ...

    def getDebugGraphicsOptions(self) -> int: ...

    def getDefaultEditor(self, __a0: java.lang.Class) -> javax.swing.table.TableCellEditor: ...

    @staticmethod
    def getDefaultLocale() -> java.util.Locale: ...

    def getDefaultRenderer(self, __a0: java.lang.Class) -> javax.swing.table.TableCellRenderer: ...

    def getDragAction(self) -> int: ...

    def getDragEnabled(self) -> bool: ...

    def getDragSourceListener(self) -> java.awt.dnd.DragSourceListener: ...

    def getDropLocation(self) -> javax.swing.JTable.DropLocation: ...

    def getDropMode(self) -> javax.swing.DropMode: ...

    def getDropTarget(self) -> java.awt.dnd.DropTarget: ...

    def getEditingColumn(self) -> int: ...

    def getEditingRow(self) -> int: ...

    def getEditorComponent(self) -> java.awt.Component: ...

    def getFillsViewportHeight(self) -> bool: ...

    def getFocusCycleRootAncestor(self) -> java.awt.Container: ...

    def getFocusListeners(self) -> List[java.awt.event.FocusListener]: ...

    def getFocusTraversalKeys(self, __a0: int) -> java.util.Set: ...

    def getFocusTraversalKeysEnabled(self) -> bool: ...

    def getFocusTraversalPolicy(self) -> java.awt.FocusTraversalPolicy: ...

    def getFont(self) -> java.awt.Font: ...

    def getFontMetrics(self, __a0: java.awt.Font) -> java.awt.FontMetrics: ...

    def getForeground(self) -> java.awt.Color: ...

    def getGraphics(self) -> java.awt.Graphics: ...

    def getGraphicsConfiguration(self) -> java.awt.GraphicsConfiguration: ...

    def getGridColor(self) -> java.awt.Color: ...

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

    def getIntercellSpacing(self) -> java.awt.Dimension: ...

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

    def getModel(self) -> javax.swing.table.TableModel: ...

    def getMouseListeners(self) -> List[java.awt.event.MouseListener]: ...

    def getMouseMotionListeners(self) -> List[java.awt.event.MouseMotionListener]: ...

    @overload
    def getMousePosition(self) -> java.awt.Point: ...

    @overload
    def getMousePosition(self, __a0: bool) -> java.awt.Point: ...

    def getMouseWheelListeners(self) -> List[java.awt.event.MouseWheelListener]: ...

    def getName(self) -> unicode: ...

    def getNextFocusableComponent(self) -> java.awt.Component: ...

    def getParent(self) -> java.awt.Container: ...

    def getPopupLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    def getPreferenceKey(self) -> unicode: ...

    def getPreferredScrollableViewportSize(self) -> java.awt.Dimension: ...

    def getPreferredSize(self) -> java.awt.Dimension: ...

    def getPrintable(self, __a0: javax.swing.JTable.PrintMode, __a1: java.text.MessageFormat, __a2: java.text.MessageFormat) -> java.awt.print.Printable: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getProgramSelection(self) -> ghidra.program.util.ProgramSelection: ...

    @overload
    def getPropertyChangeListeners(self) -> List[java.beans.PropertyChangeListener]: ...

    @overload
    def getPropertyChangeListeners(self, __a0: unicode) -> List[java.beans.PropertyChangeListener]: ...

    def getRegisteredKeyStrokes(self) -> List[javax.swing.KeyStroke]: ...

    def getRootPane(self) -> javax.swing.JRootPane: ...

    def getRowCount(self) -> int: ...

    @overload
    def getRowHeight(self) -> int: ...

    @overload
    def getRowHeight(self, __a0: int) -> int: ...

    def getRowMargin(self) -> int: ...

    def getRowSelectionAllowed(self) -> bool: ...

    def getRowSorter(self) -> javax.swing.RowSorter: ...

    def getScrollableBlockIncrement(self, __a0: java.awt.Rectangle, __a1: int, __a2: int) -> int: ...

    def getScrollableTracksViewportHeight(self) -> bool: ...

    def getScrollableTracksViewportWidth(self) -> bool: ...

    def getScrollableUnitIncrement(self, __a0: java.awt.Rectangle, __a1: int, __a2: int) -> int: ...

    def getSelectedColumn(self) -> int: ...

    def getSelectedColumnCount(self) -> int: ...

    def getSelectedColumns(self) -> List[int]: ...

    def getSelectedRow(self) -> int: ...

    def getSelectedRowCount(self) -> int: ...

    def getSelectedRows(self) -> List[int]: ...

    def getSelectionBackground(self) -> java.awt.Color: ...

    def getSelectionForeground(self) -> java.awt.Color: ...

    def getSelectionManager(self) -> docking.widgets.table.SelectionManager: ...

    def getSelectionModel(self) -> javax.swing.ListSelectionModel: ...

    def getShowHorizontalLines(self) -> bool: ...

    def getShowVerticalLines(self) -> bool: ...

    @overload
    def getSize(self) -> java.awt.Dimension: ...

    @overload
    def getSize(self, __a0: java.awt.Dimension) -> java.awt.Dimension: ...

    def getSurrendersFocusOnKeystroke(self) -> bool: ...

    def getTableColumnPopupMenu(self, __a0: int) -> javax.swing.JPopupMenu: ...

    def getTableHeader(self) -> javax.swing.table.JTableHeader: ...

    def getToolTipLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    @overload
    def getToolTipText(self) -> unicode: ...

    @overload
    def getToolTipText(self, __a0: java.awt.event.MouseEvent) -> unicode: ...

    def getToolkit(self) -> java.awt.Toolkit: ...

    def getTopLevelAncestor(self) -> java.awt.Container: ...

    def getTransferHandler(self) -> javax.swing.TransferHandler: ...

    def getTransferable(self, __a0: java.awt.Point) -> java.awt.datatransfer.Transferable: ...

    def getTreeLock(self) -> object: ...

    def getUI(self) -> javax.swing.plaf.ComponentUI: ...

    def getUIClassID(self) -> unicode: ...

    def getUpdateSelectionOnSort(self) -> bool: ...

    def getValueAt(self, __a0: int, __a1: int) -> object: ...

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

    def installNavigation(self, __a0: ghidra.app.services.GoToService, __a1: ghidra.app.nav.Navigatable) -> None: ...

    def invalidate(self) -> None: ...

    def isAncestorOf(self, __a0: java.awt.Component) -> bool: ...

    def isBackgroundSet(self) -> bool: ...

    def isCellEditable(self, __a0: int, __a1: int) -> bool: ...

    def isCellSelected(self, __a0: int, __a1: int) -> bool: ...

    def isColumnHeaderPopupEnabled(self) -> bool: ...

    def isColumnSelected(self, __a0: int) -> bool: ...

    def isCursorSet(self) -> bool: ...

    def isDisplayable(self) -> bool: ...

    def isDoubleBuffered(self) -> bool: ...

    def isEditing(self) -> bool: ...

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

    def isMaximumSizeSet(self) -> bool: ...

    def isMinimumSizeSet(self) -> bool: ...

    def isOpaque(self) -> bool: ...

    def isOptimizedDrawingEnabled(self) -> bool: ...

    def isPaintingForPrint(self) -> bool: ...

    def isPaintingTile(self) -> bool: ...

    def isPreferredSizeSet(self) -> bool: ...

    def isRequestFocusEnabled(self) -> bool: ...

    def isRowSelected(self, __a0: int) -> bool: ...

    def isShowing(self) -> bool: ...

    def isStartDragOk(self, __a0: java.awt.dnd.DragGestureEvent) -> bool: ...

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

    @overload
    def move(self) -> None: ...

    @overload
    def move(self, __a0: int, __a1: int) -> None: ...

    def moveColumn(self, __a0: int, __a1: int) -> None: ...

    def navigate(self, __a0: int, __a1: int) -> None: ...

    def nextFocus(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def notifyTableChanged(self, __a0: javax.swing.event.TableModelEvent) -> None: ...

    def paint(self, __a0: java.awt.Graphics) -> None: ...

    def paintAll(self, __a0: java.awt.Graphics) -> None: ...

    def paintComponents(self, __a0: java.awt.Graphics) -> None: ...

    @overload
    def paintImmediately(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def paintImmediately(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def postEvent(self, __a0: java.awt.Event) -> bool: ...

    def prepareEditor(self, __a0: javax.swing.table.TableCellEditor, __a1: int, __a2: int) -> java.awt.Component: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> bool: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> bool: ...

    def prepareRenderer(self, __a0: javax.swing.table.TableCellRenderer, __a1: int, __a2: int) -> java.awt.Component: ...

    @overload
    def print(self) -> bool: ...

    @overload
    def print(self, __a0: java.awt.Graphics) -> None: ...

    @overload
    def print(self, __a0: javax.swing.JTable.PrintMode) -> bool: ...

    @overload
    def print(self, __a0: javax.swing.JTable.PrintMode, __a1: java.text.MessageFormat, __a2: java.text.MessageFormat) -> bool: ...

    @overload
    def print(self, __a0: javax.swing.JTable.PrintMode, __a1: java.text.MessageFormat, __a2: java.text.MessageFormat, __a3: bool, __a4: javax.print.attribute.PrintRequestAttributeSet, __a5: bool) -> bool: ...

    @overload
    def print(self, __a0: javax.swing.JTable.PrintMode, __a1: java.text.MessageFormat, __a2: java.text.MessageFormat, __a3: bool, __a4: javax.print.attribute.PrintRequestAttributeSet, __a5: bool, __a6: javax.print.PrintService) -> bool: ...

    def printAll(self, __a0: java.awt.Graphics) -> None: ...

    def printComponents(self, __a0: java.awt.Graphics) -> None: ...

    def putClientProperty(self, __a0: object, __a1: object) -> None: ...

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

    def removeColumn(self, __a0: javax.swing.table.TableColumn) -> None: ...

    def removeColumnSelectionInterval(self, __a0: int, __a1: int) -> None: ...

    def removeComponentListener(self, __a0: java.awt.event.ComponentListener) -> None: ...

    def removeContainerListener(self, __a0: java.awt.event.ContainerListener) -> None: ...

    def removeEditor(self) -> None: ...

    def removeFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def removeHierarchyBoundsListener(self, __a0: java.awt.event.HierarchyBoundsListener) -> None: ...

    def removeHierarchyListener(self, __a0: java.awt.event.HierarchyListener) -> None: ...

    def removeInputMethodListener(self, __a0: java.awt.event.InputMethodListener) -> None: ...

    def removeKeyListener(self, __a0: java.awt.event.KeyListener) -> None: ...

    def removeMouseListener(self, __a0: java.awt.event.MouseListener) -> None: ...

    def removeMouseMotionListener(self, __a0: java.awt.event.MouseMotionListener) -> None: ...

    def removeMouseWheelListener(self, __a0: java.awt.event.MouseWheelListener) -> None: ...

    def removeNavigation(self) -> None: ...

    def removeNotify(self) -> None: ...

    @overload
    def removePropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    @overload
    def removePropertyChangeListener(self, __a0: unicode, __a1: java.beans.PropertyChangeListener) -> None: ...

    def removeRowSelectionInterval(self, __a0: int, __a1: int) -> None: ...

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

    def rowAtPoint(self, __a0: java.awt.Point) -> int: ...

    def savePreferences(self) -> None: ...

    def scrollRectToVisible(self, __a0: java.awt.Rectangle) -> None: ...

    def scrollToSelectedRow(self) -> None: ...

    def selectAll(self) -> None: ...

    @overload
    def selectRow(self, __a0: int) -> None: ...

    @overload
    def selectRow(self, __a0: java.awt.event.MouseEvent) -> bool: ...

    def setActionMap(self, __a0: javax.swing.ActionMap) -> None: ...

    def setActionsEnabled(self, __a0: bool) -> None: ...

    def setAlignmentX(self, __a0: float) -> None: ...

    def setAlignmentY(self, __a0: float) -> None: ...

    def setAutoCreateColumnsFromModel(self, __a0: bool) -> None: ...

    def setAutoCreateRowSorter(self, __a0: bool) -> None: ...

    def setAutoEditEnabled(self, __a0: bool) -> None: ...

    def setAutoLookupColumn(self, __a0: int) -> None: ...

    def setAutoLookupTimeout(self, __a0: long) -> None: ...

    def setAutoResizeMode(self, __a0: int) -> None: ...

    def setAutoscrolls(self, __a0: bool) -> None: ...

    def setBackground(self, __a0: java.awt.Color) -> None: ...

    def setBorder(self, __a0: javax.swing.border.Border) -> None: ...

    @overload
    def setBounds(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def setBounds(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def setCellEditor(self, __a0: javax.swing.table.TableCellEditor) -> None: ...

    def setCellSelectionEnabled(self, __a0: bool) -> None: ...

    def setColumnHeaderPopupEnabled(self, __a0: bool) -> None: ...

    def setColumnModel(self, __a0: javax.swing.table.TableColumnModel) -> None: ...

    def setColumnSelectionAllowed(self, __a0: bool) -> None: ...

    def setColumnSelectionInterval(self, __a0: int, __a1: int) -> None: ...

    def setComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def setComponentPopupMenu(self, __a0: javax.swing.JPopupMenu) -> None: ...

    def setComponentZOrder(self, __a0: java.awt.Component, __a1: int) -> None: ...

    def setCursor(self, __a0: java.awt.Cursor) -> None: ...

    def setDebugGraphicsOptions(self, __a0: int) -> None: ...

    def setDefaultEditor(self, __a0: java.lang.Class, __a1: javax.swing.table.TableCellEditor) -> None: ...

    @staticmethod
    def setDefaultLocale(__a0: java.util.Locale) -> None: ...

    def setDefaultRenderer(self, __a0: java.lang.Class, __a1: javax.swing.table.TableCellRenderer) -> None: ...

    def setDoubleBuffered(self, __a0: bool) -> None: ...

    def setDragEnabled(self, __a0: bool) -> None: ...

    def setDropMode(self, __a0: javax.swing.DropMode) -> None: ...

    def setDropTarget(self, __a0: java.awt.dnd.DropTarget) -> None: ...

    def setEditingColumn(self, __a0: int) -> None: ...

    def setEditingRow(self, __a0: int) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    def setFillsViewportHeight(self, __a0: bool) -> None: ...

    def setFocusCycleRoot(self, __a0: bool) -> None: ...

    def setFocusTraversalKeys(self, __a0: int, __a1: java.util.Set) -> None: ...

    def setFocusTraversalKeysEnabled(self, __a0: bool) -> None: ...

    def setFocusTraversalPolicy(self, __a0: java.awt.FocusTraversalPolicy) -> None: ...

    def setFocusTraversalPolicyProvider(self, __a0: bool) -> None: ...

    def setFocusable(self, __a0: bool) -> None: ...

    def setFont(self, __a0: java.awt.Font) -> None: ...

    def setForeground(self, __a0: java.awt.Color) -> None: ...

    def setGridColor(self, __a0: java.awt.Color) -> None: ...

    def setHTMLRenderingEnabled(self, __a0: bool) -> None: ...

    def setIgnoreRepaint(self, __a0: bool) -> None: ...

    def setInheritsPopupMenu(self, __a0: bool) -> None: ...

    def setInputMap(self, __a0: int, __a1: javax.swing.InputMap) -> None: ...

    def setInputVerifier(self, __a0: javax.swing.InputVerifier) -> None: ...

    def setIntercellSpacing(self, __a0: java.awt.Dimension) -> None: ...

    def setLayout(self, __a0: java.awt.LayoutManager) -> None: ...

    def setLocale(self, __a0: java.util.Locale) -> None: ...

    @overload
    def setLocation(self, __a0: java.awt.Point) -> None: ...

    @overload
    def setLocation(self, __a0: int, __a1: int) -> None: ...

    def setMaximumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMinimumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMixingCutoutShape(self, __a0: java.awt.Shape) -> None: ...

    def setModel(self, __a0: javax.swing.table.TableModel) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setNavigateOnSelectionEnabled(self, __a0: bool) -> None: ...

    def setNextFocusableComponent(self, __a0: java.awt.Component) -> None: ...

    def setOpaque(self, __a0: bool) -> None: ...

    def setPreferenceKey(self, __a0: unicode) -> None: ...

    def setPreferredScrollableViewportSize(self, __a0: java.awt.Dimension) -> None: ...

    def setPreferredSize(self, __a0: java.awt.Dimension) -> None: ...

    def setRequestFocusEnabled(self, __a0: bool) -> None: ...

    @overload
    def setRowHeight(self, __a0: int) -> None: ...

    @overload
    def setRowHeight(self, __a0: int, __a1: int) -> None: ...

    def setRowMargin(self, __a0: int) -> None: ...

    def setRowSelectionAllowed(self, __a0: bool) -> None: ...

    def setRowSelectionInterval(self, __a0: int, __a1: int) -> None: ...

    def setRowSorter(self, __a0: javax.swing.RowSorter) -> None: ...

    def setSelectionBackground(self, __a0: java.awt.Color) -> None: ...

    def setSelectionForeground(self, __a0: java.awt.Color) -> None: ...

    def setSelectionMode(self, __a0: int) -> None: ...

    def setSelectionModel(self, __a0: javax.swing.ListSelectionModel) -> None: ...

    def setShowGrid(self, __a0: bool) -> None: ...

    def setShowHorizontalLines(self, __a0: bool) -> None: ...

    def setShowVerticalLines(self, __a0: bool) -> None: ...

    @overload
    def setSize(self, __a0: java.awt.Dimension) -> None: ...

    @overload
    def setSize(self, __a0: int, __a1: int) -> None: ...

    def setSurrendersFocusOnKeystroke(self, __a0: bool) -> None: ...

    def setTableHeader(self, __a0: javax.swing.table.JTableHeader) -> None: ...

    def setToolTipText(self, __a0: unicode) -> None: ...

    def setTransferHandler(self, __a0: javax.swing.TransferHandler) -> None: ...

    def setUI(self, __a0: javax.swing.plaf.TableUI) -> None: ...

    def setUpdateSelectionOnSort(self, __a0: bool) -> None: ...

    def setUserSortingEnabled(self, __a0: bool) -> None: ...

    def setValueAt(self, __a0: object, __a1: int, __a2: int) -> None: ...

    def setVerifyInputWhenFocusTarget(self, __a0: bool) -> None: ...

    def setVisible(self, __a0: bool) -> None: ...

    def setVisibleRowCount(self, __a0: int) -> None: ...

    @overload
    def show(self) -> None: ...

    @overload
    def show(self, __a0: bool) -> None: ...

    @overload
    def sizeColumnsToFit(self, __a0: int) -> None: ...

    @overload
    def sizeColumnsToFit(self, __a0: bool) -> None: ...

    def sorterChanged(self, __a0: javax.swing.event.RowSorterEvent) -> None: ...

    def tableChanged(self, __a0: javax.swing.event.TableModelEvent) -> None: ...

    def toString(self) -> unicode: ...

    def transferFocus(self) -> None: ...

    def transferFocusBackward(self) -> None: ...

    def transferFocusDownCycle(self) -> None: ...

    def transferFocusUpCycle(self) -> None: ...

    def unregisterKeyboardAction(self, __a0: javax.swing.KeyStroke) -> None: ...

    def update(self, __a0: java.awt.Graphics) -> None: ...

    def updateUI(self) -> None: ...

    def validate(self) -> None: ...

    def valueChanged(self, __a0: javax.swing.event.ListSelectionEvent) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dragAction(self) -> int: ...

    @property
    def dragSourceListener(self) -> java.awt.dnd.DragSourceListener: ...
