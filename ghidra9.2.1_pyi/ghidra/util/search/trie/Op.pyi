import ghidra.util.search.trie
import java.lang


class Op(object):
    """
    Operation interface for clients to visit nodes in a ByteTrie.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def op(self, node: ghidra.util.search.trie.ByteTrieNodeIfc) -> None:
        """
        Perform an operation on a node.
        @param node the current node
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
