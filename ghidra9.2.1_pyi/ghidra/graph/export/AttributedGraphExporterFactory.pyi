import ghidra.graph.export
import java.lang
import org.jgrapht.nio


class AttributedGraphExporterFactory(ghidra.graph.export.AbstractGraphExporterFactory):








    def createExporter(self, __a0: ghidra.graph.export.GraphExportFormat) -> org.jgrapht.nio.GraphExporter: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getExporter(__a0: ghidra.graph.export.GraphExportFormat) -> org.jgrapht.nio.GraphExporter: ...

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
