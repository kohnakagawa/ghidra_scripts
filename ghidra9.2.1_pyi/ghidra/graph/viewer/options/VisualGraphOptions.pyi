import ghidra.graph.viewer.options
import java.lang


class VisualGraphOptions(object):
    SCROLL_WHEEL_PANS_DESCRIPTION: unicode = u'When enabled the mouse scroll wheel will pan the view vertically.  When not enabled, you must hold the <b>Command</b> key while using the mouse wheel'
    SCROLL_WHEEL_PANS_KEY: unicode = u'Scroll Wheel Pans'
    SHOW_ANIMATION_DESCRIPTION: unicode = u'Signals to the Function Graph to use animated transitions for certain operations, like navigation.'
    SHOW_ANIMATION_OPTIONS_KEY: unicode = u'Use Animation'
    USE_CONDENSED_LAYOUT_DESCRIPTION: unicode = u'Place vertices as close together as possible.  For example, when true, the graph will use little spacing between vertices.  Each layout will handle this option differently.'
    USE_CONDENSED_LAYOUT_KEY: unicode = u'Use Condensed Layout'
    USE_MOUSE_RELATIVE_ZOOM_DESCRIPTION: unicode = u'When true the Function Graph will perform zoom operations relative to the mouse point.'
    USE_MOUSE_RELATIVE_ZOOM_KEY: unicode = u'Use Mouse-relative Zoom'
    USE_STICKY_SELECTION_DESCRIPTION: unicode = u'When enabled Selecting code units in one vertex will not clear the selection in another.  When disabled, every new selection clears the previous selection <b>unless the Control</b>key is pressed.'
    USE_STICKY_SELECTION_KEY: unicode = u'Use Sticky Selection'
    VIEW_RESTORE_OPTIONS_DESCRIPTION: unicode = u'Dictates how the view of new graphs and already rendered graphs are zoomed and positioned.  See the help for more details.'
    VIEW_RESTORE_OPTIONS_KEY: unicode = u'View Settings'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getScrollWheelPans(self) -> bool: ...

    def getViewRestoreOption(self) -> ghidra.graph.viewer.options.ViewRestoreOption: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setUseAnimation(self, useAnimation: bool) -> None: ...

    def toString(self) -> unicode: ...

    def useAnimation(self) -> bool: ...

    def useCondensedLayout(self) -> bool: ...

    def useMouseRelativeZoom(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def scrollWheelPans(self) -> bool: ...

    @property
    def viewRestoreOption(self) -> ghidra.graph.viewer.options.ViewRestoreOption: ...
