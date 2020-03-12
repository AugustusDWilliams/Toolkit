# SSH KeyGen Guide

Start key generation program
```shell
ssh-keygen
```

Copy the public key to the remote host
```shell
ssh-copy-id -i ~/.ssh/id_rsa.pub username@host:/.ssh/authorized_keys/
Password: [Enter Password]
```

Verify the results
```shell
ssh -i ~/.ssh/id_rsa username@host
exit
ssh username@host
exit
```

Create SSH Config File
```shell
touch ~/.ssh/config
```

Create Forwarding Agent (Alias)
```shell
nano ~./ssh/config
Host alias
  HostName host(url or ipaddress)
  User username
*save*
```

Verify the results
```shell
ssh alias
exit
```