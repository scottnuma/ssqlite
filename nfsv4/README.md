        int nfs4_create(char *hostname, nfs4 *dest)
        void nfs4_destroy(nfs4)
        char *nfs4_error_string(nfs4 n)

the api requires that you. currently you cant specify the port (fix).

`nfs4_error_string` returns a human readable context string for the last
error presented on this nfs4 instance.

        int nfs4_open(nfs4 n, char *filename, int flags, nfs4_properties p, nfs4_file *dest)
        int nfs4_close(nfs4_file fd)

where flags are

        NFS4_RDONLY 
        NFS4_WRONLY 
        NFS4_CREAT 
        NFS4_TRUNC  - must be opened for writing, truncates the file on open
        NFS4_SERVER_ASYNCH 

returns a file

        int nfs4_pwrite(nfs4_file f, void *source, bytes offset, bytes length)
        int nfs4_pread(nfs4_file f, void *buf, bytes offset, bytes length)
        int nfs4_append(nfs4_file f, void *source, bytes offset)

read or write
   
        void nfs4_set_default_properties(nfs4 n, nfs4_properties p)
        int nfs4_stat(nfs4 n, char *path, nfs4_properties p)
        int nfs4_fstat(nfs4_file fd, nfs4_properties p)

        int nfs4_mkdir(nfs4 n, char *path, nfs4_properties p)

if the leading elements of path point to a directory, then nfs4_mkdir creates a new
directory with the trailing element, with the mode taken from the
passed properties.

        int nfs4_unlink(nfs4 n, char *path)

removes the file from its containing path. should verify, but the
unix semantics about removing all the children before the parent
can be removed apply.

        int nfs4_opendir(nfs4, char *path, nfs4_dir *)
        int nfs4_readdir(nfs4_dir, nfs4_properties d)
        int nfs4_closedir(nfs4_dir)

readdir iterates over the object returned by opendir, and returns
NFS4_ENOENT after all the entries are exhausted. all defined
properties of the file should be set. the standard unix
hardlinks for . and .. are not defined by the server.

        int nfs4_lock_range(nfs4_file f, int locktype, bytes offset, bytes length)
        int nfs4_unlock_range(nfs4_file f, int locktype, bytes offset, bytes length)
   
special token NFS4_ENTIRE_FILE when passed into the length
[timeout semantics]

## Environment Variables for Configuration

NFS_AUTH_NULL: in `allocate_rpc` pushes null authentication rather than system default authentication

NFS_TCP_NODELAY: in `nfs4_connect`

NFS_USE_ROOTFH: in `rpc_connection` sends an operation to set the root file handle

NFS_IGNORE_SIGPIPE: in `nfs4_create` uses `signal` to ignore the `SIGPIPE` signal

NFS_PACKET_TRACE: upon `rpc_send` will print `sent [often lengthy contents of sent buffer]`

NFS_TRACE: upon `push_op` will print `pushed op: [OPERATION]_ID`

NFS_DECODE_TRACE: in `parse_response` print the start and finish of decoding a portion of a buffer

NFS_PUSH_SEQ_TRACE: in `parse_sequence` print the sequence number in hex

NFS_RECLAIM_TRACE: in `reclaim_complete` print content of reclaim op buffer
