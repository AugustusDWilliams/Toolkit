# SSH iPhone KeyGen Guide

Create SSH Key
```shell
ssh-keygen -t rsa
```

Copy the public key file to the iPhone
```shell
scp id_rsa.pub root@iPhone_IPADDR
* Enter Password
```

Copy the public key to authorized_keys file
```shell
ssh root@iPhone_IPADDR
* Enter Password
mkdir .ssh
cat id_rsa.pub >> .ssh/authorized_keys
rm id_rsa
chmod 644 .ssh/authorized_keys
chmod 700 .ssh
exit
```

Verify the results
```shell
ssh root@iPhone_IPADDR
* No Password Should Be Required
exit
```
