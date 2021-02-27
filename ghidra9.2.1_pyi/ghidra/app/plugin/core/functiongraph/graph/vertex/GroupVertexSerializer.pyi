import ghidra.app.plugin.core.functiongraph.graph
import ghidra.app.plugin.core.functiongraph.mvc
import java.lang
import java.util
import org.jdom


class GroupVertexSerializer(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getXMLForGroupedVertices(__a0: ghidra.app.plugin.core.functiongraph.graph.FunctionGraph) -> org.jdom.Element: ...

    @staticmethod
    def getXMLForRegroupableVertices(__a0: ghidra.app.plugin.core.functiongraph.graph.FunctionGraph) -> org.jdom.Element: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def recreateGroupHistory(__a0: ghidra.app.plugin.core.functiongraph.mvc.FGController, __a1: org.jdom.Element) -> java.util.Collection: ...

    @staticmethod
    def recreateGroupedVertices(__a0: ghidra.app.plugin.core.functiongraph.mvc.FGController, __a1: org.jdom.Element) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
