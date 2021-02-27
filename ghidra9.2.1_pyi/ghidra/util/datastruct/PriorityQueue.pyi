import java.lang


class PriorityQueue(object):
    """
    Maintains a list of objects in priority order where priority is just
     an integer value.  The object with the lowest
     priority number can be retrieved using getFirst() and the object with the highest
     priority number can be retrieved using getLast().
    """





    def __init__(self): ...



    def add(self, obj: object, priority: int) -> None:
        """
        Adds the given object to the queue at the appropriate insertion point based
         on the given priority.
        @param obj the object to be added.
        @param priority the priority assigned to the object.
        """
        ...

    def clear(self) -> None:
        """
        Removes all objects from the queue.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirst(self) -> object:
        """
        Returns the object with the lowest priority number in the queue.
         If more than one object has the same priority, then the object that
         was added to the queue first is considered to have the lower priority value.
         Null is returned if the queue is empty.
        """
        ...

    def getFirstPriority(self) -> int:
        """
        Returns the priority of the object with the lowest priority in the queue.
         Null returned if the queue is empty.
        """
        ...

    def getLast(self) -> object:
        """
        Returns the object with the highest priority number in the queue.
         If more than one object has the same priority, then the object that
         was added to the queue last is considered to have the higher priority value.
         Null is returned if the queue is empty.
        """
        ...

    def getLastPriority(self) -> int:
        """
        Returns the priority of the object with the highest priority in the queue.
         Null returned if the queue is empty.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if the queue is empty.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeFirst(self) -> object:
        """
        Removes and returns the object with the lowest priority number in the queue.
         If more than one object has the same priority, then the object that
         was added to the queue first is considered to have the lower priority value.
         Null is returned if the queue is empty.
        @return the object with the lowest priority number or null if the list is empty.
        """
        ...

    def removeLast(self) -> object:
        """
        Removes and returns the object with the highest priority number in the queue.
         If more than one object has the same priority, then the object that
         was added to the queue last is considered to have the higher priority value.
         Null is returned if the queue is empty.
        @return the object with the highest priority number or null if the list is empty.
        """
        ...

    def size(self) -> int:
        """
        Returns the number of objects in the queue.
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
    def first(self) -> object: ...

    @property
    def firstPriority(self) -> int: ...

    @property
    def last(self) -> object: ...

    @property
    def lastPriority(self) -> int: ...
