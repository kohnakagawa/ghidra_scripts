import java.lang


class ZoomImageRunner(object):
    """
    A class to change the bounds of a given ZoomedImagePainter to make the Icon appear to
     grow and fade away over time.  This class handles setup for the painter and then makes changes
      on the painter by using callbacks from the Animator.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
