import java.lang


class GEdge(object):
    """
    An edge in a (usually directed) graph
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEnd(self) -> V:
        """
        Get the end, or head, of the edge

         <P>In the edge x -&gt; y, y is the end
        @return the end
        """
        ...

    def getStart(self) -> V:
        """
        Get the start, or tail, of the edge

         <P>In the edge x -&gt; y, x is the start
        @return the start
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
    def end(self) -> object: ...

    @property
    def start(self) -> object: ...
