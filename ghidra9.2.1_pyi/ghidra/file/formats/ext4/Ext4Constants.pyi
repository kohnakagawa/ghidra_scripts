import java.lang


class Ext4Constants(object):
    COMPAT_DIR_INDEX: int = 32
    COMPAT_DIR_PREALLOC: int = 1
    COMPAT_EXCLUDE_BITMAP: int = 256
    COMPAT_EXCLUDE_INODE: int = 128
    COMPAT_EXT_ATTR: int = 8
    COMPAT_HAS_JOURNAL: int = 4
    COMPAT_IMAGIC_INODES: int = 2
    COMPAT_LAZY_BG: int = 64
    COMPAT_RESIZE_INODE: int = 16
    COMPAT_SPARSE_SUPER2: int = 512
    EXT4_APPEND_FL: int = 32
    EXT4_COMPRBLK_FL: int = 512
    EXT4_COMPR_FL: int = 4
    EXT4_DIRSYNC_FL: int = 65536
    EXT4_DIRTY_FL: int = 256
    EXT4_EA_INODE_FL: int = 2097152
    EXT4_ENCRYPT_FL: int = 2048
    EXT4_EOFBLOCKS_FL: int = 4194304
    EXT4_EXTENTS_FL: int = 524288
    EXT4_FT_BLKDEV: int = 4
    EXT4_FT_CHRDEV: int = 3
    EXT4_FT_DIR: int = 2
    EXT4_FT_DIR_CSUM: int = -34
    EXT4_FT_FIFO: int = 5
    EXT4_FT_MAX: int = 8
    EXT4_FT_REG_FILE: int = 1
    EXT4_FT_SOCK: int = 6
    EXT4_FT_SYMLINK: int = 7
    EXT4_FT_UNKNOWN: int = 0
    EXT4_HUGE_FILE_FL: int = 262144
    EXT4_IMAGIC_FL: int = 8192
    EXT4_IMMUTABLE_FL: int = 16
    EXT4_INDEX_FL: int = 4096
    EXT4_INLINE_DATA_FL: int = 268435456
    EXT4_JOURNAL_DATA_FL: int = 16384
    EXT4_NOATIME_FL: int = 128
    EXT4_NOCOMPR_FL: int = 1024
    EXT4_NODUMP_FL: int = 64
    EXT4_NOTAIL_FL: int = 32768
    EXT4_PROJINHERIT_FL: int = 536870912
    EXT4_RESERVED_FL: int = -2147483648
    EXT4_SECRM_FL: int = 1
    EXT4_SNAPFILE_DELETED_FL: int = 67108864
    EXT4_SNAPFILE_FL: int = 16777216
    EXT4_SNAPFILE_SHRUNK_FL: int = 134217728
    EXT4_SYNC_FL: int = 8
    EXT4_TOPDIR_FL: int = 131072
    EXT4_UNRM_FL: int = 2
    EXTENT_HEADER_MAGIC: int = 62218
    FILE_TYPE_BLOCK_DEVICE_FILE: int = 4
    FILE_TYPE_CHARACTER_DEVICE_FILE: int = 3
    FILE_TYPE_DIRECTORY: int = 2
    FILE_TYPE_FIFO: int = 5
    FILE_TYPE_REGULAR_FILE: int = 1
    FILE_TYPE_SOCKET: int = 6
    FILE_TYPE_SYMBOLIC_LINK: int = 7
    FILE_TYPE_UNKNOWN: int = 0
    INCOMPAT_64BIT: int = 128
    INCOMPAT_COMPRESSION: int = 1
    INCOMPAT_CSUM_SEED: int = 8192
    INCOMPAT_DIRDATA: int = 4096
    INCOMPAT_EA_INODE: int = 1024
    INCOMPAT_ENCRYPT: int = 65536
    INCOMPAT_EXTENTS: int = 64
    INCOMPAT_FILETYPE: int = 2
    INCOMPAT_FLEX_BG: int = 512
    INCOMPAT_INLINE_DATA: int = 32768
    INCOMPAT_JOURNAL_DEV: int = 8
    INCOMPAT_LARGEDIR: int = 16384
    INCOMPAT_META_BG: int = 16
    INCOMPAT_MMP: int = 256
    INCOMPAT_RECOVER: int = 4
    I_MODE_MASK: int = 61440
    RO_COMPAT_BIGALLOC: int = 512
    RO_COMPAT_BTREE_DIR: int = 4
    RO_COMPAT_DIR_NLINK: int = 32
    RO_COMPAT_EXTRA_ISIZE: int = 64
    RO_COMPAT_GDT_CSUM: int = 16
    RO_COMPAT_HAS_SNAPSHOT: int = 128
    RO_COMPAT_HUGE_FILE: int = 8
    RO_COMPAT_LARGE_FILE: int = 2
    RO_COMPAT_METADATA_CSUM: int = 1024
    RO_COMPAT_PROJECT: int = 8192
    RO_COMPAT_QUOTA: int = 256
    RO_COMPAT_READONLY: int = 4096
    RO_COMPAT_REPLICA: int = 2048
    RO_COMPAT_SPARSE_SUPER: int = 1
    SUPER_BLOCK_MAGIC: int = 61267
    S_IFBLK: int = 24576
    S_IFCHR: int = 8192
    S_IFDIR: int = 16384
    S_IFIFO: int = 4096
    S_IFLNK: int = 40960
    S_IFREG: int = 32768
    S_IFSOCK: int = 49152
    S_IRGRP: int = 32
    S_IROTH: int = 4
    S_IRUSR: int = 256
    S_ISGID: int = 1024
    S_ISUID: int = 2048
    S_ISVTX: int = 512
    S_IWGRP: int = 16
    S_IWOTH: int = 2
    S_IWUSR: int = 128
    S_IXGRP: int = 8
    S_IXOTH: int = 1
    S_IXUSR: int = 64



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
