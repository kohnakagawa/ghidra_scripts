import java.awt
import java.lang


class VertexShapeProvider(object):
    """
    An interface that can be implemented to provide vertex shapes to the UI.  These are used
     for rendering and mouse interaction.  Typically, these shapes are the same.   Clients that
     wish to allow for complicated shapes can use this interface to control mouse hit detection
     while providing simpler shape painting.

     The only time a client would need this separation of shapes is if they create complex
     renderings with odd shapes (a shape that is not a rectangle).   With such a complex
     shape, those graph views that paint only shapes, like the satellite viewer, will look
     peculiar.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompactShape(self) -> java.awt.Shape:
        """
        Returns the compact shape that the user will see when full, detailed rendering is
         not being performed for a vertex, such as in the satellite viewer or when fully-zoomed-out
        @return the shape
        """
        ...

    def getFullShape(self) -> java.awt.Shape:
        """
        Returns the full (the actual) shape of a vertex.  This can be used to determine if a
         mouse point intersects a vertex or to get the real bounding-box of a vertex.
        @return the shape
        """
        ...

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

    @property
    def compactShape(self) -> java.awt.Shape: ...

    @property
    def fullShape(self) -> java.awt.Shape: ...
