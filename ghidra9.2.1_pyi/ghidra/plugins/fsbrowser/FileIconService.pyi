from typing import List
import ghidra.plugins.fsbrowser
import java.lang
import javax.swing


class FileIconService(object):
    """
    Provides Icons that represent the type and status of a file, based on
     a filename mapping and caller specified status overlays.

     The mappings between a file's extension and its icon are stored in a resource
     file called "file_extension_icons.xml", which is read and parsed the first
     time this service is referenced.

     Status overlays are also specified in the file_extension_icons.xml file, and
     are resized to be 1/2 the width and height of the icon they are being
     overlaid on.

     Threadsafe

    """

    OVERLAY_FILESYSTEM: unicode = u'filesystem'
    OVERLAY_IMPORTED: unicode = u'imported'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getImage(self, fileName: unicode, overlays: List[unicode]) -> javax.swing.Icon:
        """
        Returns an {@link Icon} that represents a file's content based on its
         name.
        @param fileName name of file that an icon is being requested for.
        @param overlays optional list of overlay names, names of icons that
                    should be overlaid on top of the base icon, that represent a
                    status or feature independent of the file's base icon.
        @return {@link Icon} instance that best represents the named file, never
                 null.
        """
        ...

    @staticmethod
    def getInstance() -> ghidra.plugins.fsbrowser.FileIconService: ...

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
