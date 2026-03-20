# Packaging/Pre-Requisites - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites

---

[Translation(s)](/DebianWiki/EditorGuide#translation): [English](/Packaging/Pre-Requisites) - [Português (Brasil)](/pt_BR/Packaging/Pre-Requisites)

Contents

1. [Option 1: Incus](#Option_1:_Incus)
2. [Option 2: Systemd Nspawn and Debspawn](#Option_2:_Systemd_Nspawn_and_Debspawn)
3. [Option 3: Schroot and Sbuild](#Option_3:_Schroot_and_Sbuild)
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

* [Using Systemd Nspawn](/Packaging/Pre-Requisites/nspawn) for creating a sid development environment.
* [Using debspawn](/Packaging/debspawn) for clean build. sbuild can be used as an alternative to debspawn.

## Option 3: Schroot and Sbuild

If you already have a Debian stable or Debian-based distribution (Arch also has schroot package, though if you have a different distro, you need to check if it has schroot package), this option is best for you.

* [Using schroot](https://wiki.debian.org/Packaging/Pre-Requisites/chroot) for creating a sid development environment.

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

The installed WSL2 doesn't come with an "out of the box" setup for schroot. You will need to setup schroot (from [Option 3](/Packaging/Pre-Requisites#Option_3:_Schroot_and_Sbuild)) after [installing a Debian distro](https://docs.microsoft.com/en-us/windows/wsl/install#change-the-default-linux-distribution-installed) on WSL2.

---

* [CategoryPackaging](/CategoryPackaging)