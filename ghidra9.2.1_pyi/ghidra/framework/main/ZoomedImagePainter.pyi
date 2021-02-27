import ghidra.util.bean
import java.awt
import java.lang
import javax.swing


class ZoomedImagePainter(object, ghidra.util.bean.GGlassPanePainter):
    """
    A class that paints a given image with varying zoom levels.  The zoom is set by clients
     according to changes made by an org.jdesktop.animation.timing.Animator.  In essence,
     this class paints the given image centered over the given target bounds at some
     level of zoom.  If the zoom or bounds of the parent container are never changed,
     then the image painted by this class will not change.

     NOTE: This class and it's getters/setters need to be public for reflective callbacks
    """





    def __init__(self, targetBounds: java.awt.Rectangle, image: java.awt.Image): ...



    @staticmethod
    def createIconImage(icon: javax.swing.Icon) -> java.awt.Image: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTargetBounds(self) -> java.awt.Rectangle: ...

    def getZoom(self) -> float: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paint(self, glassPane: ghidra.util.bean.GGlassPane, g: java.awt.Graphics) -> None: ...

    def setMagnifyFactor(self, factor: float) -> None: ...

    def setTargetBounds(self, containerBounds: java.awt.Rectangle) -> None: ...

    def setZoom(self, zoom: float) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def magnifyFactor(self) -> None: ...  # No getter available.

    @magnifyFactor.setter
    def magnifyFactor(self, value: float) -> None: ...

    @property
    def targetBounds(self) -> java.awt.Rectangle: ...

    @targetBounds.setter
    def targetBounds(self, value: java.awt.Rectangle) -> None: ...

    @property
    def zoom(self) -> float: ...

    @zoom.setter
    def zoom(self, value: float) -> None: ...
