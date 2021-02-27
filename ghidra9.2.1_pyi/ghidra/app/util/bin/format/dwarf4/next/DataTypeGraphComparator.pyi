import ghidra.app.util.bin.format.dwarf4.next.DataTypeGraphComparator
import ghidra.program.model.data
import java.lang


class DataTypeGraphComparator(object):
    """
    Compares two DataType directed graphs, calling a
     DataTypePairObserver#observe(DataType, DataType) that can observe each
     DataType pair that occupy equivalent positions in each graph.

     The first/left DataType graph is assumed to be composed of DataTypeImpl instances,
     and the second/right DataType graph is assumed to be composed of DataType DB instances.

     Only DataTypes in the left graph are followed and may lead to a possible match with
     the right graph.

     This class is used to help transfer mappings that point to impl DataTypes to also point them
     at the resultant 'db' DataTypes that are created by the DataTypeManager.
    """






    class DataTypePairObserver(object):








        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def observe(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType) -> bool: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    @staticmethod
    def compare(preDT: ghidra.program.model.data.DataType, postDT: ghidra.program.model.data.DataType, observer: ghidra.app.util.bin.format.dwarf4.next.DataTypeGraphComparator.DataTypePairObserver) -> None:
        """
        Compares two {@link DataType datatypes} graphs, calling the observer callback
         for each paired DataType that occupy equivalent positions in each graph.
         <p>
        @param preDT - Original (impl) DataType from before submitting to DataTypeManager.
        @param postDT - Result DataType from the DataTypeManager
        @param observer - Callback called for each position in the preDT graph that has a matching
         position in the postDT graph.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
