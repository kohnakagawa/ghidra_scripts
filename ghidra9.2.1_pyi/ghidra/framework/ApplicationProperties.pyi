from typing import Iterator
from typing import List
import ghidra.framework
import java.io
import java.lang
import java.nio.charset
import java.util
import java.util.function


class ApplicationProperties(java.util.Properties):
    """
    The application properties.  Application properties may either be stored on disk, or created
     dynamically.
    """

    APPLICATION_GRADLE_MIN_PROPERTY: unicode = u'application.gradle.min'
    APPLICATION_JAVA_COMPILER_PROPERTY: unicode = u'application.java.compiler'
    APPLICATION_JAVA_MAX_PROPERTY: unicode = u'application.java.max'
    APPLICATION_JAVA_MIN_PROPERTY: unicode = u'application.java.min'
    APPLICATION_LAYOUT_VERSION_PROPERTY: unicode = u'application.layout.version'
    APPLICATION_NAME_PROPERTY: unicode = u'application.name'
    APPLICATION_VERSION_PROPERTY: unicode = u'application.version'
    BUILD_DATE_PROPERTY: unicode = u'application.build.date'
    BUILD_DATE_SHORT_PROPERTY: unicode = u'application.build.date.short'
    PROPERTY_FILE: unicode = u'application.properties'
    RELEASE_MARKING_PROPERTY: unicode = u'application.release.marking'
    RELEASE_NAME_PROPERTY: unicode = u'application.release.name'
    RELEASE_SOURCE_PROPERTY: unicode = u'application.release.source'
    REVISION_PROPERTY_PREFIX: unicode = u'application.revision.'
    TEST_RELEASE_PROPERTY: unicode = u'application.test.release'



    @overload
    def __init__(self, name: unicode):
        """
        Creates a new application properties with the given name. Additional properties
         may be set with {@link #setProperty}.
        @param name The application's name.
        """
        ...

    @overload
    def __init__(self, appPropertiesFile: generic.jar.ResourceFile):
        """
        Creates a new application properties from the given application properties file.
        @param appPropertiesFile The application properties file.
        @throws IOException If there was a problem loading/reading a discovered properties file.
        """
        ...

    @overload
    def __init__(self, applicationRootDirs: java.util.Collection):
        """
        Creates a new application properties from the application properties files found
         in the given application root directories.  If multiple application properties files
         are found, the properties from the files will be combined.  If duplicate keys exist,
         the newest key encountered will overwrite the existing key.
        @param applicationRootDirs The application root directories to look for the properties files in.
        @throws IOException If there was a problem loading/reading a discovered properties file.
        """
        ...

    @overload
    def __init__(self, name: unicode, version: unicode, releaseName: unicode):
        """
        Creates a new application properties with the given name and version. Additional properties
         may be set with {@link #setProperty}.
        @param name The application's name.
        @param version The application's version.
        @param releaseName The application's release name.
        """
        ...

    def __iter__(self): ...

    def clear(self) -> None: ...

    def clone(self) -> object: ...

    def compute(self, __a0: object, __a1: java.util.function.BiFunction) -> object: ...

    def computeIfAbsent(self, __a0: object, __a1: java.util.function.Function) -> object: ...

    def computeIfPresent(self, __a0: object, __a1: java.util.function.BiFunction) -> object: ...

    def contains(self, __a0: object) -> bool: ...

    def containsKey(self, __a0: object) -> bool: ...

    def containsValue(self, __a0: object) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Map) -> java.util.Map: ...

    def elements(self) -> java.util.Enumeration: ...

    @staticmethod
    def entry(__a0: object, __a1: object) -> java.util.Map.Entry: ...

    def entrySet(self) -> java.util.Set: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.BiConsumer) -> None: ...

    @staticmethod
    def fromFile(filename: unicode) -> ghidra.framework.ApplicationProperties:
        """
        Attempts to create an instance of this class by looking for the a properties file
         with the give name in the current working directory.
        @param filename the name of the properties file to load
        @return the new instance of this class created from the properties file on disk
        @throws IOException if there is no properties file found in the expected location
        """
        ...

    def getApplicationBuildDate(self) -> unicode:
        """
        Gets the application's build date.
        @return The application's build date.
        """
        ...

    def getApplicationName(self) -> unicode:
        """
        Gets the application's name.
        @return The application's name (empty string if undefined).
        """
        ...

    def getApplicationReleaseName(self) -> unicode:
        """
        Gets the application's release name.
        @return The application's release name (empty string if undefined).
        """
        ...

    def getApplicationVersion(self) -> unicode:
        """
        Gets the application's version.
        @return The application's version (empty string if undefined).
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getOrDefault(self, __a0: object, __a1: object) -> object: ...

    @overload
    def getProperty(self, propertyName: unicode) -> unicode:
        """
        Gets the given application property.  Note that if the specified property is defined
         as a system property, the system property will be given precedence and returned.
        @param propertyName The property name to get.
        @return The property.
        """
        ...

    @overload
    def getProperty(self, __a0: unicode, __a1: unicode) -> unicode: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def keySet(self) -> java.util.Set: ...

    def keys(self) -> java.util.Enumeration: ...

    @overload
    def list(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def list(self, __a0: java.io.PrintWriter) -> None: ...

    @overload
    def load(self, __a0: java.io.InputStream) -> None: ...

    @overload
    def load(self, __a0: java.io.Reader) -> None: ...

    def loadFromXML(self, __a0: java.io.InputStream) -> None: ...

    def merge(self, __a0: object, __a1: object, __a2: java.util.function.BiFunction) -> object: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def of() -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object, __a16: object, __a17: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object, __a16: object, __a17: object, __a18: object, __a19: object) -> java.util.Map: ...

    @staticmethod
    def ofEntries(__a0: List[java.util.Map.Entry]) -> java.util.Map: ...

    def propertyNames(self) -> java.util.Enumeration: ...

    def put(self, __a0: object, __a1: object) -> object: ...

    def putAll(self, __a0: java.util.Map) -> None: ...

    def putIfAbsent(self, __a0: object, __a1: object) -> object: ...

    @overload
    def remove(self, __a0: object) -> object: ...

    @overload
    def remove(self, __a0: object, __a1: object) -> bool: ...

    @overload
    def replace(self, __a0: object, __a1: object) -> object: ...

    @overload
    def replace(self, __a0: object, __a1: object, __a2: object) -> bool: ...

    def replaceAll(self, __a0: java.util.function.BiFunction) -> None: ...

    def save(self, __a0: java.io.OutputStream, __a1: unicode) -> None: ...

    def setProperty(self, __a0: unicode, __a1: unicode) -> object: ...

    def size(self) -> int: ...

    @overload
    def store(self, __a0: java.io.OutputStream, __a1: unicode) -> None: ...

    @overload
    def store(self, __a0: java.io.Writer, __a1: unicode) -> None: ...

    @overload
    def storeToXML(self, __a0: java.io.OutputStream, __a1: unicode) -> None: ...

    @overload
    def storeToXML(self, __a0: java.io.OutputStream, __a1: unicode, __a2: unicode) -> None: ...

    @overload
    def storeToXML(self, __a0: java.io.OutputStream, __a1: unicode, __a2: java.nio.charset.Charset) -> None: ...

    def stringPropertyNames(self) -> java.util.Set: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def applicationBuildDate(self) -> unicode: ...

    @property
    def applicationName(self) -> unicode: ...

    @property
    def applicationReleaseName(self) -> unicode: ...

    @property
    def applicationVersion(self) -> unicode: ...
