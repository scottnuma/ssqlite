#include <nfs4_internal.h>

struct codepoint nfsops[] = {
{"ACCESS"               , 3},
{"CLOSE"                , 4},
{"COMMIT"               , 5},
{"CREATE"               , 6},
{"DELEGPURGE"           , 7},
{"DELEGRETURN"          , 8},
{"GETATTR"              , 9},
{"GETFH"                , 10},
{"LINK"                 , 11},
{"LOCK"                 , 12},
{"LOCKT"                , 13},
{"LOCKU"                , 14},
{"LOOKUP"               , 15},
{"LOOKUPP"              , 16},
{"NVERIFY"              , 17},
{"OPEN"                 , 18},
{"OPENATTR"             , 19},
{"OPEN_CONFIRM"         , 20},
{"OPEN_DOWNGRADE"       , 21},
{"PUTFH"                , 22},
{"PUTPUBFH"             , 23},
{"PUTROOTFH"            , 24},
{"READ"                 , 25},
{"READDIR"              , 26},
{"READLINK"             , 27},
{"REMOVE"               , 28},
{"RENAME"               , 29},
{"RENEW"                , 30}, 
{"RESTOREFH"            , 31},
{"SAVEFH"               , 32},
{"SECINFO"              , 33},
{"SETATTR"              , 34},
{"SETCLIENTID"          , 35}, 
{"SETCLIENTID_CONFIRM"  , 36}, 
{"VERIFY"               , 37},
{"WRITE"                , 38},
{"RELEASE_LOCKOWNER"    , 39}, 
{"BACKCHANNEL_CTL"      , 40},
{"BIND_CONN_TO_SESSION" , 41},
{"EXCHANGE_ID"          , 42},
{"CREATE_SESSION"       , 43},
{"DESTROY_SESSION"      , 44},
{"FREE_STATEID"         , 45},
{"GET_DIR_DELEGATION"   , 46},
{"GETDEVICEINFO"        , 47},
{"GETDEVICELIST"        , 48},
{"LAYOUTCOMMIT"         , 49},
{"LAYOUTGET"            , 50},
{"LAYOUTRETURN"         , 51},
{"SECINFO_NO_NAME"      , 52},
{"SEQUENCE"             , 53},
{"SET_SSV"              , 54},
{"TEST_STATEID"         , 55},
{"WANT_DELEGATION"      , 56},
{"DESTROY_CLIENTID"     , 57},
{"RECLAIM_COMPLETE"     , 58},
{"ALLOCATE"             , 59},
{"COPY"                 , 60},
{"COPY_NOTIFY"          , 61},
{"DEALLOCATE"           , 62},
{"IO_ADVISE"            , 63},
{"LAYOUTERROR"          , 64},
{"LAYOUTSTATS"          , 65},
{"OFFLOAD_CANCEL"       , 66},
{"OFFLOAD_STATUS"       , 67},
{"READ_PLUS"            , 68},
{"SEEK"                 , 69},
{"WRITE_SAME"           , 70},
{"CLONE"                , 71},
{"ILLEGAL"              , 10044},
{0, 0}};

struct codepoint attributes[] = {
    {"TYPE",  1},
    {"INO",   19},
    {"MODE",  33},
    {"UID",   36},
    {"GID",   37},
    {"SIZE",  4},
    {"ACCESS_TIME", 47},
    {"MODIFY_TIME", 53},
    {0, 0}};


struct codepoint nfserrs[] = {
    {"NFS4_OK",                                          0},
    {"NFS4_EPERM    Operation not permitted",           -1},
    {"NFS4_ENOENT   No such file or directory",         -2},
    {"NFS4_EIO      I/O error",                         -5},
    {"NFS4_ENXIO    No such device or address",         -6},
    {"NFS4_EBADF    Bad file number",                   -9},
    {"NFS4_EAGAIN   Try again",                        -11},
    {"NFS4_ENOMEM   Out of memory",                    -12},
    {"NFS4_EACCES   Permission denied",                -13},
    {"NFS4_EFAULT   Bad address",                      -14},
    {"NFS4_ENOTBLK  Block device required",            -15},
    {"NFS4_EBUSY    Device or resource busy",          -16},
    {"NFS4_EEXIST   File exists",                      -17},
    {"NFS4_EXDEV    Cross-device link",                -18},
    {"NFS4_ENODEV   No such device",                   -19},
    {"NFS4_ENOTDIR  Not a directory",                  -20},
    {"NFS4_EISDIR   Is a directory",                   -21},
    {"NFS4_EINVAL   Invalid argument",                 -22},
    {"NFS4_ENFILE   File table overflow",              -23},
    {"NFS4_EMFILE   Too many open files",              -24},
    {"NFS4_ETXTBSY  Text file busy",                   -26},
    {"NFS4_EFBIG    File too large",                   -27},
    {"NFS4_ENOSPC   No space left on device",          -28},
    {"NFS4_ESPIPE   Illegal seek",                     -29},
    {"NFS4_EROFS    Read-only file system",            -30},
    {"NFS4_EMLINK   Too many links",                   -31},
    {"NFS4_PROTOCOL protocol/framing error",           -32},
    {0, 0}};

