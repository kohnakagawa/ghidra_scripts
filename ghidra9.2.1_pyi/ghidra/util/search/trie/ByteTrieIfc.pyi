from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import ghidra.util.search.trie
import ghidra.util.task
import java.lang


class ByteTrieIfc(object):








    def add(self, value: List[int], item: object) -> bool:
        """
        Adds a byte sequence to the trie, with corresponding user item.  Returns
         if the add took place, or if this add was essentially a replacement of
         a previously present value (previous user item is lost forever).
        @param value the byte sequence to insert into the trie
        @param item a user item to store in that location
        @return whether the add took place
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def find(self, value: List[int]) -> ghidra.util.search.trie.ByteTrieNodeIfc:
        """
        Finds a byte sequence in the trie and returns a node interface object for it,
         or null if not present.
        @param value the byte sequence sought
        @return the node interface if present, or null
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def inorder(self, monitor: ghidra.util.task.TaskMonitor, op: ghidra.util.search.trie.Op) -> None:
        """
        Visits all the nodes in the trie such that the visitation order is properly
         byte value ordered. The client is responsible for not performing actions on
         non-terminal nodes as necessary.
        @param monitor a task monitor
        @param op the operation to perform
        @throws CancelledException if the user cancels
        """
        ...

    def isEmpty(self) -> bool:
        """
        Returns if the trie is empty.
        @return if the trie is empty
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numberOfNodes(self) -> int:
        """
        Returns the number of nodes in the trie; this is essentially equal
         to the sum of the number of characters in all byte sequences present in
         the trie, minus their shared prefixes.
        @return the number of nodes in the trie
        """
        ...

    @overload
    def search(self, text: List[int], monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.util.search.trie.SearchResult]:
        """
        Search an array of bytes using the Aho-Corasick multiple string
         trie search algorithm.
        @param text the bytes to search
        @return a list of results (tuple of offset position, text found)
        @throws CancelledException if the search is cancelled
        """
        ...

    @overload
    def search(self, memory: ghidra.program.model.mem.Memory, view: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.util.search.trie.SearchResult]:
        """
        Search an array of bytes using the Aho-Corasick multiple string
         trie search algorithm.
        @param memory the memory to search in
        @param view the AddressSetView to restrict the memory search to.
        @param monitor the task monitor
        @return a list of results (tuple of offset position, text found)
        @throws MemoryAccessException if an error occurs reading the memory
        @throws CancelledException if the search is cancelled
        """
        ...

    def size(self) -> int:
        """
        Returns the number of byte sequences in the trie.
        @return the number of byte sequences in the trie
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
