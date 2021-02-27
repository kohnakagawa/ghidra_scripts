from typing import Iterator
import java.lang
import java.util
import java.util.function
import java.util.stream


class Stack(object, java.lang.Iterable):
    """

     The Stack class represents a last-in-first-out (LIFO) stack of objects.
     It extends class ArrayList with five operations that allow an array list
     to be treated as a stack. The usual push and pop operations are provided,
     as well as a method to peek at the top item on the stack, a
     method to test for whether the stack is empty, and a method to search
     the stack for an item and discover how far it is from the top.


     When a stack is first created, it contains no items.


     Note: This implementation is not synchronized!

    """





    @overload
    def __init__(self):
        """
        Creates an empty Stack.
        """
        ...

    @overload
    def __init__(self, initialCapacity: int):
        """
        Creates an empty Stack with specified capacity.
        @param initialCapacity the initial capacity.
        """
        ...

    @overload
    def __init__(self, stack: ghidra.util.datastruct.Stack):
        """
        Copy Constructor.
         Creates a new stack using the items of the given stack.
         Only a shallow copy is performed.
        @param stack the stack to copy
        """
        ...

    def __iter__(self): ...

    def add(self, __a0: object) -> None: ...

    def clear(self) -> None:
        """
        Clears the stack. All items will be removed.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def get(self, depth: int) -> E:
        """
        Returns the element at the specified depth in this stack.
         0 indicates the bottom of the stack.
         size()-1 indicates the top of the stack.
        @param depth the depth in the stack.
        @return the element at the specified depth in this stack
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Tests if this stack is empty.
        """
        ...

    def iterator(self) -> Iterator[E]:
        """
        Returns an iterator over the items of the stack.
         The iterator starts from the bottom of the stack.
        @return an iterator over the items of the stack
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def peek(self) -> E:
        """
        Looks at the object at the top of this stack without removing it from the stack.
        """
        ...

    def pop(self) -> E:
        """
        Removes the object at the top of this stack and returns that object as the value of this function.
        """
        ...

    def push(self, __a0: object) -> object: ...

    def search(self, __a0: object) -> int: ...

    def size(self) -> int:
        """
        Returns the number of elements in this stack.
        @return the number of elements in this stack
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream:
        """
        Returns a stream over this collection.
        @return a stream over this collection.
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
