import ghidra.util.search.trie
import java.lang


class SearchResult(object):
    """
    A search result container class used with ByteTrie.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getItem(self) -> object:
        """
        Returns the user item stored in this terminal node at add time.
        @return the user item
        """
        ...

    def getNode(self) -> ghidra.util.search.trie.ByteTrieNodeIfc:
        """
        Returns the (terminal) node that was encountered in the search
        @return the node
        """
        ...

    def getPosition(self) -> P:
        """
        Returns the position at which the byte sequence was found.  Currently
         ByteTrie will use Integer for search byte arrays, and Address
         for searching Memory in a Program.
        @return the position at which the byte sequence was found
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
    def item(self) -> object: ...

    @property
    def node(self) -> ghidra.util.search.trie.ByteTrieNodeIfc: ...

    @property
    def position(self) -> object: ...
