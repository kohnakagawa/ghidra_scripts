from typing import List
import ghidra.framework.main.logviewer.event
import java.lang


class FVEvent(object):
    """
    Custom events to be used in conjunction with the FVEventListener module. Users should
     construct an event, then fire it using FVEventListener#send(FVEvent).

     Two items are passed along with each event:
     	- The #eventType attribute specifies the event that is being fired.
     	- The #arg is a generic object and can be populated with whatever is appropriate for the
     associated event. It's up to the receiver to understand how to parse it.
    """

    arg: object
    eventType: ghidra.framework.main.logviewer.event.FVEvent.EventType




    class EventType(java.lang.Enum):
        COPY_SELECTION: ghidra.framework.main.logviewer.event.FVEvent.EventType = COPY_SELECTION
        DECREMENT_AND_ADD_SELECTION: ghidra.framework.main.logviewer.event.FVEvent.EventType = DECREMENT_AND_ADD_SELECTION
        DECREMENT_SELECTION: ghidra.framework.main.logviewer.event.FVEvent.EventType = DECREMENT_SELECTION
        FILE_CHANGED: ghidra.framework.main.logviewer.event.FVEvent.EventType = FILE_CHANGED
        INCREMENT_AND_ADD_SELECTION: ghidra.framework.main.logviewer.event.FVEvent.EventType = INCREMENT_AND_ADD_SELECTION
        INCREMENT_SELECTION: ghidra.framework.main.logviewer.event.FVEvent.EventType = INCREMENT_SELECTION
        OPEN_FILE_LOCATION: ghidra.framework.main.logviewer.event.FVEvent.EventType = OPEN_FILE_LOCATION
        RELOAD_FILE: ghidra.framework.main.logviewer.event.FVEvent.EventType = RELOAD_FILE
        SCROLL_END: ghidra.framework.main.logviewer.event.FVEvent.EventType = SCROLL_END
        SCROLL_END_2: ghidra.framework.main.logviewer.event.FVEvent.EventType = SCROLL_END_2
        SCROLL_HOME: ghidra.framework.main.logviewer.event.FVEvent.EventType = SCROLL_HOME
        SCROLL_LOCK_OFF: ghidra.framework.main.logviewer.event.FVEvent.EventType = SCROLL_LOCK_OFF
        SCROLL_LOCK_ON: ghidra.framework.main.logviewer.event.FVEvent.EventType = SCROLL_LOCK_ON
        SLIDER_CHANGED: ghidra.framework.main.logviewer.event.FVEvent.EventType = SLIDER_CHANGED
        VIEWPORT_DOWN: ghidra.framework.main.logviewer.event.FVEvent.EventType = VIEWPORT_DOWN
        VIEWPORT_PAGE_DOWN: ghidra.framework.main.logviewer.event.FVEvent.EventType = VIEWPORT_PAGE_DOWN
        VIEWPORT_PAGE_UP: ghidra.framework.main.logviewer.event.FVEvent.EventType = VIEWPORT_PAGE_UP
        VIEWPORT_UP: ghidra.framework.main.logviewer.event.FVEvent.EventType = VIEWPORT_UP
        VIEWPORT_UPDATE: ghidra.framework.main.logviewer.event.FVEvent.EventType = VIEWPORT_UPDATE







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.framework.main.logviewer.event.FVEvent.EventType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.framework.main.logviewer.event.FVEvent.EventType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, eventType: ghidra.framework.main.logviewer.event.FVEvent.EventType, arg: object):
        """
        @param eventType
        @param arg
        """
        ...



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
