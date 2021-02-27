from typing import List
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.xml
import java.lang


class PcodeInjectLibraryJava(ghidra.program.model.lang.PcodeInjectLibrary):
    CONSTANT_POOL_START_ADDRESS: int = 10
    GETFIELD: unicode = u'getFieldCallOther'
    GETSTATIC: unicode = u'getStaticCallOther'
    INVOKE_DYNAMIC: unicode = u'invokedynamicCallOther'
    INVOKE_INTERFACE: unicode = u'invokeinterfaceCallOther'
    INVOKE_SPECIAL: unicode = u'invokespecialCallOther'
    INVOKE_STATIC: unicode = u'invokestaticCallOther'
    INVOKE_VIRTUAL: unicode = u'invokevirtualCallOther'
    LDC: unicode = u'ldcCallOther'
    LDC2_W: unicode = u'ldc2_wCallOther'
    LDC_W: unicode = u'ldc_wCallOther'
    MULTIANEWARRAY: unicode = u'multianewarrayCallOther'
    PUTFIELD: unicode = u'putFieldCallOther'
    PUTSTATIC: unicode = u'putStaticCallOther'
    REFERENCE_SIZE: int = 4
    SOURCENAME: unicode = u'javainternal'



    def __init__(self, __a0: ghidra.app.plugin.processors.sleigh.SleighLanguage): ...



    def buildInjectContext(self) -> ghidra.program.model.lang.InjectContext: ...

    def equals(self, __a0: object) -> bool: ...

    def getCallFixupNames(self) -> List[unicode]: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstantPool(self, __a0: ghidra.program.model.listing.Program) -> ghidra.program.model.lang.ConstantPool: ...

    def getPayload(self, __a0: int, __a1: unicode, __a2: ghidra.program.model.listing.Program, __a3: unicode) -> ghidra.program.model.lang.InjectPayload: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXmlInject(self, __a0: unicode, __a1: unicode, __a2: int, __a3: ghidra.xml.XmlPullParser) -> ghidra.program.model.lang.InjectPayload: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
