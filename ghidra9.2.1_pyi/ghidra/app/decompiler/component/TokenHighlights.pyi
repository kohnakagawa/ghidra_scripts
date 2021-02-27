from typing import Iterator
import ghidra.app.decompiler
import ghidra.app.decompiler.component
import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function


class TokenHighlights(object, java.lang.Iterable):
    """
    A simple class to manage HighlightTokens used to create highlights in the Decompiler.
     This class allows clients to access highlights either by a ClangToken or a
     HighlightToken.
    """





    def __init__(self): ...

    def __iter__(self): ...

    def add(self, t: ghidra.app.decompiler.component.HighlightToken) -> None:
        """
        Adds the given highlight to this container
        @param t the highlight
        """
        ...

    def clear(self) -> None:
        """
        Removes all highlights from this container
        """
        ...

    def contains(self, t: ghidra.app.decompiler.ClangToken) -> bool:
        """
        Returns true if this class has a highlight for the given token
        @param t the token
        @return true if this class has a highlight for the given token
        """
        ...

    def copyHighlightsByName(self) -> java.util.Map: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def get(self, t: ghidra.app.decompiler.ClangToken) -> ghidra.app.decompiler.component.HighlightToken:
        """
        Gets the current highlight for the given token
        @param t the token
        @return the highlight
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getHighlightsByFunction(self, f: ghidra.program.model.listing.Function) -> java.util.Set:
        """
        Returns all highlights for the given function
        @param f the function
        @return the highlights
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if there are not highlights
        @return true if there are not highlights
        """
        ...

    def iterator(self) -> Iterator[ghidra.app.decompiler.component.HighlightToken]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, t: ghidra.app.decompiler.ClangToken) -> None:
        """
        Removes the highlight for the given token
        @param t the token
        """
        ...

    def removeHighlightsByFunction(self, function: ghidra.program.model.listing.Function) -> java.util.Set:
        """
        Removes all highlights associated with the given function
        @param function the function
        @return the removed highlights; empty if no highlights existed
        """
        ...

    def size(self) -> int:
        """
        Returns the number of highlights
        @return the number of highlights
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...
