import java.lang


class XmlAttributes(object):
    """
    A container class for creating XML attribute strings.
     For example, given the following code:

     XmlAttributes attrs = new XmlAttributes();
     attrs.add("FIVE", 32, true);
     attrs.add("BAR", "foo");
     attrs.add("PI", 3.14159);

     The output would be: FIVE="0x20" BAR="foo" PI="3.14159".
    """





    def __init__(self):
        """
        Constructs a new empty XML attributes.
        """
        ...



    @overload
    def addAttribute(self, name: unicode, value: long) -> None:
        """
        Add a new long attribute as decimal.
        @param name the name of the new attribute
        @param value the long value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: int) -> None:
        """
        Add a new byte attribute as decimal.
        @param name the name of the new attribute
        @param value the byte value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: int) -> None:
        """
        Add a new byte attribute as decimal.
        @param name the name of the new attribute
        @param value the byte value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: int) -> None:
        """
        Add a new byte attribute as decimal.
        @param name the name of the new attribute
        @param value the byte value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: float) -> None:
        """
        Add a new float attribute.
        @param name the name of the new attribute
        @param value the float value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: float) -> None:
        """
        Add a new float attribute.
        @param name the name of the new attribute
        @param value the float value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: bool) -> None:
        """
        Add a new boolean attribute.
        @param name the name of the new attribute
        @param value the boolean value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: unicode) -> None:
        """
        Add a new string attribute.
        @param name the name of the new attribute
        @param value the string value
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: long, hex: bool) -> None:
        """
        Add a new long attribute.
        @param name the name of the new attribute
        @param value the long value
        @param hex true if value should be written in hex
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: int, hex: bool) -> None:
        """
        Add a new byte attribute.
        @param name the name of the new attribute
        @param value the byte value
        @param hex true if value should be written in hex
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: int, hex: bool) -> None:
        """
        Add a new byte attribute.
        @param name the name of the new attribute
        @param value the byte value
        @param hex true if value should be written in hex
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: int, hex: bool) -> None:
        """
        Add a new byte attribute.
        @param name the name of the new attribute
        @param value the byte value
        @param hex true if value should be written in hex
        """
        ...

    @overload
    def addAttribute(self, name: unicode, value: long, hex: bool) -> None:
        """
        Add a new long attribute.
        @param name the name of the new attribute
        @param value the long value
        @param hex true if value should be written in hex
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        @return the number of attributes in this
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...
