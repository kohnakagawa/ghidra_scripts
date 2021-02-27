from typing import List
import ghidra.util.graph.attributes
import java.lang


class AttributeManager(object):
    """
    Class which creates and keeps track of attributes defined
     for a single KeyIndexableSet.
    """

    DOUBLE_TYPE: unicode = u'DOUBLE_TYPE'
    INTEGER_TYPE: unicode = u'INTEGER_TYPE'
    LONG_TYPE: unicode = u'LONG_TYPE'
    OBJECT_TYPE: unicode = u'OBJECT_TYPE'
    STRING_TYPE: unicode = u'STRING_TYPE'



    def __init__(self, attributedSet: ghidra.util.graph.KeyIndexableSet):
        """
        Constructor.
        @param attributedSet The KeyIndexableSet whose Attributes this
         AttributeManager manages.
        """
        ...



    def clear(self) -> None:
        """
        Clears all of the attributes managed by this AttributeManager
         while leaving the attributes defined.
        """
        ...

    def createAttribute(self, attributeName: unicode, attributeType: unicode) -> ghidra.util.graph.attributes.Attribute:
        """
        Create a new attribute.
        @param attributeName The name used to identify this Attribute.
        @param attributeType The type of Attribute to construct. Public static
         Strings have been defined for the various choices.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAttribute(self, attributeName: unicode) -> ghidra.util.graph.attributes.Attribute:
        """
        Returns the attribute with the specified name. Returns null
         if there is no attribute with that name.
        """
        ...

    def getAttributeNames(self) -> List[unicode]:
        """
        Returns an array of all names of attributes managed by
         this AttributeManager.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hasAttributeNamed(self, attributeName: unicode) -> bool:
        """
        Returns true if there is an attribute with the specified name managed
         by this attribute manager.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeAttribute(self, attributeName: unicode) -> None:
        """
        Remove the attribute with the specified name from this AttributeManager.
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
    def attributeNames(self) -> List[unicode]: ...
