import java.lang


class FunctionTag(java.lang.Comparable, object):
    """
    Represents a function tag object that can be associated with
     functions. This maps to the
     ghidra.program.database.function.FunctionTagAdapter table.
    """









    def compareTo(self, __a0: object) -> int: ...

    def delete(self) -> None:
        """
        Deletes this tag from the program.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Returns the tag comment.
        @return
        """
        ...

    def getId(self) -> long:
        """
        Returns the id of the item.
        @return
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the tag name.
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None:
        """
        Sets the comment for this tag.
        @param comment the tag comment
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Sets the name of the tag.
        @param name the tag name
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
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def id(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...
