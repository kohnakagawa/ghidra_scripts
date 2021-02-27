from typing import List
import ghidra.util.filechooser
import java.io
import java.lang


class ExtensionFileFilter(object, ghidra.util.filechooser.GhidraFileFilter):
    """
    A convenience implementation of FileFilter that filters out
     all files except for those type extensions that it knows about.

     Extensions are of the type ".foo", which is typically found on
     Windows and Unix boxes, but not on Mac. Case is ignored.

     Example - create a new filter that filters out all files
     but gif and jpg image files:

         GhidraFileChooser chooser = new GhidraFileChooser();
         ExtensionFileFilter filter = new ExtensionFileFilter(
                       new String{"gif", "jpg"}, "JPEG and GIF Images")
         chooser.addFileFilter(filter);

    """

    ALL: ghidra.util.filechooser.GhidraFileFilter = ghidra.util.filechooser.GhidraFileFilter$1@25becf17



    @overload
    def __init__(self, extension: unicode, description: unicode):
        """
        Creates a file filter that accepts the given file type.
         Example: new ExtensionFileFilter("jpg", "JPEG Image Images");

         Note that the "." before the extension is not needed. If
         provided, it will be ignored.
        @see #addExtension
        """
        ...

    @overload
    def __init__(self, filters: List[unicode], description: unicode):
        """
        Creates a file filter from the given string array and description.
         Example: new ExtensionFileFilter(String {"gif", "jpg"}, "Gif and JPG Images");

         Note that the "." before the extension is not needed and will be ignored.
        @see #addExtension
        """
        ...



    def accept(self, f: java.io.File, model: ghidra.util.filechooser.GhidraFileChooserModel) -> bool:
        """
        Return true if this file should be shown in the directory pane,
         false if it shouldn't.

         Files that begin with "." are ignored.
        @see #getExtension
        @see FileFilter#accept
        """
        ...

    def addExtension(self, extension: unicode) -> None:
        """
        Adds a filetype "dot" extension to filter against.

         For example: the following code will create a filter that filters
         out all files except those that end in ".jpg" and ".tif":

           ExtensionFileFilter filter = new ExtensionFileFilter();
           filter.addExtension("jpg");
           filter.addExtension("tif");

         Note that the "." before the extension is not needed and will be ignored.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def forExtensions(description: unicode, exts: List[unicode]) -> ghidra.util.filechooser.ExtensionFileFilter:
        """
        Creates a {@link ExtensionFileFilter} in a varargs friendly way.
        @param description String description of this set of file extensions.
        @param exts variable length list of file extensions, without leading dot.
        @return new {@link ExtensionFileFilter} instance.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns the human readable description of this filter. For
         example: "JPEG and GIF Image Files (*.jpg, *.gif)"
        """
        ...

    def getExtension(self, f: java.io.File) -> unicode:
        """
        Return the extension portion of the file's name .
        @see #getExtension
        @see FileFilter#accept
        """
        ...

    def hashCode(self) -> int: ...

    def isExtensionListInDescription(self) -> bool:
        """
        Returns whether the extension list (.jpg, .gif, etc) should
         show up in the human readable description.

         Only relevant if a description was provided in the constructor
         or using setDescription();
        @see #getDescription
        @see #setDescription
        @see #setExtensionListInDescription
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDescription(self, description: unicode) -> None:
        """
        Sets the human readable description of this filter. For
         example: filter.setDescription("Gif and JPG Images");
        @see #setDescription
        @see #setExtensionListInDescription
        @see #isExtensionListInDescription
        """
        ...

    def setExtensionListInDescription(self, b: bool) -> None:
        """
        Determines whether the extension list (.jpg, .gif, etc) should
         show up in the human readable description.

         Only relevant if a description was provided in the constructor
         or using setDescription();
        @see #getDescription
        @see #setDescription
        @see #isExtensionListInDescription
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def extensionListInDescription(self) -> bool: ...

    @extensionListInDescription.setter
    def extensionListInDescription(self, value: bool) -> None: ...
