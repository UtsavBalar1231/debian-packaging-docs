# Packaging/Pre-Requisites - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites

---

[Translation(s)](/DebianWiki/EditorGuide#translation): [English](/Packaging/Pre-Requisites) - [Português (Brasil)](/pt_BR/Packaging/Pre-Requisites)

Contents

1. [Option 1: Incus](#Option_1:_Incus)
2. [Option 2: Systemd Nspawn and Debspawn](#Option_2:_Systemd_Nspawn_and_Debspawn)
3. [Option 3: Schroot and Sbuild](#Option_3:_Schroot_and_Sbuild)
   1. [Configuring locales](#Configuring_locales)
4. [Option 4: LXC](#Option_4:_LXC)
5. [Option 5: Docker](#Option_5:_Docker)
6. [Option 6: Virtual Machine](#Option_6:_Virtual_Machine)
7. [Option 7: Direct/Bare metal install](#Option_7:_Direct.2FBare_metal_install)
8. [Option 8: Window Subsystem for Linux (WSL 2)](#Option_8:_Window_Subsystem_for_Linux_.28WSL_2.29)

You MUST have a [Debian unstable](/DebianUnstable) environment (physical/dual boot, virtual machine, container or a chroot with [schroot](/Schroot)) to create packages suitable for uploading to Debian. See instructions given below to setup Debian Sid. You can use lxc, incus, docker or a virtual machine for development.

Note: The target audience is people just discovering Debian.

Readers note: This page lists 8 different approaches. It doesn't list 8 steps of one approach. You can choose any one approach at a time and follow the instructions under it. For example, if you want to use docker, there is no need to run the commands listed under Schroot/Incus/LXC/Virtual Machine.

If you want to use osx on x86\_64 platform for packaging, refer to docker or virtual machines sections and for arm64 platform use [UTM](https://mac.getutm.app/)

If you don't know about these options, Incus is the recommended option.

## Option 1: Incus

Incus is a fork of LXC/LXD by the original LXD developers. It can create a container or a virtual machine.

If you already setup a sid development environment using one of the methods given above, you can skip this step.

* [Using Incus](/Packaging/Pre-Requisites/Incus) for creating a sid development environment.

## Option 2: Systemd Nspawn and Debspawn

If your host system already has systemd as init system, this would be the best option for you.

* [Using Systemd Nspawn](/Packaging/Pre-Requisites/nspawn) for creating a sid development environment
* [Using debspawn](/Packaging/debspawn) for clean build. sbuild can be used as an alternative to debspawn.

## Option 3: Schroot and Sbuild

If you already have a Debian stable or Debian-based distribution (Arch also has schroot package, though if you have a different distro, you need to check if it has schroot package), this option is best for you. If you are using a chroot for the first time, read this Wikipedia article to learn more <https://en.wikipedia.org/wiki/Chroot>

```
sudo apt install schroot debootstrap
```

Create root file system:

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

To get root shell use,

```
sudo schroot -c debian-sid
```

*W: Failed to change to directory '/ ... is ok.*

```
apt-get update && apt-get install <some-package>
exit
```

To get normal user shell (run schroot as normal user),

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

sbuild is a convenience wrapper script of schroot to build package under specified chroot such as unstable. See [sbuild](/sbuild).

Note: You will need separate chroots for schroot (local development) and sbuild (clean build). Both schroot and sbuild should be setup on the host system (don't try to setup sbuild inside schroot).

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

## Option 4: LXC

If you have trouble setting it up, skip this section and see docker section below.

If you already setup a sid development environment using one of the methods given above, you can skip this step.

* [Using LXC](/Packaging/Pre-Requisites/LXC) for creating a sid development environment.

## Option 5: Docker

If you already setup a sid development environment using one of the methods given above, you can skip this step.

* [Using Docker](/Packaging/Pre-Requisites/Docker) for creating a sid development environment.

## Option 6: Virtual Machine

If you already set up a sid development environment using one of the methods given above, you can skip this step.

* [Using Virtual Box or Vagrant](/Packaging/Pre-Requisites/Virtual-Machine) to create a sid development environment.

## Option 7: Direct/Bare metal install

You can also install Debian unstable in your machine under dual boot configuration or even replacing existing OS. See [DebianUnstable](/DebianUnstable)

## Option 8: Window Subsystem for Linux (WSL 2)

If you already set up a sid development environment using one of the methods given above, you can skip this step.

Debian unstable can also be installed in your local Windows OS machine using [WSL2](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) ([install info](/InstallingDebianOn/Microsoft/Windows/SubsystemForLinux)).

Note that this requires you be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11. See [installing WSL2](https://docs.microsoft.com/en-us/windows/wsl/install).

The installed WSL2 doesn't come with an "out of the box" setup for schroot. You will need to setup schroot (from [Option 2](/Packaging/Pre-Requisites#Option_2:_Schroot_and_Sbuild)) after [installing a Debian distro](https://docs.microsoft.com/en-us/windows/wsl/install#change-the-default-linux-distribution-installed) on WSL2.

---

* [CategoryPackaging](/CategoryPackaging)