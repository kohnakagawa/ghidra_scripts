import ghidra.util.graph
import java.lang


class KeyedObjectFactory(object):
    """
    The KeyedObjectFactory class is responsible for ensuring that no two
        vertices or edges have the same keys. One and only one instance of the
        KeyedObjectFactory may exist. In addition to ensuring that all vertices
        and edges contained within any graph have distinct keys, KeyedObjectFactory
        provides methods for obtaining the Object that a KeyedObject refers to. More
        than one vertex may refer to the same object. The object a Vertex refers
        to can not be changed. There is no method to return the vertex referring
        to a specific object since in theory there can be a one-to-many
        correspondence.
    """

    instance_: ghidra.util.graph.KeyedObjectFactory







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstance() -> ghidra.util.graph.KeyedObjectFactory:
        """
        Returns singleton instance of KeyedObjectFactory.
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
