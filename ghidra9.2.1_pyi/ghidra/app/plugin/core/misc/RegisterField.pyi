from typing import List
import java.awt
import java.awt.dnd
import java.awt.event
import java.awt.geom
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
import javax.swing.text


class RegisterField(javax.swing.JTextField):




    @overload
    def __init__(self, __a0: int, __a1: long): ...

    @overload
    def __init__(self, __a0: int, __a1: long, __a2: bool): ...



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

    def addActionListener(self, __a0: java.awt.event.ActionListener) -> None: ...

    def addAncestorListener(self, __a0: javax.swing.event.AncestorListener) -> None: ...

    def addCaretListener(self, __a0: javax.swing.event.CaretListener) -> None: ...

    def addComponentListener(self, __a0: java.awt.event.ComponentListener) -> None: ...

    def addContainerListener(self, __a0: java.awt.event.ContainerListener) -> None: ...

    def addFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def addHierarchyBoundsListener(self, __a0: java.awt.event.HierarchyBoundsListener) -> None: ...

    def addHierarchyListener(self, __a0: java.awt.event.HierarchyListener) -> None: ...

    def addInputMethodListener(self, __a0: java.awt.event.InputMethodListener) -> None: ...

    def addKeyListener(self, __a0: java.awt.event.KeyListener) -> None: ...

    @staticmethod
    def addKeymap(__a0: unicode, __a1: javax.swing.text.Keymap) -> javax.swing.text.Keymap: ...

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

    def copy(self) -> None: ...

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

    def cut(self) -> None: ...

    def deliverEvent(self, __a0: java.awt.Event) -> None: ...

    def disable(self) -> None: ...

    def dispatchEvent(self, __a0: java.awt.AWTEvent) -> None: ...

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

    def getAccessibleContext(self) -> javax.accessibility.AccessibleContext: ...

    def getAction(self) -> javax.swing.Action: ...

    def getActionForKeyStroke(self, __a0: javax.swing.KeyStroke) -> java.awt.event.ActionListener: ...

    def getActionListeners(self) -> List[java.awt.event.ActionListener]: ...

    def getActionMap(self) -> javax.swing.ActionMap: ...

    def getActions(self) -> List[javax.swing.Action]: ...

    def getAlignmentX(self) -> float: ...

    def getAlignmentY(self) -> float: ...

    def getAncestorListeners(self) -> List[javax.swing.event.AncestorListener]: ...

    def getAutoscrolls(self) -> bool: ...

    def getBackground(self) -> java.awt.Color: ...

    def getBaseline(self, __a0: int, __a1: int) -> int: ...

    def getBaselineResizeBehavior(self) -> java.awt.Component.BaselineResizeBehavior: ...

    def getBitSize(self) -> int: ...

    def getBorder(self) -> javax.swing.border.Border: ...

    @overload
    def getBounds(self) -> java.awt.Rectangle: ...

    @overload
    def getBounds(self, __a0: java.awt.Rectangle) -> java.awt.Rectangle: ...

    def getCaret(self) -> javax.swing.text.Caret: ...

    def getCaretColor(self) -> java.awt.Color: ...

    def getCaretListeners(self) -> List[javax.swing.event.CaretListener]: ...

    def getCaretPosition(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getClientProperty(self, __a0: object) -> object: ...

    def getColorModel(self) -> java.awt.image.ColorModel: ...

    def getColumns(self) -> int: ...

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

    def getDisabledTextColor(self) -> java.awt.Color: ...

    def getDocument(self) -> javax.swing.text.Document: ...

    def getDragEnabled(self) -> bool: ...

    def getDropLocation(self) -> javax.swing.text.JTextComponent.DropLocation: ...

    def getDropMode(self) -> javax.swing.DropMode: ...

    def getDropTarget(self) -> java.awt.dnd.DropTarget: ...

    def getFocusAccelerator(self) -> int: ...

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

    def getHeight(self) -> int: ...

    def getHierarchyBoundsListeners(self) -> List[java.awt.event.HierarchyBoundsListener]: ...

    def getHierarchyListeners(self) -> List[java.awt.event.HierarchyListener]: ...

    def getHighlighter(self) -> javax.swing.text.Highlighter: ...

    def getHorizontalAlignment(self) -> int: ...

    def getHorizontalVisibility(self) -> javax.swing.BoundedRangeModel: ...

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

    @overload
    def getKeymap(self) -> javax.swing.text.Keymap: ...

    @overload
    @staticmethod
    def getKeymap(__a0: unicode) -> javax.swing.text.Keymap: ...

    def getLayout(self) -> java.awt.LayoutManager: ...

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getLocale(self) -> java.util.Locale: ...

    @overload
    def getLocation(self) -> java.awt.Point: ...

    @overload
    def getLocation(self, __a0: java.awt.Point) -> java.awt.Point: ...

    def getLocationOnScreen(self) -> java.awt.Point: ...

    def getMargin(self) -> java.awt.Insets: ...

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

    def getNavigationFilter(self) -> javax.swing.text.NavigationFilter: ...

    def getNextFocusableComponent(self) -> java.awt.Component: ...

    def getParent(self) -> java.awt.Container: ...

    def getPopupLocation(self, __a0: java.awt.event.MouseEvent) -> java.awt.Point: ...

    def getPreferredScrollableViewportSize(self) -> java.awt.Dimension: ...

    def getPreferredSize(self) -> java.awt.Dimension: ...

    def getPrintable(self, __a0: java.text.MessageFormat, __a1: java.text.MessageFormat) -> java.awt.print.Printable: ...

    @overload
    def getPropertyChangeListeners(self) -> List[java.beans.PropertyChangeListener]: ...

    @overload
    def getPropertyChangeListeners(self, __a0: unicode) -> List[java.beans.PropertyChangeListener]: ...

    def getRegisteredKeyStrokes(self) -> List[javax.swing.KeyStroke]: ...

    def getRootPane(self) -> javax.swing.JRootPane: ...

    def getScrollOffset(self) -> int: ...

    def getScrollableBlockIncrement(self, __a0: java.awt.Rectangle, __a1: int, __a2: int) -> int: ...

    def getScrollableTracksViewportHeight(self) -> bool: ...

    def getScrollableTracksViewportWidth(self) -> bool: ...

    def getScrollableUnitIncrement(self, __a0: java.awt.Rectangle, __a1: int, __a2: int) -> int: ...

    def getSelectedText(self) -> unicode: ...

    def getSelectedTextColor(self) -> java.awt.Color: ...

    def getSelectionColor(self) -> java.awt.Color: ...

    def getSelectionEnd(self) -> int: ...

    def getSelectionStart(self) -> int: ...

    @overload
    def getSize(self) -> java.awt.Dimension: ...

    @overload
    def getSize(self, __a0: java.awt.Dimension) -> java.awt.Dimension: ...

    @overload
    def getText(self) -> unicode: ...

    @overload
    def getText(self, __a0: int, __a1: int) -> unicode: ...

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

    def getValue(self) -> long: ...

    def getValueColor(self) -> java.awt.Color: ...

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

    def isEditable(self) -> bool: ...

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

    @staticmethod
    def loadKeymap(__a0: javax.swing.text.Keymap, __a1: List[javax.swing.text.JTextComponent.KeyBinding], __a2: List[javax.swing.Action]) -> None: ...

    def locate(self, __a0: int, __a1: int) -> java.awt.Component: ...

    def location(self) -> java.awt.Point: ...

    def lostFocus(self, __a0: java.awt.Event, __a1: object) -> bool: ...

    @staticmethod
    def main(__a0: List[unicode]) -> None: ...

    def modelToView(self, __a0: int) -> java.awt.Rectangle: ...

    def modelToView2D(self, __a0: int) -> java.awt.geom.Rectangle2D: ...

    def mouseDown(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseDrag(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseEnter(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseExit(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseMove(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def mouseUp(self, __a0: java.awt.Event, __a1: int, __a2: int) -> bool: ...

    def move(self, __a0: int, __a1: int) -> None: ...

    def moveCaretPosition(self, __a0: int) -> None: ...

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

    def paste(self) -> None: ...

    def postActionEvent(self) -> None: ...

    def postEvent(self, __a0: java.awt.Event) -> bool: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: java.awt.image.ImageObserver) -> bool: ...

    @overload
    def prepareImage(self, __a0: java.awt.Image, __a1: int, __a2: int, __a3: java.awt.image.ImageObserver) -> bool: ...

    @overload
    def print(self) -> bool: ...

    @overload
    def print(self, __a0: java.awt.Graphics) -> None: ...

    @overload
    def print(self, __a0: java.text.MessageFormat, __a1: java.text.MessageFormat) -> bool: ...

    @overload
    def print(self, __a0: java.text.MessageFormat, __a1: java.text.MessageFormat, __a2: bool, __a3: javax.print.PrintService, __a4: javax.print.attribute.PrintRequestAttributeSet, __a5: bool) -> bool: ...

    def printAll(self, __a0: java.awt.Graphics) -> None: ...

    def printComponents(self, __a0: java.awt.Graphics) -> None: ...

    def putClientProperty(self, __a0: object, __a1: object) -> None: ...

    def read(self, __a0: java.io.Reader, __a1: object) -> None: ...

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

    def removeActionListener(self, __a0: java.awt.event.ActionListener) -> None: ...

    def removeAll(self) -> None: ...

    def removeAncestorListener(self, __a0: javax.swing.event.AncestorListener) -> None: ...

    def removeCaretListener(self, __a0: javax.swing.event.CaretListener) -> None: ...

    def removeComponentListener(self, __a0: java.awt.event.ComponentListener) -> None: ...

    def removeContainerListener(self, __a0: java.awt.event.ContainerListener) -> None: ...

    def removeFocusListener(self, __a0: java.awt.event.FocusListener) -> None: ...

    def removeHierarchyBoundsListener(self, __a0: java.awt.event.HierarchyBoundsListener) -> None: ...

    def removeHierarchyListener(self, __a0: java.awt.event.HierarchyListener) -> None: ...

    def removeInputMethodListener(self, __a0: java.awt.event.InputMethodListener) -> None: ...

    def removeKeyListener(self, __a0: java.awt.event.KeyListener) -> None: ...

    @staticmethod
    def removeKeymap(__a0: unicode) -> javax.swing.text.Keymap: ...

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

    def replaceSelection(self, __a0: unicode) -> None: ...

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

    def select(self, __a0: int, __a1: int) -> None: ...

    def selectAll(self) -> None: ...

    def setAction(self, __a0: javax.swing.Action) -> None: ...

    def setActionCommand(self, __a0: unicode) -> None: ...

    def setActionMap(self, __a0: javax.swing.ActionMap) -> None: ...

    def setAlignmentX(self, __a0: float) -> None: ...

    def setAlignmentY(self, __a0: float) -> None: ...

    def setAutoscrolls(self, __a0: bool) -> None: ...

    def setBackground(self, __a0: java.awt.Color) -> None: ...

    def setBitSize(self, __a0: int) -> None: ...

    def setBorder(self, __a0: javax.swing.border.Border) -> None: ...

    @overload
    def setBounds(self, __a0: java.awt.Rectangle) -> None: ...

    @overload
    def setBounds(self, __a0: int, __a1: int, __a2: int, __a3: int) -> None: ...

    def setCaret(self, __a0: javax.swing.text.Caret) -> None: ...

    def setCaretColor(self, __a0: java.awt.Color) -> None: ...

    def setCaretPosition(self, __a0: int) -> None: ...

    def setChangeListener(self, __a0: javax.swing.event.ChangeListener) -> None: ...

    def setColumns(self, __a0: int) -> None: ...

    def setComponentOrientation(self, __a0: java.awt.ComponentOrientation) -> None: ...

    def setComponentPopupMenu(self, __a0: javax.swing.JPopupMenu) -> None: ...

    def setComponentZOrder(self, __a0: java.awt.Component, __a1: int) -> None: ...

    def setCursor(self, __a0: java.awt.Cursor) -> None: ...

    def setDebugGraphicsOptions(self, __a0: int) -> None: ...

    @staticmethod
    def setDefaultLocale(__a0: java.util.Locale) -> None: ...

    def setDisabledTextColor(self, __a0: java.awt.Color) -> None: ...

    def setDocument(self, __a0: javax.swing.text.Document) -> None: ...

    def setDoubleBuffered(self, __a0: bool) -> None: ...

    def setDragEnabled(self, __a0: bool) -> None: ...

    def setDropMode(self, __a0: javax.swing.DropMode) -> None: ...

    def setDropTarget(self, __a0: java.awt.dnd.DropTarget) -> None: ...

    def setEditable(self, __a0: bool) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    def setFocusAccelerator(self, __a0: int) -> None: ...

    def setFocusCycleRoot(self, __a0: bool) -> None: ...

    def setFocusTraversalKeys(self, __a0: int, __a1: java.util.Set) -> None: ...

    def setFocusTraversalKeysEnabled(self, __a0: bool) -> None: ...

    def setFocusTraversalPolicy(self, __a0: java.awt.FocusTraversalPolicy) -> None: ...

    def setFocusTraversalPolicyProvider(self, __a0: bool) -> None: ...

    def setFocusable(self, __a0: bool) -> None: ...

    def setFont(self, __a0: java.awt.Font) -> None: ...

    def setForeground(self, __a0: java.awt.Color) -> None: ...

    def setHighlighter(self, __a0: javax.swing.text.Highlighter) -> None: ...

    def setHorizontalAlignment(self, __a0: int) -> None: ...

    def setIgnoreRepaint(self, __a0: bool) -> None: ...

    def setInheritsPopupMenu(self, __a0: bool) -> None: ...

    def setInputMap(self, __a0: int, __a1: javax.swing.InputMap) -> None: ...

    def setInputVerifier(self, __a0: javax.swing.InputVerifier) -> None: ...

    def setKeymap(self, __a0: javax.swing.text.Keymap) -> None: ...

    def setLayout(self, __a0: java.awt.LayoutManager) -> None: ...

    def setLocale(self, __a0: java.util.Locale) -> None: ...

    @overload
    def setLocation(self, __a0: java.awt.Point) -> None: ...

    @overload
    def setLocation(self, __a0: int, __a1: int) -> None: ...

    def setMargin(self, __a0: java.awt.Insets) -> None: ...

    def setMaximumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMinimumSize(self, __a0: java.awt.Dimension) -> None: ...

    def setMixingCutoutShape(self, __a0: java.awt.Shape) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setNavigationFilter(self, __a0: javax.swing.text.NavigationFilter) -> None: ...

    def setNextFocusableComponent(self, __a0: java.awt.Component) -> None: ...

    def setNoValueColor(self, __a0: java.awt.Color) -> None: ...

    def setOpaque(self, __a0: bool) -> None: ...

    def setPreferredSize(self, __a0: java.awt.Dimension) -> None: ...

    def setRequestFocusEnabled(self, __a0: bool) -> None: ...

    def setScrollOffset(self, __a0: int) -> None: ...

    def setSelectedTextColor(self, __a0: java.awt.Color) -> None: ...

    def setSelectionColor(self, __a0: java.awt.Color) -> None: ...

    def setSelectionEnd(self, __a0: int) -> None: ...

    def setSelectionStart(self, __a0: int) -> None: ...

    @overload
    def setSize(self, __a0: java.awt.Dimension) -> None: ...

    @overload
    def setSize(self, __a0: int, __a1: int) -> None: ...

    def setText(self, __a0: unicode) -> None: ...

    def setToolTipText(self, __a0: unicode) -> None: ...

    def setTransferHandler(self, __a0: javax.swing.TransferHandler) -> None: ...

    def setUI(self, __a0: javax.swing.plaf.TextUI) -> None: ...

    def setValue(self, __a0: long) -> None: ...

    def setValueColor(self, __a0: java.awt.Color) -> None: ...

    def setVerifyInputWhenFocusTarget(self, __a0: bool) -> None: ...

    def setVisible(self, __a0: bool) -> None: ...

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

    def updateUI(self) -> None: ...

    def validate(self) -> None: ...

    def viewToModel(self, __a0: java.awt.Point) -> int: ...

    def viewToModel2D(self, __a0: java.awt.geom.Point2D) -> int: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, __a0: java.io.Writer) -> None: ...

    @property
    def bitSize(self) -> int: ...

    @bitSize.setter
    def bitSize(self, value: int) -> None: ...

    @property
    def noValueColor(self) -> None: ...  # No getter available.

    @noValueColor.setter
    def noValueColor(self, value: java.awt.Color) -> None: ...

    @property
    def value(self) -> long: ...

    @value.setter
    def value(self, value: long) -> None: ...

    @property
    def valueColor(self) -> java.awt.Color: ...

    @valueColor.setter
    def valueColor(self, value: java.awt.Color) -> None: ...
