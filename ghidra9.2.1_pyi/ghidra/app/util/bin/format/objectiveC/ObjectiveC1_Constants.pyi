from typing import List
import ghidra.program.model.listing
import java.lang


class ObjectiveC1_Constants(object):
    CATEGORY: unicode = u'/objc'
    CATEGORY_PATH: ghidra.program.model.data.CategoryPath = /objc
    NAMESPACE: unicode = u'objc'
    OBJC_MSG_SEND: unicode = u'_objc_msgSend'
    OBJC_MSG_SEND_RTP_NAME: unicode = u'_objc_msgSend_rtp'
    OBJC_MSG_SEND_WILDCARD: unicode = u'_objc_msgSend*'
    OBJC_SECTION_CATEGORY: unicode = u'__category'
    OBJC_SECTION_CATEGORY_CLASS_METHODS: unicode = u'__cat_cls_meth'
    OBJC_SECTION_CATEGORY_INSTANCE_METHODS: unicode = u'__cat_inst_meth'
    OBJC_SECTION_CLASS: unicode = u'__class'
    OBJC_SECTION_CLASS_METHODS: unicode = u'__cls_meth'
    OBJC_SECTION_CLASS_REFS: unicode = u'__cls_refs'
    OBJC_SECTION_DATA: unicode = u'__data'
    OBJC_SECTION_INSTANCE_METHODS: unicode = u'__inst_meth'
    OBJC_SECTION_INSTANCE_VARS: unicode = u'__instance_vars'
    OBJC_SECTION_MESSAGE_REFS: unicode = u'__message_refs'
    OBJC_SECTION_METACLASS: unicode = u'__meta_class'
    OBJC_SECTION_MODULE_INFO: unicode = u'__module_info'
    OBJC_SECTION_PROTOCOL: unicode = u'__protocol'
    OBJC_SECTION_SYMBOLS: unicode = u'__symbols'
    OBJ_MSGSEND_RTP: long = 0xfffeff00L
    OBJ_MSGSEND_RTP_EXIT: long = 0xffff0000L
    READ_UNIX2003: unicode = u'_read$UNIX2003'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getObjectiveCSectionNames() -> List[unicode]:
        """
        Returns a list containing valid Objective-C section names.
        @return a list containing valid Objective-C section names
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isObjectiveC(program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if this program contains Objective-C.
        @param program the program to check
        @return true if the program contains Objective-C.
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
