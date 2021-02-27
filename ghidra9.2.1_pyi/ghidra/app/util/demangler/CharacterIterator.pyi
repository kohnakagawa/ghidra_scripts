import java.lang


class CharacterIterator(object):
    """
    A class for bidirectional iteration over a string.

     Iterators maintain a current character index, whose valid range is from
     0 to string.length()-1.

     The current index can be retrieved by calling getIndex() and set directly
     by calling setIndex().

     The methods previous() and next() are used for iteration. They return DONE if
     they would move outside the range from 0 to string.length()-1.
    """

    DONE: int



    def __init__(self, str: unicode):
        """
        Constructs a new character iterator using str.
        @param str the string to iterate
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def find(self, c: int) -> int:
        """
        Looks for the next occurrence of 'c' starting
         at the current index. Returns the character
         position in the underlying string or -1 if 'c'
         is not found.
        """
        ...

    def getAndIncrement(self) -> int:
        """
        Returns the character at the current index and then increments the index by one.
         If the resulting index is greater or equal
         to the end index, the current index is reset to the end index and
         a value of DONE is returned.
        @return the character at the new position or DONE
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getIndex(self) -> int:
        """
        Returns the current index.
        @return the current index.
        """
        ...

    def getLength(self) -> int:
        """
        Returns the length of the iterator.
        @return the length of the iterator
        """
        ...

    def getString(self) -> unicode:
        """
        Returns the underlying string.
        @return the underlying string
        """
        ...

    def hasNext(self) -> bool:
        """
        Returns true if there are more characters to read.
        @return true if there are more characters to read
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> int:
        """
        Increments the current index by one and returns the character
         at the new index.  If the resulting index is greater or equal
         to the end index, the current index is reset to the end index and
         a value of DONE is returned.
        @return the character at the new position or DONE
        """
        ...

    def nextInteger(self) -> int:
        """
        Returns the next integer. The radix must be 10 (decimal).
         For example, given "...12fred..". If current index is pointing
         to the '1', then this value will return 12.
        @return the next base-10 integer.
        """
        ...

    def nextString(self, len: int) -> unicode:
        """
        Returns the next ascii string of the specified length starting
         at the current index.
        @param len the length of the string to read
        @return the next ascii string
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def peek(self) -> int:
        """
        Returns the next character without incrementing the current index.
        @return the next character without incrementing the current index
        """
        ...

    @overload
    def peek(self, lookAhead: int) -> int:
        """
        Peeks at the character current index + lookAhead.
         Returns DONE if the computed position is out of range.
        @param lookAhead number of characters to look ahead
        @return the character at index+lookAhead
        """
        ...

    def previous(self) -> int:
        """
        Decrements the current index by one and returns the character
         at the new index. If the current index is 0, the index
         remains at 0 and a value of DONE is returned.
        @return the character at the new position or DONE
        """
        ...

    def setIndex(self, index: int) -> None:
        """
        Sets the position to the specified position in the text.
        @param index the position within the text.
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
    def andIncrement(self) -> int: ...

    @property
    def index(self) -> int: ...

    @index.setter
    def index(self, value: int) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def string(self) -> unicode: ...
