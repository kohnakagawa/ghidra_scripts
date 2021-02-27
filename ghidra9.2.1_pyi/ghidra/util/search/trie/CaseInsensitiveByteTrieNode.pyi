from typing import List
import ghidra.util.search.trie
import java.lang


class CaseInsensitiveByteTrieNode(ghidra.util.search.trie.ByteTrieNode):
    """
    Class to represent a (possibly non-terminal!) node within the CaseInsensitiveByteTrie.
    """









    def equals(self, __a0: object) -> bool: ...

    def getChild(self, value: int) -> ghidra.util.search.trie.ByteTrieNode:
        """
        Returns the child node (successor in the byte sequence) which
         has byte value, or null if no such child exists.
        @param value the byte value
        @return the child node if present or null
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getItem(self) -> object:
        """
        Returns the user item stored in a terminal node (or null in an
         internal node).
        @return the user item
        """
        ...

    def getValue(self) -> List[int]:
        """
        Returns a new byte array with the value of the byte sequence represented
         by this node (slow, built from scratch every time).
        @return the byte sequence
        """
        ...

    def hashCode(self) -> int: ...

    def isTerminal(self) -> bool:
        """
        Returns whether this node represents a byte sequence in the trie
         or just an internal node on our way down to one.
        @return whether this node represents a terminal value
        """
        ...

    def length(self) -> int:
        """
        Returns the length of the byte sequence represented by this node
         (cached integer, very fast).
        @return the length of the byte sequence
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
