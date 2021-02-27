import ghidra.app.util.viewer.listingpanel
import java.lang


class ProxyObj(object):
    """
    Implementing objects of this interface hold an object from a program (e.g. CodeUnit, Funtion etc.)
     in such a way as to be robust against changes to the program.   In other words, it protects
     against holding on to` "stale" objects.  The getObject() method will return the represented object
     (refreshed if it was stale) or null if it no longer exists.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getListingLayoutModel(self) -> ghidra.app.util.viewer.listingpanel.ListingModel:
        """
        Returns the layout model which corresponds to this field proxy.
        """
        ...

    def getObject(self) -> object:
        """
        Returns the object that this proxy represents or null if the represented object no longer
         exists.
        @return the object that this proxy represents or null if the represented object no longer
         exists.
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
    def listingLayoutModel(self) -> ghidra.app.util.viewer.listingpanel.ListingModel: ...

    @property
    def object(self) -> object: ...
