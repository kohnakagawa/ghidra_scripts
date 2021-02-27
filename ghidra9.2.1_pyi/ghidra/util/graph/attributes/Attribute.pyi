import ghidra.util.graph
import java.lang


class Attribute(object):
    """
    Base class for attributes -- int, double, or String values -- which can
      be assigned to the members of a KeyIndexableSet, e.g. the vertices or
      edges of a DirectedGraph. The attributes do not track changes in the owning
      set, but you can check if the owning set has been modified since creation
      time. It is possible to create an attribute on the vertex set and then
      remove the vertex from the graph. An attempt to get the value associated
      with that vertex will cause a NoValueException to be thrown.
    """





    def __init__(self, name: unicode, set: ghidra.util.graph.KeyIndexableSet):
        """
        Constructor
        @param name name of the attribute
        @param set set whose members may have attribute values defined
        """
        ...



    def attributeType(self) -> unicode:
        """
        Return the type of Attribute, i.e. what kind of values does
         this attribute hold. "Long", "Object", "Double" are examples.
        """
        ...

    def clear(self) -> None:
        """
        Undefine all values set for this attribute.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getModificationNumber(self) -> long:
        """
        Return the current value of the modificationNumber which counts
         the number of changes this Attribute has undergone.
        """
        ...

    def getValueAsString(self, o: ghidra.util.graph.KeyedObject) -> unicode:
        """
        Return the attribute of the specified KeyedObject as a String.
        """
        ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode:
        """
        Return the name of this Attribute.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def owningSet(self) -> ghidra.util.graph.KeyIndexableSet:
        """
        Return the KeyIndexableSet, typically a VertexSet or EdgeSet, that
         this attribute is defined for. An attribute value can only be set
         for a KeyedObject if it is a member of the owningSet.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def modificationNumber(self) -> long: ...
