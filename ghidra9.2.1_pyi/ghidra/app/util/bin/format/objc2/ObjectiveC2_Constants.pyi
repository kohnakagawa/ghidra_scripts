from typing import List
import ghidra.program.model.listing
import java.lang


class ObjectiveC2_Constants(object):
    CATEGORY: unicode = u'/_objc2_'
    CATEGORY_PATH: ghidra.program.model.data.CategoryPath = /_objc2_
    NAMESPACE: unicode = u'objc2'
    OBJC2_CATEGORY_LIST: unicode = u'__objc_catlist'
    OBJC2_CLASS_LIST: unicode = u'__objc_classlist'
    OBJC2_CLASS_REFS: unicode = u'__objc_classrefs'
    OBJC2_CONST: unicode = u'__objc_const'
    OBJC2_DATA: unicode = u'__objc_data'
    OBJC2_IMAGE_INFO: unicode = u'__objc_imageinfo'
    OBJC2_MESSAGE_REFS: unicode = u'__objc_msgrefs'
    OBJC2_NON_LAZY_CLASS_LIST: unicode = u'__objc_nlclslist'
    OBJC2_PROTOCOL_LIST: unicode = u'__objc_protolist'
    OBJC2_PROTOCOL_REFS: unicode = u'__objc_protorefs'
    OBJC2_SELECTOR_REFS: unicode = u'__objc_selrefs'
    OBJC2_SUPER_REFS: unicode = u'__objc_superrefs'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getObjectiveC2SectionNames() -> List[unicode]:
        """
        Returns a list containing valid Objective-C 2.0 section names.
        @return a list containing valid Objective-C 2.0 section names
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isObjectiveC2(program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if this program contains Objective-C 2.
        @param program the program to check
        @return true if the program contains Objective-C 2.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
