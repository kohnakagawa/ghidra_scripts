import java.lang
import java.util


class GhidraScriptProperties(object):
    """
    Handles processing for .properties files associated with a GhidraScript (.properties file and
     script should share the same basename).

     This should only be called/used by the GhidraScript class.
    """









    def containsKey(self, keyString: unicode) -> bool:
        """
        @param keyString a property name
        @return true if the key exists in the property file
        """
        ...

    def containsValue(self, valueString: unicode) -> bool:
        """
        @param valueString a value string
        @return true if any property has the given value
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFilename(self) -> unicode:
        """
        @return the properties file name
        """
        ...

    def getValue(self, keyString: unicode) -> unicode:
        """
        @param keyString the property name
        @return the value of the key in the properties file, or an empty string if no property exists
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        @return true if there are no properties
        """
        ...

    def keySet(self) -> java.util.Set:
        """
        @return the property names for all properties
        """
        ...

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
    def empty(self) -> bool: ...

    @property
    def filename(self) -> unicode: ...
