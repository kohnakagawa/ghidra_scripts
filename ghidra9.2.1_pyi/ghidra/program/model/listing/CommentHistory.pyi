import ghidra.program.model.address
import java.lang
import java.util


class CommentHistory(object):
    """
    Container class for information about changes to a comment.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, commentType: int, userName: unicode, comments: unicode, modificationDate: java.util.Date):
        """
        Constructs a new CommentHistory object
        @param addr the address of the comment
        @param commentType the type of comment
        @param userName the name of the user that changed the comment
        @param comments the list of comments.
        @param modificationDate the date the comment was changed.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get address for this label history object
        @return address for this label history object.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCommentType(self) -> int:
        """
        Get the comment type
        @return the comment type
        """
        ...

    def getComments(self) -> unicode:
        """
        Get the comments for this history object
        @return the comments for this history object
        """
        ...

    def getModificationDate(self) -> java.util.Date:
        """
        Get the modification date
        @return the modification date
        """
        ...

    def getUserName(self) -> unicode:
        """
        Get the user that made the change
        @return the user that made the change
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def commentType(self) -> int: ...

    @property
    def comments(self) -> unicode: ...

    @property
    def modificationDate(self) -> java.util.Date: ...

    @property
    def userName(self) -> unicode: ...
