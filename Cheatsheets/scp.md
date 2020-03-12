# SCP Ecamples

Copy a file from a remote host to a local directory:

```bash
scp username@host_ip:/remote_directory/file.txt /local_directory/
```

Copy a file from a local directory to a remote host:

```bash
scp /local_directory/file.txt username@host_ip:/remote_directory/
```

Copy a remote directory to a local directory:

```bash
scp -r username@host_ip:/remote_directory/ /local_directory/
```

Copy a local directory to a remote host:

```bash
scp /local_directory/ username@host_ip:/remote_directory/
```
