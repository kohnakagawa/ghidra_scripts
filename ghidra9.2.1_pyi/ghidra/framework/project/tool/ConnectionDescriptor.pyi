import java.io
import java.lang


class ConnectionDescriptor(object, java.io.Serializable):
    """
    Class to describe the connection between two tools for a specific event.
     This class is used by the ToolSetImpl when it serializes itself.
    """









    def equals(self, obj: object) -> bool:
        """
        Indicates whether some other object is "equal to" this one.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int:
        """
        Returns a hash code value for the object. This method is
         supported for the benefit of hashtables such as those provided by
         <code>java.util.Hashtable</code>.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        Returns a string representation of the object. In general, the
         <code>toString</code> method returns a string that
         "textually represents" this object. The result should
         be a concise but informative representation that is easy for a
         person to read.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
