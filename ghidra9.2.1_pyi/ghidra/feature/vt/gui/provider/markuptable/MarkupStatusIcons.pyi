import java.lang


class MarkupStatusIcons(object):
    APPLIED_ADDED_ICON: javax.swing.Icon = MultiIcon[jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/checkmark_green.gif, TranslateIcon[jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/Plus.png]]
    APPLIED_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/checkmark_green.gif
    APPLIED_REPLACED_ICON: javax.swing.Icon = MultiIcon[jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/checkmark_green.gif, TranslateIcon[jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/VersionTracking/lib/VersionTracking.jar!/images/sync_enabled.png]]
    APPLY_ADD_MENU_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/Plus.png
    APPLY_REPLACE_MENU_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/VersionTracking/lib/VersionTracking.jar!/images/sync_enabled.png
    CONFLICT_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/VersionTracking/lib/VersionTracking.jar!/images/cache.png
    DONT_CARE_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/VersionTracking/lib/VersionTracking.jar!/images/asterisk_orange.png
    DONT_KNOW_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Features/Base/lib/Base.jar!/images/unknown.gif
    FAILED_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/edit-delete.png
    REJECTED_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/dialog-cancel.png
    SAME_ICON: javax.swing.Icon = MultiIcon[jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/checkmark_green.gif, TranslateIcon[jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Docking/lib/Docking.jar!/images/checkmark_green.gif]]



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
