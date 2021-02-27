from typing import List
import ghidra.docking.settings
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import java.lang


class StringDataInstance(object):
    """
    Represents an instance of a string in a MemBuffer.

     This class handles all the details of detecting a terminated string's length,
     converting the bytes in the membuffer into a java native String, and converting
     the raw String into a formatted human-readable version, according to the
     various SettingsDefinitions attached to the string data location.

    """

    DEFAULT_CHARSET_NAME: unicode = u'US-ASCII'
    MAX_STRING_LENGTH: int = 16384
    NULL_INSTANCE: ghidra.program.model.data.StringDataInstance =
    UNKNOWN: unicode = u'??'
    UNKNOWN_DOT_DOT_DOT: unicode = u'??...'




    class StaticStringInstance(ghidra.program.model.data.StringDataInstance):




        def __init__(self, __a0: unicode, __a1: int): ...



        def equals(self, __a0: object) -> bool: ...

        def getAddress(self) -> ghidra.program.model.address.Address: ...

        def getByteOffcut(self, __a0: int) -> ghidra.program.model.data.StringDataInstance: ...

        def getCharOffcut(self, __a0: int) -> ghidra.program.model.data.StringDataInstance: ...

        @overload
        def getCharRepresentation(self) -> unicode: ...

        @overload
        @staticmethod
        def getCharRepresentation(__a0: ghidra.program.model.data.DataType, __a1: List[int], __a2: ghidra.docking.settings.Settings) -> unicode: ...

        def getCharsetName(self) -> unicode: ...

        def getClass(self) -> java.lang.Class: ...

        def getDataLength(self) -> int: ...

        def getLabel(self, __a0: unicode, __a1: unicode, __a2: unicode, __a3: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

        def getOffcutLabelString(self, __a0: unicode, __a1: unicode, __a2: unicode, __a3: ghidra.program.model.data.DataTypeDisplayOptions, __a4: int) -> unicode: ...

        @overload
        @staticmethod
        def getStringDataInstance(__a0: ghidra.program.model.listing.Data) -> ghidra.program.model.data.StringDataInstance: ...

        @overload
        @staticmethod
        def getStringDataInstance(__a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.mem.MemBuffer, __a2: ghidra.docking.settings.Settings, __a3: int) -> ghidra.program.model.data.StringDataInstance: ...

        def getStringDataTypeGuess(self) -> ghidra.program.model.data.DataType: ...

        def getStringLength(self) -> int: ...

        def getStringRepresentation(self) -> unicode: ...

        def getStringValue(self) -> unicode: ...

        def getTranslatedValue(self) -> unicode: ...

        def hashCode(self) -> int: ...

        @staticmethod
        def isChar(__a0: ghidra.program.model.listing.Data) -> bool: ...

        def isMissingNullTerminator(self) -> bool: ...

        def isShowTranslation(self) -> bool: ...

        @staticmethod
        def isString(__a0: ghidra.program.model.listing.Data) -> bool: ...

        @staticmethod
        def isStringDataType(__a0: ghidra.program.model.data.DataType) -> bool: ...

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
        def stringLength(self) -> int: ...

        @property
        def stringRepresentation(self) -> unicode: ...

        @property
        def stringValue(self) -> unicode: ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, settings: ghidra.docking.settings.Settings, buf: ghidra.program.model.mem.MemBuffer, length: int):
        """
        Creates a string instance using the data in the {@link MemBuffer} and the settings
         pulled from the {@link AbstractStringDataType string data type}.
        @param dataType {@link DataType} of the string, either a {@link AbstractStringDataType} derived type
         or an {@link ArrayStringable} element-of-char-array type.
        @param settings {@link Settings} attached to the data location.
        @param buf {@link MemBuffer} containing the data.
        @param length Length passed from the caller to the datatype.  -1 indicates a 'probe'
         trying to detect the length of an unknown string, otherwise it will be the length
         of the containing field of the data instance.
        """
        ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, settings: ghidra.docking.settings.Settings, buf: ghidra.program.model.mem.MemBuffer, length: int, isArrayElement: bool):
        """
        Creates a string instance using the data in the {@link MemBuffer} and the settings
         pulled from the {@link AbstractStringDataType string data type}.
        @param dataType {@link DataType} of the string, either a {@link AbstractStringDataType} derived type
         or an {@link ArrayStringable} element-of-char-array type.
        @param settings {@link Settings} attached to the data location.
        @param buf {@link MemBuffer} containing the data.
        @param length Length passed from the caller to the datatype.  -1 indicates a 'probe'
         trying to detect the length of an unknown string, otherwise it will be the length
         of the containing field of the data instance.
        @param isArrayElement boolean flag, true indicates that the specified dataType is an
         element in an array (ie. char[] vs. just a plain char), causing the string layout
         to be forced to {@link StringLayoutEnum#NULL_TERMINATED_BOUNDED}
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the {@link MemBuffer}.
        @return {@link Address} of the MemBuffer.
        """
        ...

    def getByteOffcut(self, byteOffset: int) -> ghidra.program.model.data.StringDataInstance:
        """
        Returns a new {@link StringDataInstance} that points to the string characters
         that start at {@code byteOffset} from the start of this instance.
         <p>
         If the requested offset is not valid, the base string instance (itself) will be returned
         instead of a new instance.
         <p>
        @param byteOffset number of bytes from start of data instance to start new instance.
        @return new StringDataInstance, or <code>this</code> if offset not valid.
        """
        ...

    def getCharOffcut(self, offsetChars: int) -> ghidra.program.model.data.StringDataInstance:
        """
        Create a new {@link StringDataInstance} that points to a portion of this
         instance, starting at a character offset (whereever that may be) into the data.
         <p>
        @param offsetChars number of characters from the beginning of the string to start
         the new StringDataInstance.
        @return new {@link StringDataInstance} pointing to a subset of characters, or the
         <code>this</code> instance if there was an error.
        """
        ...

    @overload
    def getCharRepresentation(self) -> unicode:
        """
        Convert a char value (or sequence of char values) in memory into its canonical unicode representation, using
         attached charset and encoding information.
         <p>
        @return String containing the representation of the char.
        """
        ...

    @overload
    @staticmethod
    def getCharRepresentation(dataType: ghidra.program.model.data.DataType, bytes: List[int], settings: ghidra.docking.settings.Settings) -> unicode:
        """
        Returns a string representation of the character(s) contained in the byte array, suitable
         for display as a single character, or as a sequence of characters.
         <p>
        @param dataType the {@link DataType} of the element containing the bytes (most likely a ByteDataType)
        @param bytes the big-endian ordered bytes to convert to a char representation
        @param settings the {@link Settings} object for the location where the bytes came from, or null
        @return formatted string (typically with quotes around the contents): single character: 'a', multiple characters: "a\x12bc"
        """
        ...

    def getCharsetName(self) -> unicode:
        """
        Returns the string name of the charset.
        @return string charset name
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataLength(self) -> int:
        """
        Returns the length of this string's data, in bytes.
        @return number of bytes in this string.
        """
        ...

    def getLabel(self, prefixStr: unicode, abbrevPrefixStr: unicode, defaultStr: unicode, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getOffcutLabelString(self, prefixStr: unicode, abbrevPrefixStr: unicode, defaultStr: unicode, options: ghidra.program.model.data.DataTypeDisplayOptions, byteOffset: int) -> unicode: ...

    @overload
    @staticmethod
    def getStringDataInstance(data: ghidra.program.model.listing.Data) -> ghidra.program.model.data.StringDataInstance:
        """
        Returns a new {@link StringDataInstance} using the bytes in the data codeunit.
         <p>
        @param data {@link Data} item
        @return new {@link StringDataInstance}, never NULL.  See {@link #NULL_INSTANCE}.
        """
        ...

    @overload
    @staticmethod
    def getStringDataInstance(dataType: ghidra.program.model.data.DataType, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> ghidra.program.model.data.StringDataInstance:
        """
        Returns a new {@link StringDataInstance} using the bytes in the MemBuffer.
         <p>
        @param dataType {@link DataType} of the bytes in the buffer.
        @param buf memory buffer containing the bytes.
        @param settings the Settings object
        @param length the length of the data.
        @return new {@link StringDataInstance}, never NULL.  See {@link #NULL_INSTANCE}.
        """
        ...

    def getStringDataTypeGuess(self) -> ghidra.program.model.data.DataType:
        """
        Maps a {@link StringDataInstance} (this type) to the String DataType that best
         can handle this type of data.
         <p>
         I dare myself to type Type one more time.
         <p>
        @return {@link DataType}, defaulting to {@link StringDataType} if no direct match found.
        """
        ...

    def getStringLength(self) -> int:
        """
        Returns the length, in bytes, of the string data object contained in the
         {@link MemBuffer}, or -1 if the length could not be determined.
         <p>
         This is not the same as the number of characters in the string, or the number of bytes
         occupied by the characters.  For instance, pascal strings have a 1 or 2 byte length
         field that increases the size of the string data object beyond the characters in the
         string, and null terminated strings have don't include the null character, but its
         presence is included in the size of the string object.
         <p>
         For length-specified string data types that do not use null-terminators and with a
         known data instance length (ie. not a probe), this method just returns the
         value specified in the constructor {@code length} parameter, otherwise a null-terminator
         is searched for.
         <p>
         When searching for a null-terminator, the constructor {@code length} parameter will
         be respected or ignored depending on the {@link StringLayoutEnum}.
         <p>
         When the length parameter is ignored (ie. "unbounded" searching), the search is
         limited to {@link #MAX_STRING_LENGTH} bytes.
         <p>
         The MemBuffer's endian'ness is used to determine which end of the padded character
         field contains our n-bit character which will be tested for null-ness.  (not the
         endian'ness of the character set name - ie. "UTF-16BE")
        @return length of the string (NOT including null term if null term probe), in bytes,
         or -1 if no terminator found.
        """
        ...

    def getStringRepresentation(self) -> unicode:
        """
        Returns a formatted version of the string returned by {@link #getStringValue()}.
         <p>
         The resulting string will be formatted with quotes around the parts that contain
         plain ASCII alpha characters (and simple escape sequences), and out-of-range
         byte-ish values listed as comma separated hex-encoded values:
         <p>
         Example (quotes are part of result): {@code "Test\tstring",01,02,"Second\npart",00}
        @return formatted String
        """
        ...

    def getStringValue(self) -> unicode:
        """
        Returns the string contained in the specified {@link MemBuffer}, or null if
         all the bytes of the string could not be read.
         <p>
         This method deals in characters of size {@link #charSize}, that might be
         {@link #paddedCharSize padded} to a larger size.  The raw n-byte characters
         are converted into a Java String using a Java {@link Charset} or by
         using a custom Ghidra conversion.  (see convertBytesToStringCustomCharset)
         <p>
         The MemBuffer's endian'ness is used to determine which end of the
         {@link #paddedCharSize padded } field contains our {@link #charSize}
         character bytes which will be used to create the java String.
        @return String containing the characters in buf or null if unable to read all
         {@code length} bytes from the membuffer.
        """
        ...

    def getTranslatedValue(self) -> unicode:
        """
        Returns the value of the stored
         {@link TranslationSettingsDefinition#getTranslatedValue(Settings) translated settings}
         string.
         <p>
        @return previously translated string.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isChar(data: ghidra.program.model.listing.Data) -> bool:
        """
        Returns true if the {@link Data} instance is one of the many 'char' data types.
        @param data {@link Data} instance to test, null ok
        @return boolean true if char data
        """
        ...

    def isMissingNullTerminator(self) -> bool:
        """
        Returns true if the string should have a trailing NULL character and doesn't.
        @return boolean true if the trailing NULL character is missing, false if string type
         doesn't need a trailing NULL character or if it is present.
        """
        ...

    def isShowTranslation(self) -> bool:
        """
        Returns true if the user should be shown the translated value of the string instead
         of the real value.
        @return boolean true if should show previously translated value.
        """
        ...

    @staticmethod
    def isString(data: ghidra.program.model.listing.Data) -> bool:
        """
        Returns true if the {@link Data} instance is a 'string'.
        @param data {@link Data} instance to test, null ok.
        @return boolean true if string data.
        """
        ...

    @staticmethod
    def isStringDataType(dt: ghidra.program.model.data.DataType) -> bool:
        """
        Returns true if the specified {@link DataType} is (or could be) a
         string.
         <p>
         Arrays of char-like elements (see {@link ArrayStringable}) are treated
         as string data types.  The actual data instance needs to be inspected
         to determine if the array is an actual string.
         <p>
        @param dt DataType to test
        @return boolean true if data type is or could be a string
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

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def charRepresentation(self) -> unicode: ...

    @property
    def charsetName(self) -> unicode: ...

    @property
    def dataLength(self) -> int: ...

    @property
    def missingNullTerminator(self) -> bool: ...

    @property
    def showTranslation(self) -> bool: ...

    @property
    def stringDataTypeGuess(self) -> ghidra.program.model.data.DataType: ...

    @property
    def stringLength(self) -> int: ...

    @property
    def stringRepresentation(self) -> unicode: ...

    @property
    def stringValue(self) -> unicode: ...

    @property
    def translatedValue(self) -> unicode: ...
