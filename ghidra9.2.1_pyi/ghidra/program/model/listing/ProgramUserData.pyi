from typing import List
import ghidra.framework.model
import ghidra.framework.options
import ghidra.program.model.util
import java.lang


class ProgramUserData(ghidra.framework.model.UserData, object):








    def endTransaction(self, transactionID: int) -> None:
        """
        End a previously started transaction
        @param transactionID
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBooleanProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.VoidPropertyMap:
        """
        Get a address-based Boolean property map
        @param owner name of property owner (e.g., plugin name)
        @param propertyName
        @param create creates the property map if it does not exist
        @return property map
        @throws PropertyTypeMismatchException if a conflicting map definition was found
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getIntProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.IntPropertyMap:
        """
        Get a address-based Integer property map
        @param owner name of property owner (e.g., plugin name)
        @param propertyName
        @param create creates the property map if it does not exist
        @return property map
        @throws PropertyTypeMismatchException if a conflicting map definition was found
        """
        ...

    def getLongProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.LongPropertyMap:
        """
        Get a address-based Long property map
        @param owner name of property owner (e.g., plugin name)
        @param propertyName
        @param create creates the property map if it does not exist
        @return property map
        @throws PropertyTypeMismatchException if a conflicting map definition was found
        """
        ...

    def getObjectProperty(self, owner: unicode, propertyName: unicode, saveableObjectClass: java.lang.Class, create: bool) -> ghidra.program.model.util.ObjectPropertyMap:
        """
        Get a address-based Saveable-object property map
        @param owner name of property owner (e.g., plugin name)
        @param propertyName
        @param create creates the property map if it does not exist
        @return property map
        @throws PropertyTypeMismatchException if a conflicting map definition was found
        """
        ...

    def getOptions(self, propertyListName: unicode) -> ghidra.framework.options.Options:
        """
        Get the property list for the given name.
        @param propertyListName name of property list
        """
        ...

    def getOptionsNames(self) -> List[unicode]:
        """
        Returns all properties lists contained by this domain object.
        @return all property lists contained by this domain object.
        """
        ...

    def getProperties(self, owner: unicode) -> List[ghidra.program.model.util.PropertyMap]:
        """
        Get all property maps associated with a specific owner.
        @param owner name of property owner (e.g., plugin name)
        @return list of property maps
        """
        ...

    def getPropertyOwners(self) -> List[unicode]:
        """
        Returns list of all property owners for which property maps have been defined.
        """
        ...

    def getStringProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.StringPropertyMap:
        """
        Get a address-based String property map
        @param owner name of property owner (e.g., plugin name)
        @param propertyName
        @param create creates the property map if it does not exist
        @return property map
        @throws PropertyTypeMismatchException if a conflicting map definition was found
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def startTransaction(self) -> int:
        """
        Start a transaction prior to changing any properties
        @return transaction ID needed for endTransaction
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
    def optionsNames(self) -> List[object]: ...

    @property
    def propertyOwners(self) -> List[object]: ...
