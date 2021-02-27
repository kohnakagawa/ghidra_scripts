import java.lang


class AttributesConstants(object):
    AnnotationDefault: unicode = u'AnnotationDefault'
    BootstrapMethods: unicode = u'BootstrapMethods'
    Code: unicode = u'Code'
    ConstantValue: unicode = u'ConstantValue'
    Deprecated: unicode = u'Deprecated'
    EnclosingMethod: unicode = u'EnclosingMethod'
    Exceptions: unicode = u'Exceptions'
    InnerClasses: unicode = u'InnerClasses'
    LineNumberTable: unicode = u'LineNumberTable'
    LocalVariableTable: unicode = u'LocalVariableTable'
    LocalVariableTypeTable: unicode = u'LocalVariableTypeTable'
    Module: unicode = u'Module'
    ModuleMainClass: unicode = u'ModuleMainClass'
    ModulePackages: unicode = u'ModulePackages'
    NestHost: unicode = u'NestHost'
    NestMembers: unicode = u'NestMembers'
    RuntimeInvisibleAnnotations: unicode = u'RuntimeInvisibleAnnotations'
    RuntimeInvisibleParameterAnnotations: unicode = u'RuntimeInvisibleParameterAnnotations'
    RuntimeVisibleAnnotations: unicode = u'RuntimeVisibleAnnotations'
    RuntimeVisibleParameterAnnotations: unicode = u'RuntimeVisibleParameterAnnotations'
    Signature: unicode = u'Signature'
    SourceDebugExtension: unicode = u'SourceDebugExtension'
    SourceFile: unicode = u'SourceFile'
    StackMapTable: unicode = u'StackMapTable'
    Synthetic: unicode = u'Synthetic'



    def __init__(self): ...



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
