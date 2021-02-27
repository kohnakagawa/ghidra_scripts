import edu.uci.ics.jung.visualization
import edu.uci.ics.jung.visualization.control
import java.awt.geom
import java.lang


class VisualGraphScalingControl(object, edu.uci.ics.jung.visualization.control.ScalingControl):
    """
    An implementation of ScalingControl that allows us to zoom in and out of the view.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def scale(self, vv: edu.uci.ics.jung.visualization.VisualizationServer, amount: float, at: java.awt.geom.Point2D) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
