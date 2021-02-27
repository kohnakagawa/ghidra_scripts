import ghidra.framework.options
import ghidra.graph.viewer
import java.awt
import java.lang


class GraphPerspectiveInfo(object):
    """
    An object that allows for storing and restoring of graph perspective data, like the zoom
     level and the position of the graph.
    """





    @overload
    def __init__(self, saveState: ghidra.framework.options.SaveState): ...

    @overload
    def __init__(self, renderContext: edu.uci.ics.jung.visualization.RenderContext, zoom: float): ...



    @staticmethod
    def createInvalidGraphPerspectiveInfo() -> ghidra.graph.viewer.GraphPerspectiveInfo: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLayoutTranslateCoordinates(self) -> java.awt.Point:
        """
        The offset of the transform from the world origin (which at the time of writing is
         the (0,0) at the upper left-hand corner of the GUI.  This is for the layout transformer.
        """
        ...

    def getViewTranslateCoordinates(self) -> java.awt.Point:
        """
        The offset of the transform from the world origin (which at the time of writing is
         the (0,0) at the upper left-hand corner of the GUI.  This is for the view transformer,
         which also potentially has a scale applied to the transform.
        """
        ...

    def getZoom(self) -> float: ...

    def hashCode(self) -> int: ...

    def isInvalid(self) -> bool: ...

    def isRestoreZoom(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def saveState(self, saveState: ghidra.framework.options.SaveState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def invalid(self) -> bool: ...

    @property
    def layoutTranslateCoordinates(self) -> java.awt.Point: ...

    @property
    def restoreZoom(self) -> bool: ...

    @property
    def viewTranslateCoordinates(self) -> java.awt.Point: ...

    @property
    def zoom(self) -> float: ...
