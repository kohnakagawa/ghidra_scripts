from typing import List
import java.lang


class CommentTypes(object):
    """
    Class with a convenience method to get an array of the CodeUnit
     comment types. The method is useful to loop through the comment types
     once you have a code unit.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getTypes() -> List[int]:
        """
        Get an array containing the comment types on a code unit.
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
