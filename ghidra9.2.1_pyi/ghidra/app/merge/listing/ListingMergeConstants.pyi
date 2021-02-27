import java.lang


class ListingMergeConstants(object):
    """
    ListingMergeConstants is an interface that provides constants
     that are used throughout all of the Listing merge managers for multi-user.
    """

    ASK_USER: int = 0
    CANCELED: int = -1
    CHECKED_OUT_BUTTON_NAME: unicode = u'CheckedOutVersionRB'
    CHECKED_OUT_CHECK_BOX_NAME: unicode = u'CheckedOutVersionCheckBox'
    CHECKED_OUT_LABEL_NAME: unicode = u'CheckedOutVersionLabel'
    CHECKED_OUT_LIST_BUTTON_NAME: unicode = u'CheckedOutListRB'
    INFO_ROW: int = 0
    KEEP_ALL: int = 7
    KEEP_BOTH: int = 6
    KEEP_LATEST: int = 2
    KEEP_MY: int = 4
    KEEP_ORIGINAL: int = 1
    KEEP_RESULT: int = 8
    LATEST_BUTTON_NAME: unicode = u'LatestVersionRB'
    LATEST_CHECK_BOX_NAME: unicode = u'LatestVersionCheckBox'
    LATEST_LABEL_NAME: unicode = u'LatestVersionLabel'
    LATEST_LIST_BUTTON_NAME: unicode = u'LatestListRB'
    LATEST_TITLE: unicode = u'Latest'
    MY_TITLE: unicode = u'Checked Out'
    ORIGINAL_BUTTON_NAME: unicode = u'OriginalVersionRB'
    ORIGINAL_CHECK_BOX_NAME: unicode = u'OriginalVersionCheckBox'
    ORIGINAL_LABEL_NAME: unicode = u'OriginalVersionLabel'
    ORIGINAL_TITLE: unicode = u'Original'
    REMOVE_CHECKED_OUT_BUTTON_NAME: unicode = u'RemoveCheckedOutRB'
    REMOVE_LATEST: int = 8
    REMOVE_LATEST_BUTTON_NAME: unicode = u'RemoveLatestRB'
    REMOVE_MY: int = 32
    RENAME_CHECKED_OUT_BUTTON_NAME: unicode = u'RenameCheckedOutRB'
    RENAME_LATEST: int = 16
    RENAME_LATEST_BUTTON_NAME: unicode = u'RenameLatestRB'
    RENAME_MY: int = 64
    RESULT_BUTTON_NAME: unicode = u'ResultVersionRB'
    RESULT_TITLE: unicode = u'Result'
    TRUNCATE_LENGTH: int = 160







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
