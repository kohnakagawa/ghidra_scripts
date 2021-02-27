from typing import List
import java.io
import java.lang
import java.util
import org.jdom


class SaveState(object):
    """
    Class for saving values in "serializable safe" way.  Classes that want to be
     able to save their state can do so using the SaveState object.
     The idea is that each state variable in the class
     is first saved into a SaveState object via a String key.  Then the SaveState
     object is written out to an XML element.  When the save state object is
     to be restored, the saveState object is constructed with an XML Element
     that contains all of the name/value pairs. Since the "get" methods require
     a default value, the object that is recovering its state variables
     will be successfully initialized even if
     the given key,value pair is not found in the SaveState object.
      Note: Names for options are assumed to be unique. When a putXXX()
     method is called, if a value already exists for a name, it will
     be overwritten.
    """





    @overload
    def __init__(self):
        """
        Default Constructor for SaveState; uses "SAVE_STATE" as the
         name of the state.
        @see java.lang.Object#Object()
        """
        ...

    @overload
    def __init__(self, name: unicode):
        """
        Creates a new saveState object.
        @param name of the state
        """
        ...

    @overload
    def __init__(self, file: java.io.File):
        """
        Construct a SaveState from a file containing XML from a previously saved SaveState.
        @param file the file containing the XML to read.
        @throws IOException if the file can't be read or is not formatted properly for a SaveState
        """
        ...

    @overload
    def __init__(self, root: org.jdom.Element):
        """
        Construct a new SaveState object using the given XML element.
        @param root XML contents of the save state
        """
        ...



    def clear(self) -> None:
        """
        Clear all objects from the save state.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBoolean(self, name: unicode, defaultValue: bool) -> bool:
        """
        Gets the boolean value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the boolean value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getBooleans(self, name: unicode, defaultValue: List[bool]) -> List[bool]:
        """
        Gets the boolean array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the boolean array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getByte(self, name: unicode, defaultValue: int) -> int:
        """
        Gets the byte value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the byte value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getBytes(self, name: unicode, defaultValue: List[int]) -> List[int]:
        """
        Gets the byte array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the byte array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDouble(self, name: unicode, defaultValue: float) -> float:
        """
        Gets the double value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the double value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getDoubles(self, name: unicode, defaultValue: List[float]) -> List[float]:
        """
        Gets the double array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the double array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getEnum(self, __a0: unicode, __a1: java.lang.Enum) -> java.lang.Enum: ...

    def getFloat(self, name: unicode, defaultValue: float) -> float:
        """
        Gets the float value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the float value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getFloats(self, name: unicode, defaultValue: List[float]) -> List[float]:
        """
        Gets the float array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the float array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getInt(self, name: unicode, defaultValue: int) -> int:
        """
        Gets the int value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the int value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getInts(self, name: unicode, defaultValue: List[int]) -> List[int]:
        """
        Gets the int array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the int array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getLong(self, name: unicode, defaultValue: long) -> long:
        """
        Gets the long value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the long value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getLongs(self, name: unicode, defaultValue: List[long]) -> List[long]:
        """
        Gets the long array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the long array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getNames(self) -> List[unicode]:
        """
        Return the names of the objects saved in the state.
        @return String[] array will be zero length if the save state
         is empty
        """
        ...

    def getShort(self, name: unicode, defaultValue: int) -> int:
        """
        Gets the short value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the short value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getShorts(self, name: unicode, defaultValue: List[int]) -> List[int]:
        """
        Gets the short array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the short array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getString(self, name: unicode, defaultValue: unicode) -> unicode:
        """
        Gets the String value for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the String value associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getStrings(self, name: unicode, defaultValue: List[unicode]) -> List[unicode]:
        """
        Gets the String array for the given name.
        @param name the name of the pair.
        @param defaultValue the default value to be returned if the name does
         not exist in the map, or it does not contain the proper object type.
        @return the String array associated with the given name or the defaultValue
         passed in if the name doesn't exist or is the wrong type.
        """
        ...

    def getXmlElement(self, name: unicode) -> org.jdom.Element:
        """
        Returns the root of an XML sub-tree associated with the
         given name.
        @param name The name associated with the desired Element.
        @return The root of an XML sub-tree associated with the
         given name.
        """
        ...

    def hasValue(self, name: unicode) -> bool:
        """
        Returns true if the SaveState object has a value for the given name.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Return whether anything was added to this save state.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putBoolean(self, name: unicode, value: bool) -> None:
        """
        Associates a boolean value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putBooleans(self, name: unicode, value: List[bool]) -> None:
        """
        Associates a boolean array with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putByte(self, name: unicode, value: int) -> None:
        """
        Associates a byte value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putBytes(self, name: unicode, value: List[int]) -> None:
        """
        Associates a byte array with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putDouble(self, name: unicode, value: float) -> None:
        """
        Associates a double value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putDoubles(self, name: unicode, value: List[float]) -> None:
        """
        Associates a double value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putEnum(self, name: unicode, value: java.lang.Enum) -> None:
        """
        Associates an Enum with the given name.
        @param name The name in the name,value pair.
        @param value The Enum value in the name,value pair.
        """
        ...

    def putFloat(self, name: unicode, value: float) -> None:
        """
        Associates a float value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putFloats(self, name: unicode, value: List[float]) -> None:
        """
        Associates a float array with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putInt(self, name: unicode, value: int) -> None:
        """
        Associates an integer value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putInts(self, name: unicode, value: List[int]) -> None:
        """
        Associates an integer array with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putLong(self, name: unicode, value: long) -> None:
        """
        Associates a long value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putLongs(self, name: unicode, value: List[long]) -> None:
        """
        Associates a long array with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putShort(self, name: unicode, value: int) -> None:
        """
        Associates a short value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putShorts(self, name: unicode, value: List[int]) -> None:
        """
        Associates a short array with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putString(self, name: unicode, value: unicode) -> None:
        """
        Associates a String value with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putStrings(self, name: unicode, value: List[unicode]) -> None:
        """
        Associates a String array with the given name.
        @param name The name in the name,value pair.
        @param value The value in the name,value pair.
        """
        ...

    def putXmlElement(self, name: unicode, element: org.jdom.Element) -> None:
        """
        Adds an XML element to the
         saved state object. Used by plugins that have more
         complicated state information that needs to be saved.
        @param name the name to associate with the element
        @param element XML element which is the root of an
         XML sub-tree.
        """
        ...

    def remove(self, name: unicode) -> None:
        """
        Remove the object identified by the given name.
        """
        ...

    def saveToFile(self, file: java.io.File) -> None:
        """
        Write the saveState to a file as XML
        @param file the file to write to.
        @throws FileNotFoundException if the file does not represent a valid file path.
        @throws IOException if the file could not be written
        """
        ...

    @overload
    def saveToXml(self) -> org.jdom.Element:
        """
        Save this object to an XML element.
        @return Element XML element containing the state
        """
        ...

    @overload
    def saveToXml(self, restrictedSet: java.util.Set) -> org.jdom.Element:
        """
        Save this object to an XML element.
         Restrict child elements to the set specified.
        @param restrictedSet restricted set of element names or null for all names
        @return Element XML element containing the state
        """
        ...

    def size(self) -> int:
        """
        Return the number of objects in the save state.
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
    def empty(self) -> bool: ...

    @property
    def names(self) -> List[unicode]: ...
