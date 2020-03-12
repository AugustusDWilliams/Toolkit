# Ubuntu Boot Loop Troubleshooting Guide

- If needed press to bring up login terminal, enter:
```bash
Ctrl + Alt + F3

```
- At the login terminal enter your username and password
- Login as root
```bash
sudo -i
```
- To temporarily restore the GUI, enter:
```bash
mount -o rw,remount /
```
- Login as regular
- Open a terminal and enter:
```bash
sudo gedit /etc/fstab
```
- Add the following line to the end of the file
```bash
/dev/sda6 / ext4 defaults 1 1
```