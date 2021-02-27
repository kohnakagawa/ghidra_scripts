from typing import List
import ghidra.app.util
import ghidra.app.util.exporter
import ghidra.app.util.importer
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class CppExporter(ghidra.app.util.exporter.Exporter):
    CREATE_C_FILE: unicode = u'Create C File (.c)'
    CREATE_HEADER_FILE: unicode = u'Create Header File (.h)'
    EMIT_TYPE_DEFINITONS: unicode = u'Emit data-type definitions'
    FUNCTION_TAG_EXCLUDE: unicode = u'Function tags excluded'
    FUNCTION_TAG_FILTERS: unicode = u'Function tags to filter'
    SPLIT_FILE: unicode = u'Split each function into individual file'
    USE_CPP_STYLE_COMMENTS: unicode = u'Use C++ Style comments (//)'



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: ghidra.app.decompiler.DecompileOptions): ...

    @overload
    def __init__(self, __a0: bool, __a1: bool, __a2: bool, __a3: bool, __a4: unicode): ...



    def canExportDomainObject(self, __a0: java.lang.Class) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def export(self, __a0: java.io.File, __a1: ghidra.framework.model.DomainObject, __a2: ghidra.program.model.address.AddressSetView, __a3: ghidra.util.task.TaskMonitor) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultFileExtension(self) -> unicode: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getMessageLog(self) -> ghidra.app.util.importer.MessageLog: ...

    def getName(self) -> unicode: ...

    def getOptions(self, __a0: ghidra.app.util.DomainObjectService) -> List[object]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setExporterServiceProvider(self, __a0: ghidra.framework.plugintool.ServiceProvider) -> None: ...

    def setOptions(self, __a0: List[object]) -> None: ...

    def supportsPartialExport(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def options(self) -> None: ...  # No getter available.

    @options.setter
    def options(self, value: List[object]) -> None: ...
