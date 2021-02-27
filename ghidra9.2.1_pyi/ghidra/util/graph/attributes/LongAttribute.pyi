from typing import List
import ghidra.util.graph
import ghidra.util.graph.attributes
import java.lang


class LongAttribute(ghidra.util.graph.attributes.Attribute):
    """
    This class provides a storage mechanism for long-valued information about
      the elements of a KeyIndexableSet, e.g. the vertices of a DirectedGraph.
    """





    def __init__(self, name: unicode, set: ghidra.util.graph.KeyIndexableSet):
        """
        Constructor.
        @param name The name used to identify this attribute.
        @param set The KeyIndexableSet whose elements can be assigned
         a value within this attribute.
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
        Removes all assigned values of this attribute.
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

    def getValue(self, o: ghidra.util.graph.KeyedObject) -> long:
        """
        Return the value associated to the specified KeyedObject.
        @throws NoValueException if the value has not been set or
         the KeyedObject does not belong to the owningSet.
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

    def setValue(self, o: ghidra.util.graph.KeyedObject, value: long) -> None:
        """
        Set the value of this attribute for the specified KeyedObject.
        @param o The KeyedObject that is assigned the value. Should
         be a member of the owningSet.
        @param value The value to associate with the specified KeyedObject.
        """
        ...

    @overload
    def toSortedArray(self) -> List[ghidra.util.graph.KeyedObject]:
        """
        Returns the elements of the owningSet sorted by their
         values of this Attribute.
        """
        ...

    @overload
    def toSortedArray(self, keyedObjects: List[ghidra.util.graph.KeyedObject]) -> List[ghidra.util.graph.KeyedObject]:
        """
        Sorts the array of keyedObjects by their values of this
         Attribute.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
