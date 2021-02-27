from typing import List
import ghidra.pcodeCPort.slghsymbol
import java.lang


class symbol_type(java.lang.Enum):
    bitrange_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = bitrange_symbol
    context_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = context_symbol
    dummy_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = dummy_symbol
    end_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = end_symbol
    epsilon_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = epsilon_symbol
    label_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = label_symbol
    macro_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = macro_symbol
    name_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = name_symbol
    operand_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = operand_symbol
    section_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = section_symbol
    space_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = space_symbol
    start_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = start_symbol
    subtable_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = subtable_symbol
    token_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = token_symbol
    userop_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = userop_symbol
    value_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = value_symbol
    valuemap_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = valuemap_symbol
    varnode_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = varnode_symbol
    varnodelist_symbol: ghidra.pcodeCPort.slghsymbol.symbol_type = varnodelist_symbol







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.pcodeCPort.slghsymbol.symbol_type: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.pcodeCPort.slghsymbol.symbol_type]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
