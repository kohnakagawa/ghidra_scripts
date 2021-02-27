from typing import List
import ghidra.util.bytesearch
import ghidra.util.task
import java.io
import java.lang
import java.util


class SequenceSearchState(object, java.lang.Comparable):
    """
    SeqenceSearchState holds the state of a search for a DittedBitSequence within a byte
     sequence.
    """





    def __init__(self, parent: ghidra.util.bytesearch.SequenceSearchState):
        """
        Construct a sub sequence state with a parent sequence
        @param parent parent SequenceSearchState
        """
        ...



    def addSequence(self, pat: ghidra.util.bytesearch.DittedBitSequence, pos: int) -> None:
        """
        Add a pattern to this search sequence.  The last pattern added is the successful
         match pattern.
        @param pat pattern to add
        @param pos position within the current set of patterns to add this pattern
        """
        ...

    @overload
    def apply(self, __a0: List[int], __a1: java.util.ArrayList) -> None: ...

    @overload
    def apply(self, __a0: java.io.InputStream, __a1: java.util.ArrayList, __a2: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def apply(self, __a0: java.io.InputStream, __a1: long, __a2: java.util.ArrayList, __a3: ghidra.util.task.TaskMonitor) -> None: ...

    @staticmethod
    def buildStateMachine(patterns: java.util.ArrayList) -> ghidra.util.bytesearch.SequenceSearchState:
        """
        Build a search state machine from a list of DittedBitSequences
        @param patterns bit sequence patterns
        @return search state the will match the given sequences
        """
        ...

    @overload
    def compareTo(self, o: ghidra.util.bytesearch.SequenceSearchState) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMaxSequenceSize(self) -> int:
        """
        @return maximum number of bytes that could be matched by this sequence
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sequenceMatch(self, __a0: List[int], __a1: int, __a2: java.util.ArrayList) -> None: ...

    def sortSequences(self) -> None:
        """
        Sort the sequences that have been added
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
    def maxSequenceSize(self) -> int: ...
