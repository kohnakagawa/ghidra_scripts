from typing import List
import ghidra.app.util.bin.format.pe.cli.tables
import java.lang


class CliTypeTable(java.lang.Enum):
    Assembly: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = Assembly
    AssemblyOS: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = AssemblyOS
    AssemblyProcessor: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = AssemblyProcessor
    AssemblyRef: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = AssemblyRef
    AssemblyRefOS: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = AssemblyRefOS
    AssemblyRefProcessor: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = AssemblyRefProcessor
    ClassLayout: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = ClassLayout
    Constant: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = Constant
    CustomAttribute: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = CustomAttribute
    DeclSecurity: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = DeclSecurity
    Event: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = Event
    EventMap: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = EventMap
    ExportedType: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = ExportedType
    Field: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = Field
    FieldLayout: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = FieldLayout
    FieldMarshal: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = FieldMarshal
    FieldRVA: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = FieldRVA
    File: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = File
    GenericParam: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = GenericParam
    GenericParamConstraint: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = GenericParamConstraint
    ImplMap: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = ImplMap
    InterfaceImpl: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = InterfaceImpl
    ManifestResource: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = ManifestResource
    MemberRef: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = MemberRef
    MethodDef: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = MethodDef
    MethodImpl: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = MethodImpl
    MethodSemantics: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = MethodSemantics
    MethodSpec: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = MethodSpec
    Module: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = Module
    ModuleRef: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = ModuleRef
    NestedClass: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = NestedClass
    Param: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = Param
    Property: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = Property
    PropertyMap: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = PropertyMap
    StandAloneSig: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = StandAloneSig
    TypeDef: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = TypeDef
    TypeRef: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = TypeRef
    TypeSpec: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable = TypeSpec







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromId(__a0: int) -> ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def id(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
