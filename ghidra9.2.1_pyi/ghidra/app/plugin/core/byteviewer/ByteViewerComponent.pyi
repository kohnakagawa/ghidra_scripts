from typing import List
import docking.widgets
import docking.widgets.fieldpanel
import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.listener
import docking.widgets.fieldpanel.support
import docking.widgets.indexedscrollpane
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


class ByteViewerComponent(docking.widgets.fieldpanel.FieldPanel, docking.widgets.fieldpanel.listener.FieldMouseListener, docking.widgets.fieldpanel.listener.FieldLocationListener, docking.widgets.fieldpanel.listener.FieldSelectionListener, docking.widgets.fieldpanel.listener.FieldInputListener):








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

    def addFieldInputListener(self, __a0: docking.widgets.fieldpanel.listener.FieldInputListener) -> None: ...

    def addFieldLocationListener(self, __a0: docking.widgets.fieldpanel.listener.FieldLocationListener) -> None: ...

    def addFieldMouseListener(self, __a0: docking.widgets.fieldpanel.listener.FieldMouseListener) -> None: ...

    def addFieldSelectionListener(self, __a0: docking.widgets.fieldpanel.listener.FieldSelectionListener) -> None: ...

    def addFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def addHierarchyBoundsListener(self, __a0: java.awt.event.HierarchyBoundsListener) -> None: ...

    def addHierarchyListener(self, __a0: java.awt.event.HierarchyListener) -> None: ...

    def addHighlightListener(self, __a0: docking.widgets.fieldpanel.listener.FieldSelectionListener) -> None: ...

    def addIndexScrollListener(self, __a0: docking.widgets.indexedscrollpane.IndexScrollListener) -> None: ...

    def addInputMethodListener(self, __a0: java.awt.event.InputMethodListener) -> None: ...

    def addKeyListener(self, __a0: java.awt.event.KeyListener) -> None: ...

    def addLayoutListener(self, __a0: docking.widgets.fieldpanel.listener.LayoutListener) -> None: ...

    def addMouseListener(self, __a0: java.awt.event.MouseListener) -> None: ...

    def addMouseMotionListener(self, __a0: java.awt.event.MouseMotionListener) -> None: ...

    def addMouseWheelListener(self, __a0: java.awt.event.MouseWheelListener) -> None: ...

    def addNotify(self) -> None: ...

    @overload
    def addPropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    @overload
    def addPropertyChangeListener(self, __a0: unicode, __a1: java.beans.PropertyChangeListener) -> None: ...

    def addVetoableChangeListener(self, __a0: java.beans.VetoableChangeListener) -> None: ...

    def addViewListener(self, __a0: docking.widgets.fieldpanel.listener.ViewListener) -> None: ...

    def applyComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def areFocusTraversalKeysSet(self, __a0: int) -> bool: ...

    def buttonPressed(self, __a0: docking.widgets.fieldpanel.support.FieldLocation, __a1: docking.widgets.fieldpanel.field.Field, __a2: java.awt.event.MouseEvent) -> None: ...

    def center(self, __a0: docking.widgets.fieldpanel.support.FieldLocation) -> None: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> int: ...

    @overload
    def checkImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> int: ...

    def clearHighlight(self) -> None: ...

    def clearSelection(self) -> None: ...

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

    def cursorBottomOfFile(self) -> None: ...

    def cursorDown(self) -> None: ...

    def cursorEnd(self) -> None: ...

    def cursorHome(self) -> None: ...

    def cursorLeft(self) -> None: ...

    def cursorRight(self) -> None: ...

    def cursorTopOfFile(self) -> None: ...

    def cursorUp(self) -> None: ...

    def dataChanged(self, __a0: long, __a1: long) -> None: ...

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

    def enableSelection(self, __a0: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fieldLocationChanged(self, __a0: docking.widgets.fieldpanel.support.FieldLocation, __a1: docking.widgets.fieldpanel.field.Field, __a2: docking.widgets.EventTrigger) -> None: ...

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

    @overload
    def getBackgroundColor(self) -> java.awt.Color: ...

    @overload
    def getBackgroundColor(self, __a0: long) -> java.awt.Color: ...

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

    def getCurrentField(self) -> docking.widgets.fieldpanel.field.Field: ...

    def getCursor(self) -> java.awt.Cursor: ...

    def getCursorBounds(self) -> java.awt.Rectangle: ...

    def getCursorLocation(self) -> docking.widgets.fieldpanel.support.FieldLocation: ...

    def getCursorOffset(self) -> int: ...

    def getCursorPoint(self) -> java.awt.Point: ...

    def getDebugGraphicsOptions(self) -> int: ...

    @staticmethod
    def getDefaultLocale() -> java.util.Locale: ...

    def getDropTarget(self) -> java.awt.dnd.DropTarget: ...

    def getFieldAt(self, __a0: int, __a1: int, __a2: docking.widgets.fieldpanel.support.FieldLocation) -> docking.widgets.fieldpanel.field.Field: ...

    def getFocusCycleRootAncestor(self) -> java.awt.Container: ...

    def getFocusListeners(self) -> List[java.awt.event.FocusListener]: ...

    def getFocusTraversalKeys(self, __a0: int) -> java.util.Set: ...

    def getFocusTraversalKeysEnabled(self) -> bool: ...

    def getFocusTraversalPolicy(self) -> java.awt.FocusTraversalPolicy: ...

    def getFocusedCursorColor(self) -> java.awt.Color: ...

    def getFont(self) -> java.awt.Font: ...

    def getFontMetrics(self, __a0: java.awt.Font) -> java.awt.FontMetrics: ...

    def getForeground(self) -> java.awt.Color: ...

    def getForegroundColor(self) -> java.awt.Color: ...

    def getGraphics(self) -> java.awt.Graphics: ...

    def getGraphicsConfiguration(self) -> java.awt.GraphicsConfiguration: ...

    @overload
    def getHeight(self) -> int: ...

    @overload
    def getHeight(self, __a0: long) -> int: ...

    def getHierarchyBoundsListeners(self) -> List[java.awt.event.HierarchyBoundsListener]: ...

    def getHierarchyListeners(self) -> List[java.awt.event.HierarchyListener]: ...

    def getHighlight(self) -> docking.widgets.fieldpanel.support.FieldSelection: ...

    def getHighlightColor(self) -> java.awt.Color: ...

    def getHoverHandler(self) -> docking.widgets.fieldpanel.HoverHandler: ...

    def getIgnoreRepaint(self) -> bool: ...

    def getIndexAfter(self, __a0: long) -> long: ...

    def getIndexBefore(self, __a0: long) -> long: ...

    def getIndexCount(self) -> long: ...

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

    def getLayoutModel(self) -> docking.widgets.fieldpanel.LayoutModel: ...

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getLocale(self) -> java.util.Locale: ...

    @overload
    def getLocation(self) -> java.awt.Point: ...

    @overload
    def getLocation(self, __a0: java.awt.Point) -> java.awt.Point: ...

    def getLocationForPoint(self, __a0: int, __a1: int) -> docking.widgets.fieldpanel.support.FieldLocation: ...

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

    def getNonFocusCursorColor(self) -> java.awt.Color: ...

    def getOffset(self, __a0: docking.widgets.fieldpanel.support.FieldLocation) -> int: ...

    def getParent(self) -> java.awt.Container: ...

    def getPointForLocation(self, __a0: docking.widgets.fieldpanel.support.FieldLocation) -> java.awt.Point: ...

    def getPopupLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    def getPreferredSize(self) -> java.awt.Dimension: ...

    @overload
    def getPropertyChangeListeners(self) -> List[java.beans.PropertyChangeListener]: ...

    @overload
    def getPropertyChangeListeners(self, __a0: unicode) -> List[java.beans.PropertyChangeListener]: ...

    def getRegisteredKeyStrokes(self) -> List[javax.swing.KeyStroke]: ...

    def getRootPane(self) -> javax.swing.JRootPane: ...

    def getSelection(self) -> docking.widgets.fieldpanel.support.FieldSelection: ...

    def getSelectionColor(self) -> java.awt.Color: ...

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

    def getUI(self) -> javax.swing.plaf.ComponentUI: ...

    def getUIClassID(self) -> unicode: ...

    def getVerifyInputWhenFocusTarget(self) -> bool: ...

    def getVetoableChangeListeners(self) -> List[java.beans.VetoableChangeListener]: ...

    def getViewerPosition(self) -> docking.widgets.fieldpanel.support.ViewerPosition: ...

    def getVisibleEndLayout(self) -> docking.widgets.fieldpanel.support.AnchoredLayout: ...

    def getVisibleLayouts(self) -> List[object]: ...

    def getVisibleRect(self) -> java.awt.Rectangle: ...

    def getVisibleStartLayout(self) -> docking.widgets.fieldpanel.support.AnchoredLayout: ...

    def getWidth(self) -> int: ...

    def getX(self) -> int: ...

    def getY(self) -> int: ...

    def goTo(self, __a0: long, __a1: int, __a2: int, __a3: int, __a4: bool) -> None: ...

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

    def isCursorOn(self) -> bool: ...

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

    def isFocused(self) -> bool: ...

    def isFontSet(self) -> bool: ...

    def isForegroundSet(self) -> bool: ...

    def isLightweight(self) -> bool: ...

    @staticmethod
    def isLightweightComponent(__a0: java.awt.Component) -> bool: ...

    def isLocationVisible(self, __a0: docking.widgets.fieldpanel.support.FieldLocation) -> bool: ...

    def isManagingFocus(self) -> bool: ...

    def isMaximumSizeSet(self) -> bool: ...

    def isMinimumSizeSet(self) -> bool: ...

    def isOpaque(self) -> bool: ...

    def isOptimizedDrawingEnabled(self) -> bool: ...

    def isPaintingForPrint(self) -> bool: ...

    def isPaintingTile(self) -> bool: ...

    def isPreferredSizeSet(self) -> bool: ...

    def isRequestFocusEnabled(self) -> bool: ...

    def isShowing(self) -> bool: ...

    def isStartDragOK(self) -> bool: ...

    def isUniformIndex(self) -> bool: ...

    def isValid(self) -> bool: ...

    def isValidateRoot(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def keyDown(self, __a0: java.awt.Event, __a1: int) -> bool: ...

    def keyPressed(self, __a0: java.awt.event.KeyEvent, __a1: long, __a2: int, __a3: int, __a4: int, __a5: docking.widgets.fieldpanel.field.Field) -> None: ...

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

    def modelSizeChanged(self, __a0: docking.widgets.fieldpanel.listener.IndexMapper) -> None: ...

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

    def pageDown(self) -> None: ...

    def pageUp(self) -> None: ...

    def paint(self, __a0: java.awt.Graphics) -> None: ...

    def paintAll(self, __a0: java.awt.Graphics) -> None: ...

    def paintComponents(self, __a0: java.awt.Graphics) -> None: ...

    @overload
    def paintImmediately(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def paintImmediately(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def positionCursor(self, __a0: int) -> None: ...

    def postEvent(self, __a0: java.awt.Event) -> bool: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> bool: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> bool: ...

    def print(self, __a0: java.awt.Graphics) -> None: ...

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

    def removeComponentListener(self, __a0: java.awt.event.ComponentListener) -> None: ...

    def removeContainerListener(self, __a0: java.awt.event.ContainerListener) -> None: ...

    def removeFieldInputListener(self, __a0: docking.widgets.fieldpanel.listener.FieldInputListener) -> None: ...

    def removeFieldLocationListener(self, __a0: docking.widgets.fieldpanel.listener.FieldLocationListener) -> None: ...

    def removeFieldMouseListener(self, __a0: docking.widgets.fieldpanel.listener.FieldMouseListener) -> None: ...

    def removeFieldSelectionListener(self, __a0: docking.widgets.fieldpanel.listener.FieldSelectionListener) -> None: ...

    def removeFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def removeHierarchyBoundsListener(self, __a0: java.awt.event.HierarchyBoundsListener) -> None: ...

    def removeHierarchyListener(self, __a0: java.awt.event.HierarchyListener) -> None: ...

    def removeHighlightListener(self, __a0: docking.widgets.fieldpanel.listener.FieldSelectionListener) -> None: ...

    def removeIndexScrollListener(self, __a0: docking.widgets.indexedscrollpane.IndexScrollListener) -> None: ...

    def removeInputMethodListener(self, __a0: java.awt.event.InputMethodListener) -> None: ...

    def removeKeyListener(self, __a0: java.awt.event.KeyListener) -> None: ...

    def removeLayoutListener(self, __a0: docking.widgets.fieldpanel.listener.LayoutListener) -> None: ...

    def removeMouseListener(self, __a0: java.awt.event.MouseListener) -> None: ...

    def removeMouseMotionListener(self, __a0: java.awt.event.MouseMotionListener) -> None: ...

    def removeMouseWheelListener(self, __a0: java.awt.event.MouseWheelListener) -> None: ...

    def removeNotify(self) -> None: ...

    @overload
    def removePropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    @overload
    def removePropertyChangeListener(self, __a0: unicode, __a1: java.beans.PropertyChangeListener) -> None: ...

    def removeVetoableChangeListener(self, __a0: java.beans.VetoableChangeListener) -> None: ...

    def removeViewListener(self, __a0: docking.widgets.fieldpanel.listener.ViewListener) -> None: ...

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

    def scrollLineDown(self) -> None: ...

    def scrollLineUp(self) -> None: ...

    def scrollPageDown(self) -> None: ...

    def scrollPageUp(self) -> None: ...

    def scrollRectToVisible(self, __a0: java.awt.Rectangle) -> None: ...

    def scrollTo(self, __a0: docking.widgets.fieldpanel.support.FieldLocation) -> None: ...

    def scrollToCursor(self) -> None: ...

    def scrollView(self, __a0: int) -> None: ...

    def selectionChanged(self, __a0: docking.widgets.fieldpanel.support.FieldSelection, __a1: docking.widgets.EventTrigger) -> None: ...

    def setActionMap(self, __a0: javax.swing.ActionMap) -> None: ...

    def setAlignmentX(self, __a0: float) -> None: ...

    def setAlignmentY(self, __a0: float) -> None: ...

    def setAutoscrolls(self, __a0: bool) -> None: ...

    def setBackground(self, __a0: java.awt.Color) -> None: ...

    def setBackgroundColor(self, __a0: java.awt.Color) -> None: ...

    def setBackgroundColorModel(self, __a0: docking.widgets.fieldpanel.support.BackgroundColorModel) -> None: ...

    def setBlinkCursor(self, __a0: bool) -> None: ...

    def setBorder(self, __a0: javax.swing.border.Border) -> None: ...

    @overload
    def setBounds(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def setBounds(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def setComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def setComponentPopupMenu(self, __a0: javax.swing.JPopupMenu) -> None: ...

    def setComponentZOrder(self, __a0: java.awt.Component, __a1: int) -> None: ...

    def setCursor(self, __a0: java.awt.Cursor) -> None: ...

    def setCursorOn(self, __a0: bool) -> None: ...

    @overload
    def setCursorPosition(self, __a0: long, __a1: int, __a2: int, __a3: int) -> bool: ...

    @overload
    def setCursorPosition(self, __a0: long, __a1: int, __a2: int, __a3: int, __a4: docking.widgets.EventTrigger) -> bool: ...

    def setDebugGraphicsOptions(self, __a0: int) -> None: ...

    @staticmethod
    def setDefaultLocale(__a0: java.util.Locale) -> None: ...

    def setDoubleBuffered(self, __a0: bool) -> None: ...

    def setDropTarget(self, __a0: java.awt.dnd.DropTarget) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    def setFocusCycleRoot(self, __a0: bool) -> None: ...

    def setFocusTraversalKeys(self, __a0: int, __a1: java.util.Set) -> None: ...

    def setFocusTraversalKeysEnabled(self, __a0: bool) -> None: ...

    def setFocusTraversalPolicy(self, __a0: java.awt.FocusTraversalPolicy) -> None: ...

    def setFocusTraversalPolicyProvider(self, __a0: bool) -> None: ...

    def setFocusable(self, __a0: bool) -> None: ...

    def setFocusedCursorColor(self, __a0: java.awt.Color) -> None: ...

    def setFont(self, __a0: java.awt.Font) -> None: ...

    def setForeground(self, __a0: java.awt.Color) -> None: ...

    def setHighlight(self, __a0: docking.widgets.fieldpanel.support.FieldSelection) -> None: ...

    def setHighlightColor(self, __a0: java.awt.Color) -> None: ...

    def setHorizontalScrollingEnabled(self, __a0: bool) -> None: ...

    def setHoverProvider(self, __a0: docking.widgets.fieldpanel.support.HoverProvider) -> None: ...

    def setIgnoreRepaint(self, __a0: bool) -> None: ...

    def setInheritsPopupMenu(self, __a0: bool) -> None: ...

    def setInputMap(self, __a0: int, __a1: javax.swing.InputMap) -> None: ...

    def setInputVerifier(self, __a0: javax.swing.InputVerifier) -> None: ...

    def setLayout(self, __a0: java.awt.LayoutManager) -> None: ...

    def setLayoutModel(self, __a0: docking.widgets.fieldpanel.LayoutModel) -> None: ...

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

    def setNonFocusCursorColor(self, __a0: java.awt.Color) -> None: ...

    def setOpaque(self, __a0: bool) -> None: ...

    def setPreferredSize(self, __a0: java.awt.Dimension) -> None: ...

    def setRequestFocusEnabled(self, __a0: bool) -> None: ...

    def setSelection(self, __a0: docking.widgets.fieldpanel.support.FieldSelection) -> None: ...

    def setSelectionColor(self, __a0: java.awt.Color) -> None: ...

    @overload
    def setSize(self, __a0: java.awt.Dimension) -> None: ...

    @overload
    def setSize(self, __a0: int, __a1: int) -> None: ...

    def setToolTipText(self, __a0: unicode) -> None: ...

    def setTransferHandler(self, __a0: javax.swing.TransferHandler) -> None: ...

    def setUI(self, __a0: javax.swing.plaf.PanelUI) -> None: ...

    def setVerifyInputWhenFocusTarget(self, __a0: bool) -> None: ...

    def setViewerPosition(self, __a0: long, __a1: int, __a2: int) -> None: ...

    def setVisible(self, __a0: bool) -> None: ...

    @overload
    def show(self) -> None: ...

    @overload
    def show(self, __a0: bool) -> None: ...

    def showIndex(self, __a0: long, __a1: int) -> None: ...

    def stateChanged(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

    def takeFocus(self) -> None: ...

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