import java.io
import java.lang


class ShortListIndexer(object, java.io.Serializable):
    """
    Class to manage multiple linked lists of short indexes. Users can add indexes
     to a list, remove indexes from a list, remove all indexes from a list, and
     retrieve all indexes within a given list.
    """





    def __init__(self, numLists: int, capacity: int):
        """
        The constructor
        @param numLists - The initial number of lists to be managed.
        @param capacity - The current size of the pool of possible indexes.  All indexes
          begin on the free list.
        """
        ...



    def add(self, listID: int) -> int:
        """
        Allocates a new index resource and adds it to the front of the linked list
         indexed by listID.
        @param listID the id of the list to add to.
        @exception IndexOutOfBoundsException thrown if the listID is not in the
         the range [0, numLists).
        """
        ...

    def append(self, listID: int) -> int:
        """
        Allocates a new index resource and adds it to the end of the linked list
         indexed by listID.
        @param listID the id of the list to add to.
        @exception IndexOutOfBoundsException thrown if the listID is not in the
         the range [0, numLists).
        """
        ...

    def clear(self) -> None:
        """
        Removes all indexes from all lists.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def first(self, listID: int) -> int:
        """
        Returns the first index resource on the linked list indexed by listID.
        @exception IndexOutOfBoundsException thrown if the listID is not in the
         the range [0, numLists].
        """
        ...

    def getCapacity(self) -> int:
        """
        Returns the current index capacity.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getListSize(self, listID: int) -> int:
        """
        Returns the number of indexes in the specified list.
        @exception IndexOutOfBoundsException thrown if the listID is not in the
         the range [0, numLists).
        """
        ...

    def getNewCapacity(self) -> int:
        """
        Computes the next size that should be used to grow the index capacity.
        """
        ...

    def getNumLists(self) -> int:
        """
        Returns the number of linked list being managed.
        """
        ...

    def getSize(self) -> int:
        """
        Returns the current number of used index resources.
        """
        ...

    def growCapacity(self, newCapacity: int) -> None:
        """
        Increases the index resource pool.
        @param newCapacity the new number of resource indexes to manage.  if this number
         is smaller than the current number of resource indexes, then nothing changes.
        """
        ...

    def growNumLists(self, newListSize: int) -> None:
        """
        Increases the number of managed linked lists.
        @param newListSize the new number of linked lists.  If this number is
         smaller than the current number of linked lists, then nothing changes.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self, index: int) -> int:
        """
        Returns the next index resource that follows the given index in a linked list.
         The index should be an index that is in some linked list.  Otherwise, the
         results are undefined( probably give you the next index on the free list )
        @param index to search after to find the next index.
        @exception IndexOutOfBoundsException thrown if the index is not in the
         the range [0, capacity].
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, listID: int, index: int) -> None:
        """
        Remove the index resource from the linked list indexed by listID.
        @param listID the id of the list from which to removed the value at index.
        @param index the index of the value to be removed from the specified list.
        @exception IndexOutOfBoundsException thrown if the listID is not in the
         the range [0, numLists).
        """
        ...

    def removeAll(self, listID: int) -> None:
        """
        Removes all indexes from the specified list.
        @param listID the list to be emptied.
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
    def capacity(self) -> int: ...

    @property
    def newCapacity(self) -> int: ...

    @property
    def numLists(self) -> int: ...

    @property
    def size(self) -> int: ...
