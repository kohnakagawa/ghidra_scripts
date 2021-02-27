import ghidra.util.graph
import java.lang


class Vertex(object, ghidra.util.graph.KeyedObject, java.lang.Comparable):
    """
    An implementation of vertices for use in ghidra.util.graph.
    """





    def __init__(self, referent: object):
        """
        Creates a vertex tied to a referent object. The object the key refers
         to can be obtained from the vertex factory using the key of the vertex.
         If there is already a vertex having the same key as returned by
         KeyedObjectFactory.getInstance().getKeyForThisObject( Object o ), then a
         DuplicateKeyException is thrown and no vertex is created.
        """
        ...



    @overload
    def compareTo(self, v: ghidra.util.graph.Vertex) -> int:
        """
        Compares two vertices by keys. If the specified object o is not a Vertex a
         ClassCastException will be thrown.
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, o: object) -> bool:
        """
        @return true iff and only if the given object is a Vertex with the same
         key.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode() Overides hashCode() to use the key of this Vertex.
        """
        ...

    def key(self) -> long:
        """
        @return The key of this vertex.
        """
        ...

    def name(self) -> unicode:
        """
        Return the name of this vertex. If the Vertex has a referent, the
         referent's toString() method will be used to create the name. If
         the Vertex has a null referent, then the key will be used to determine
         the name.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def referent(self) -> object:
        """
        @return The Object this vertex refers to specified at creation time.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
