import ghidra.service.graph
import java.lang
import java.util


class AttributedVertex(ghidra.service.graph.Attributed):
    """
    Graph vertex with attributes
    """





    @overload
    def __init__(self, id: unicode): ...

    @overload
    def __init__(self, id: unicode, name: unicode):
        """
        Constructs a new GhidraVertex with the given id and name
        @param id the unique id for the vertex
        @param name the name for the vertex
        """
        ...



    def clear(self) -> None:
        """
        removes all key/value mappings
        """
        ...

    def clearCache(self) -> None: ...

    def entrySet(self) -> java.util.Set:
        """
        Returns a {@link Set} containing the key/value entry associations
        @return a {@link Set} containing the key/value entry associations
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getAttribute(self, key: unicode) -> unicode:
        """
        gets the value of the given attribute name
        @param key attribute name
        @return the mapped value for the supplied key
        """
        ...

    def getAttributeMap(self) -> java.util.Map:
        """
        Returns an unmodifiable view of the attribute map
        @return an unmodifiable view of the attribute map
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getHtmlString(self) -> unicode:
        """
        parse (one time) then cache the attributes to html
        @return the html string
        """
        ...

    def getId(self) -> unicode:
        """
        Returns the id for this vertex
        @return the id for this vertex
        """
        ...

    def getName(self) -> unicode:
        """
        returns the name of the vertex
        @return the name of the vertex
        """
        ...

    def hasAttribute(self, key: unicode) -> bool:
        """
        Returns true if there is an attribute with that name
        @param key attribute key
        @return true if there is an attribute with that name
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Return true if there are no attributes
        @return true if there are no mapped attributes
        """
        ...

    def keys(self) -> java.util.Set:
        """
        Returns the keys for the attributes
        @return the keys for the attributes
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putAttributes(self, map: java.util.Map) -> None:
        """
        Adds all the key/value pairs from the given map as attributes
        @param map a map of key/values to add as attributes
        """
        ...

    def removeAttribute(self, key: unicode) -> unicode:
        """
        Removes the attribute with the given key
        @param key attribute key
        @return the value of the removed attribute
        """
        ...

    def setAttribute(self, key: unicode, value: unicode) -> unicode:
        """
        Sets the attribute with the given key and value
        @param key attribute key
        @param value attribute value
        @return the previous value of the attribute
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Sets the name on the vertex
        @param name the new name for the vertex
        """
        ...

    def size(self) -> int:
        """
        Returns the number of attributes defined
        @return the number of attributes defined
        """
        ...

    def toString(self) -> unicode: ...

    def values(self) -> java.util.Collection:
        """
        Returns the attribute values
        @return the attribute values
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def htmlString(self) -> unicode: ...

    @property
    def id(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...
