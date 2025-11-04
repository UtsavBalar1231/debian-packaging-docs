# PackagingTools - Debian Wiki

**Source:** https://wiki.debian.org/PackagingTools

---

Tools to help with the packaging process. For more information about packaging, see [Packaging](/Packaging). For tools to create basic Debian packages, see [AutomaticPackagingTools](/AutomaticPackagingTools).

Contents

1. [Package maintenance tools](#Package_maintenance_tools)
   1. [Automatic packaging tools](#Automatic_packaging_tools)
   2. [Automatic debian/copyright tools](#Automatic_debian.2Fcopyright_tools)
   3. [Package-checking tools](#Package-checking_tools)
2. [Package build tools](#Package_build_tools)
3. [Debian repository build tools](#Debian_repository_build_tools)
4. [Tools to create a build system](#Tools_to_create_a_build_system)
   1. [Wrappers](#Wrappers)
5. [See also](#See_also)

# Package maintenance tools

Tools to manage the overall process of packaging software.

* [git-buildpackage](/git-buildpackage)

  + for use with [git](/git) repositories
  + **Features**

    - *Language:* Python
* [git-dpm](/PackagingWithGit/GitDpm)

  + **Features**

    - *Language:* shell
* [gitpkg](https://packages.debian.org/gitpkg "DebianPkg")

  + **Features**

    - *Language:* shell
* [svn-buildpackage](/svn-buildpackage)

  + for use with [Subversion](/Subversion) repositories
  + **Features**

    - *Language:* Perl
* [cvs-buildpackage](https://packages.debian.org/cvs-buildpackage "DebianPkg")

  + for use with [CVS](/CVS) repositories
  + removed in [trixie](/DebianTrixie)
  + **Features**

    - *Language:* Perl
* [brz-debian](/BzrBuildpackage)

  + for use with Breezy repositories
  + **Features**

    - *Language:* Python
* [darcs-buildpackage](/PackagingWithDarcs)

  + for use with Darcs repositories
  + **Features**

    - *Language:* C

## Automatic packaging tools

Tools to create basic working Debian packages.

See [AutomaticPackagingTools](/AutomaticPackagingTools).

## Automatic debian/copyright tools

Tools to maintain copyright information in debian/copyright.

See [CopyrightReviewTools](/CopyrightReviewTools).

## Package-checking tools

Tools to ensure your package conforms to various requirements and guidelines.

* [adequate](https://packages.debian.org/adequate "DebianPkg")

  + checks installed packages for bugs and policy violations
  + may be useful as an [autopkgtest](/autopkgtest)
  + **Features**

    - *Language:* Perl
* [blhc](/blhc)

  + find missing [hardening](/Hardening) tags in complex build systems
  + **Features**

    - *Language:* Perl
* [autopkgtest](/autopkgtest)

  + tests binary packages as specified by their source packages
  + **Features**

    - *Language:* Python
* [lintian](/Lintian)

  + reports bugs and policy violations
  + **Features**

    - *Language:* Perl
* [piuparts](/piuparts)

  + checks packages handle installation, upgrading, and removal correctly
  + **Features**

    - *Language:* Python
* [ratt](https://packages.debian.org/ratt "DebianPkg")

  + rebuilds reverse-build-dependencies of a .changes file

    - e.g. check whether your new library version breaks any existing packages
  + **Features**

    - *Language:* C

---

# Package build tools

Tools to build .deb packages from Debian-formatted sources.

* [sbuild](/sbuild)

  + used by official [buildd](/buildd)s
  + chroot/unshare/schroot for isolation
  + calls autopkgtest, which uses schroot/lxc/chroot/qemu/ssh for isolation
  + **Features**

    - *Language:* Perl
* [pbuilder](/pbuilder)

  + chroot for isolation
  + **Features**

    - *Language:* Bash
* [cowbuilder](/cowbuilder)

  + chroot for isolation
  + [cowdancer](https://packages.debian.org/cowdancer "DebianPackage") via LD\_PRELOAD for copy-on-write
  + **Features**

    - *Language:* C
* [qemubuilder](/qemubuilder)

  + qemu for isolation
  + **Features**

    - *Language:* C
* [debspawn](/Packaging/debspawn)

  + systemd-nspawn for isolation
  + **Features**

    - *Language:* Python
* [conbuilder](https://salsa.debian.org/federico/conbuilder)

  + systemd-nspawn for isolation
  + **Features**

    - *Language:* Python
* [whalebuilder](https://packages.debian.org/whalebuilder "DebianPackage") (package)

  + docker for isolation
  + **Features**

    - *Language:* Ruby
* [whalebuilder](https://github.com/rockstorm101/whalebuilder) (script)

  + docker for isolation
  + not related to [whalebuilder](https://packages.debian.org/whalebuilder "DebianPackage")
  + **Features**

    - *Language:* Shell
* [docker-buildpackage](https://github.com/metux/docker-buildpackage)

  + docker for isolation
  + **Features**

    - *Language:* Bash
* [debocker](https://packages.debian.org/debocker "DebianPackage")

  + docker for isolation
  + **Features**

    - *Language:* Python
* [debdocker](https://salsa.debian.org/spog/debdocker)

  + docker for isolation
  + **Features**

    - *Language:* Bash
* [deb-build-pkg](https://github.com/resnullius/deb-build-pkg)

  + docker for isolation
  + **Features**

    - *Language:* Bash
* [DUE](https://github.com/CumulusNetworks/DUE/)

  + docker for isolation
  + **Features**

    - *Language:* Bash
* [rocm-builder](https://salsa.debian.org/rocm-team/community/rocm-builder)

  + docker for isolation
  + **Features**

    - *Language:* Bash
* [docker-deb-builder](https://github.com/tsaarni/docker-deb-builder)

  + docker for isolation
  + **Features**

    - *Language:* Shell
* [debpic](https://github.com/aidan-gallagher/debpic)

  + docker for isolation
  + integrates with Jenkins & VSCode
  + **Features**

    - *Language:* Python
* [Debcraft](https://salsa.debian.org/otto/debcraft)

  + podman and docker for isolation
  + all steps automated, easiest to use
  + **Features**

    - *Language:* shell
* [bampkgbuild](https://github.com/brianmay/bampkgbuild)

  + docker for isolation
  + **Features**

    - *Language:* Python

---

# Debian repository build tools

Tools to maintain APT-compatible repositories of packages.

See [DebianRepository/Setup](/DebianRepository/Setup)

---

# Tools to create a build system

Tools to create minimal Debian systems for building packages.

* [debootstrap](/debootstrap)

  + works on systems without apt, used in d-i
  + **Features**

    - *Language:* shell, Perl
    - *Formats:* directory
* [cdebootstrap](/cdebootstrap)

  + **Features**

    - *Formats:* directory
* [mmdebstrap](https://packages.debian.org/mmdebstrap "DebianPackage")

  + no superuser privileges required
  + multiple mirrors possible
  + stable includes security mirrors by default
  + twice as fast as debootstrap
  + chroots with only Essential:yes or without apt possible
  + bit-by-bit reproducible with SOURCE\_DATE\_EPOCH set
  + foreign architecture chroots supported
  + **Features**

    - *Language:* Perl, Python
    - *Formats:* directory, tarball, ext2, squashfs, null
* sbuild-createchroot

  + deprecated - use mmdebstrap instead
* [zdebootstrap](https://git.sr.ht/~kilobyte/zdebootstrap)

  + research project for fast install bootstrap through parallelism
  + **Features**

    - *Language:* C++
    - *Formats:* directory
* [crosshurd](https://packages.debian.org/crosshurd "DebianPackage")

  + **Features**

    - *Formats:* directory
* [rinse](https://packages.debian.org/rinse "DebianPackage")

  + only for rpm packages
  + build rpm distro chroot on Debian
  + **Features**

    - *Language:* Perl
    - *Formats:* directory
* [fai-server](https://packages.debian.org/fai-server "DebianPackage")

  + [fai](/FAI) dirinstall creates a chroot
  + **Features**

    - *Language:* shell, Perl
    - *Formats:* directory

## Wrappers

Specialisations of the above tools.

* [vmdb2](https://packages.debian.org/vmdb2 "DebianPkg")

  + vmdebootstrap successor
  + **Features**

    - *Language:* python, configuration specified in yaml
    - *Read-only/Writable:* read/write
    - *Formats:* raw
* [qemu-debootstrap](https://packages.debian.org/qemu-user-static "DebianPkg")

  + little shell wrapper around debootstrap
  + supports multiple architectures via qemu-user
  + **Features**

    - *Language:* shell
    - *Formats:* directory
* [DQIB](https://gitlab.com/giomasce/dqib)

  + wrapper around mmdebstrap
  + **Features**

    - *Language:* shell
    - *Formats:* ZIP file containing rootfs, kernel, initrd
* [bdebstrap](https://github.com/bdrung/bdebstrap)

  + wrapper around mmdebstrap for YAML configuration
  + **Features**

    - *Language:* Python
* [deb-bpo-builder](https://git.vv221.fr/deb-bpo-builder/)

  + wrapper around mmdebstrap
  + targeted at building Debian testing → stable backports
  + **Features**

    - *Language:* shell
* [debuerreotype](https://packages.debian.org/debuerreotype "DebianPackage")

  + wrapper around debootstrap
  + reproducible rootfs builds (especially for application containers)
  + **Features**

    - *Language:* Bash
* [grml-debootstrap](https://packages.debian.org/grml-debootstrap "DebianPackage")

  + wrapper around mmdebstrap
  + **Features**

    - *Language:* Bash

---

# See also

* [PackagesForBuildingPackages](/PackagesForBuildingPackages) - should always be installed build environments
* other packaging solutions 
  + [Open Suse Build Service](/OpenSuseBuildService)
* [SystemBuildTools](/SystemBuildTools)

* package/system hybrids 
  + [other packaging solutions](/PackageManagement#Other_packaging_solutions) blur the line between packages and whole systems
  + [docker](https://packages.debian.org/docker.io "DebianPkg") and [podman](https://packages.debian.org/podman "DebianPkg") can be used like whole systems or just sandboxed apps

---

[CategorySoftware](/CategorySoftware) [CategoryPackaging](/CategoryPackaging)