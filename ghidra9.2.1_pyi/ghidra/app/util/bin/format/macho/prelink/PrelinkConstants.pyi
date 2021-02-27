import java.lang


class PrelinkConstants(object):
    """
    Taken from:
     http://www.opensource.apple.com/source/xnu/xnu-1456.1.26/libkern/libkern/prelink.h
    """

    TITLE: unicode = u'iOS Prelink'
    kPrelinkBundlePathKey: unicode = u'_PrelinkBundlePath'
    kPrelinkExecutableKey: unicode = u'_PrelinkExecutable'
    kPrelinkExecutableLoadKey: unicode = u'_PrelinkExecutableLoadAddr'
    kPrelinkExecutableSizeKey: unicode = u'_PrelinkExecutableSize'
    kPrelinkExecutableSourceKey: unicode = u'_PrelinkExecutableSourceAddr'
    kPrelinkInfoDictionaryKey: unicode = u'_PrelinkInfoDictionary'
    kPrelinkInfoSection: unicode = u'__info'
    kPrelinkInfoSegment: unicode = u'__PRELINK_INFO'
    kPrelinkInterfaceUUIDKey: unicode = u'_PrelinkInterfaceUUID'
    kPrelinkKernelLinkStateSection: unicode = u'__kernel'
    kPrelinkKextsLinkStateSection: unicode = u'__kexts'
    kPrelinkKmodInfoKey: unicode = u'_PrelinkKmodInfo'
    kPrelinkLinkStateKey: unicode = u'_PrelinkLinkState'
    kPrelinkLinkStateSizeKey: unicode = u'_PrelinkLinkStateSize'
    kPrelinkModuleIndexKey: unicode = u'ModuleIndex'
    kPrelinkPersonalitiesKey: unicode = u'_PrelinkPersonalities'
    kPrelinkSegment_iOS_1x: unicode = u'__PRELINK'
    kPrelinkStateSegment: unicode = u'__PRELINK_STATE'
    kPrelinkTextSection: unicode = u'__text'
    kPrelinkTextSegment: unicode = u'__PRELINK_TEXT'



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
