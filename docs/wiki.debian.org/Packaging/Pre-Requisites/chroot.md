# Packaging/Pre-Requisites/chroot - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites/chroot

---

Contents

1. [Sid environment with Schroot](#Sid_environment_with_Schroot)
   1. [Install basic tools](#Install_basic_tools)
   2. [Create root file system](#Create_root_file_system)
   3. [Getting root shell](#Getting_root_shell)
   4. [Getting normal user shell (running schroot as normal user)](#Getting_normal_user_shell_.28running_schroot_as_normal_user.29)
   5. [Configuring locales](#Configuring_locales)
   6. [Notes on Packaging](#Notes_on_Packaging)

## Sid environment with Schroot

If you are using a chroot for the first time, read this Wikipedia article to learn more <https://en.wikipedia.org/wiki/Chroot>

### Install basic tools

```
sudo apt install schroot debootstrap
```

### Create root file system

```
sudo mkdir -p /srv/chroot/debian-sid
sudo debootstrap sid /srv/chroot/debian-sid
```

If you have an unreliable internet connection, you may want to use apt-cacher-ng to store and reuses already downloaded debs when you retry the debootstrap command.

sudo apt install apt-cacher-ng auto-apt-proxy debian-archive-keyring

sudo auto-apt-proxy debootstrap sid /srv/chroot/debian-sid

Create a text file */etc/schroot/chroot.d/debian-sid* with your favorite text editor (for example nano)

```
sudo nano /etc/schroot/chroot.d/debian-sid
```

and add the following lines in it:

```
# schroot chroot definitions.
# See schroot.conf(5) for complete documentation of the file format.
#
# Please take note that you should not add untrusted users to
# root-groups, because they will essentially have full root access
# to your system.  They will only have root access inside the chroot,
# but that's enough to cause malicious damage.
#
# The following lines are examples only.  Uncomment and alter them to
# customise schroot for your needs, or create a new entry from scratch.
#
[debian-sid]
description=Debian Sid for building packages suitable for uploading to Debian
type=directory
directory=/srv/chroot/debian-sid
users=<your username>
root-groups=root
personality=linux
preserve-environment=true
```

Where <your username> is an underprivileged user on your host system.

### Getting root shell

```
sudo schroot -c debian-sid
```

*W: Failed to change to directory '/ ... is ok.*

```
apt-get update && apt-get install <some-package>
exit
```

### Getting normal user shell (running schroot as normal user)

```
schroot -c debian-sid
```

*Error: pkg: unrecoverable fatal error, aborting: unknown system group 'apt-cacher-ng' in statoverride file*

:   If you encountered this error, follow these steps ( this should be done inside chroot ) to remove it
:   1. Open *"/var/lib/dpkg/statoverride"*

```
nano /var/lib/dpkg/statoverride
```

:   2. Remove this line: *"root apt-cacher-ng 640 /etc/apt-cacher-ng/security.conf"* from the file and save it.

### Configuring locales

After you have set up the chroot, you also need to enable default locale of your host in the chroot as well.

To do this, go to the chroot

```
sudo schroot -c debian-sid
```

And run as root user in chroot:

```
# apt install locales
# dpkg-reconfigure locales
```

Now configure your locales according to the instructions on the screen.

### Notes on Packaging

sbuild is a convenience wrapper script of schroot to build package under specified chroot such as unstable. See [sbuild](/sbuild).

Note: For Packaging you will need separate chroots for schroot (local development) and sbuild (clean build). Both schroot and sbuild should be setup on the host system (don't try to setup sbuild inside schroot).