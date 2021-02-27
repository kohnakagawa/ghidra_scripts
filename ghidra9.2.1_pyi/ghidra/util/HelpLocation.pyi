import java.lang
import java.net


class HelpLocation(object):
    """
    Class to identify where help can be located for some object. Help can be
     set on actions or dialogs.
    """





    @overload
    def __init__(self, topic: unicode, anchor: unicode):
        """
        Construct a Help location using the specified topic and anchor names.
         An html file contained within the specified help topic directory must have an Anchor
         defined using the specified anchor name.
         <p>
         <b>Note:</b>  You can specify a <code>null</code> anchor value.  In that case, the given topic
         will be searched for a file with the same name as the topic.  If such a file exists,
         then that file will be used as the file for this location.  If no such file exists, then
         the help file to use <b>cannot be resolved</b>.  Therefore, it is best to always specify
         a value for the help location.
        @param topic topic directory name
        @param anchor anchor name or null
        """
        ...

    @overload
    def __init__(self, topic: unicode, anchor: unicode, inceptionInformation: unicode):
        """
        Construct a Help location using the specified topic and anchor names.
         An html file contained within the specified help topic directory must have an Anchor
         defined using the specified anchor name.
         <p>
         <b>Note:</b>  You can specify a <code>null</code> anchor value.  In that case, the given topic
         will be searched for a file with the same name as the topic.  If such a file exists,
         then that file will be used as the file for this location.  If no such file exists, then
         the help file to use <b>cannot be resolved</b>.  Therefore, it is best to always specify
         a value for the help location.
        @param topic topic directory name
        @param anchor anchor name or null
        @param inceptionInformation the description of from whence the item
                described by this location has come; can be null
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getAnchor(self) -> unicode:
        """
        Returns the topic anchor name if known, otherwise null.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getHelpId(self) -> unicode:
        """
        Get the help ID for this help location.
        @return null if there is a Help URL instead of a help ID
        """
        ...

    def getHelpURL(self) -> java.net.URL:
        """
        Get the help URL for this help location. A URL is created when the
         constructor <code>HelpLocation(Class, String, String)</code> is
         used by a plugin that has help relative to its class.
        @return the URL or null if a help ID is used
        """
        ...

    def getInceptionInformation(self) -> unicode:
        """
        Returns information describing how/where this help location was created.  This value may
         be null.
        @return information describing how/where this help location was created.
        """
        ...

    def getTopic(self) -> unicode:
        """
        Returns the topic name/path if known, otherwise null.
        """
        ...

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

    @property
    def anchor(self) -> unicode: ...

    @property
    def helpId(self) -> unicode: ...

    @property
    def helpURL(self) -> java.net.URL: ...

    @property
    def inceptionInformation(self) -> unicode: ...

    @property
    def topic(self) -> unicode: ...
